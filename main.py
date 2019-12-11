#! /usr/bin/python3.6

import graphs 
import os 
import sqlite3
import multiprocessing
import concurrent.futures 
from lifelines import KaplanMeierFitter
import datetime
import random
import pandas


#probablity density function.
def pdf( t ): 

    conn = sqlite3.connect("./survival.db")
    c = conn.cursor()
    
    numDead = c.execute( "SELECT COUNT(*) FROM Survival WHERE DaysAlive < ?", (t,) ).fetchall()
    numTotal = c.execute( "SELECT COUNT(*) FROM Survival" ).fetchall() 

    c.close()
    conn.close()

    return numDead // numTotal 


def survival( t ): 
    return 1 - pdf( t ) 


# gives the risk of dying at time t. 
def harzard( t ): 
    return pdf(t)  // survival(t) 

def KCM( t ): 
    
    conn = sqlite3.connect("./survival.db")
    c = conn.cursor()

    durations = c.execute( "SELECT MAX( daysAlive ) FROM Survival"  ).fetchall()

    c.close()
    conn.close()

    return 0


#to be run after collecting all days alive. 
def updateEventOccured(): 

    print("updating lastDate feilds")
    conn = sqlite3.connect("./survival.db")
    c = conn.cursor()

    lastDateStr= c.execute( "SELECT MAX(firstDate) FROM Survival").fetchall()[0][0]
    lastDate = datetime.datetime.strptime( lastDateStr, '%Y-%m-%d')
    

    hds = c.execute( "SELECT firstDate, serialNumber, daysAlive FROM Survival").fetchall()
    
    for (dateStr, serialNumber, daysAlive) in hds:
        startDate = datetime.datetime.strptime(dateStr, '%Y-%m-%d')

        #add on days Alive to see if hardDrive has died.
        endDate = startDate + datetime.timedelta(days=daysAlive)
        endDateStr = endDate.strftime('%Y-%m-%d')
        timeDelta = lastDate - endDate 

        #if the difference is greater than one day.
        if timeDelta.total_seconds() > 86400: 
            eventOccured = 1
        else: 
            eventOccured = 0

        c.execute( "UPDATE Survival SET lastDate = ?, eventOccured = ? where SerialNumber = ?", (endDateStr, eventOccured, serialNumber))

    conn.commit()
    c.close()
    conn.close()




def collectPaths(start): 

    def recHelper( path, result ): 

        if (os.path.isdir( path ) is False):
            result.append( path ) 
            return result 
        else: 
            for f in os.listdir( path ):
                recHelper( path + "/" + f , result )  

    result = []
    if os.path.isdir(start) is True :
        recHelper( start, result )
    return result 



def createGraphs(): 
    #filename = "./aggergated.csv"
    #n = sum(1 for line in open(filename)) - 1 #number of records in file (excludes header)
    #s = 10000 #desired sample size
    #skip = sorted(random.sample(range(1,n+1),n-s)) #the 0-indexed header will not be included in the skip list
    #df = pandas.read_csv(filename, skiprows=skip)


    #graphs.histogram("daysAlive")
    #graphs.histogramCSV("smart_2_normalized", df)
    #graphs.histogramCSV("smart_9_normalized", df)
    #graphs.histogramCSV("smart_200_normalized", df)
    #graphs.normalProbablityPlot()
    graphs.createSurvivalGraphs()
    print("Average tenure is: " + str(graphs.averageTenure()))
    graphs.createSubSurvialGraph( "model", "ST4000DM000")
    graphs.createSubSurvialGraph( "capacity", 4000787030016 ) 


def main2():

    #updateEventOccured()
    createGraphs()



def main(): 
    paths = collectPaths("./data")
    for path in paths: 
        run( path )

    updateEventOccured()

    #executor = concurrent.futures.ProcessPoolExecutor(10)
    #futures = [] 
    #for path in paths: 
    #    future = executor.submit( run, path )
    #    futures.append( future ) 

    #concurrent.futures.wait(futures, timeout=None, return_when=concurrent.futures.ALL_COMPLETED)


#Collect the following information 
#   -Serial Number
#   -Alive? 
def run( path ): 


    print("collecting data from " + path) 
    conn = sqlite3.connect("./survival.db")
    c = conn.cursor()
    
    with open(path) as f: 
        next(f)
        for line in f: 

            #we want the drive serial number, and whether the drive is alive. Index 1 and 4.
            fields = line.split(",")
            serialNumber = fields[1]
            failure = fields[4]
            date = fields[0]
            model = fields[2]
            capacity = fields[3] 
            
            #if it is alive, update it's time alive. 
            if int(failure) == 0: 

                qresult = c.execute( "SELECT * FROM Survival WHERE serialNumber = ?", (serialNumber,)).fetchall()


                #if we already have an entry for this drive. 
                if len(qresult) > 0: 
                    daysAlive = int(qresult[0][4])

                    os.system('clear')
                    print("In: \t " + path ) 
                    print("updating "+ serialNumber + "\tto " + str(daysAlive+1)   )
                    c.execute( "UPDATE Survival SET daysAlive = ? where serialNumber = ?", (daysAlive +1, serialNumber,))

                else: 
                    #last column is last date, will be added later. 
                    c.execute("INSERT INTO Survival VALUES(?,?,?,?,?,?,?)", ( date, serialNumber, model, capacity, 1, 0, "" ))

    conn.commit()
    c.close()
    conn.close()

main2()
