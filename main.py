#! /usr/bin/python3.6

import graphs 
import os 
import sqlite3
import multiprocessing
import concurrent.futures 
from lifelines import KaplanMeierFitter
import datetime


#probablity density function.
def pdf( t ): 

    conn = sqlite3.connect("./survival.db")
    c = conn.cursor()
    
    numDead = c.execute( "SELECT COUNT(*) FROM Survival WHERE DaysAlive < ?", (t,) ).fetchAll()
    numTotal = c.execute( "SELECT COUNT(*) FROM Survival" ).fetchAll() 

    return numDead // numTotal 


def survival( t ): 
    return 1 - pdf( t ) 


# gives the risk of dying at time t. 
def harzard( t ): 
    return pdf(t)  // survival(t) 

def KCM( t ): 
    
    conn = sqlite3.connect("./survival.db")
    c = conn.cursor()

    durations = c.execute( "SELECT MAX( DaysAlive ) FROM Survival"  ).fetchAll()


    return 0


def eventOccured(): 

    conn = sqlite3.connect("./survival.db")
    c = conn.cursor()

    lastDate = c.execute( "SELECT FirstDate FROM Survival ORDER BY DATE(FirstDate) DESC LIMIT 1").fetchAll()
    print(lastDate.rowcount)

    hds = c.execute( "SELECT FirstDate, SerialNumber, DaysAlive FROM Survival")
    
    for (dateStr, serialNumber, daysAlive) in hds:
        startDate = datetime.datetime.strptime(date, '%Y/%m/%d')

        #add on days Alive to see if hardDrive has died.
        print(startDate) 

    c.close()
    conn.close()
        





def collectDurationsAndEvents( ): 

    conn = sqlite3.connect("./survival.db")
    c = conn.cursor()

    qresult = c.execute( "SELECT DaysAlive FROM Survival" ).fetchall()
    durations = [ qresult[i][0] for i in range(0, len( qresult )) ] 

    eventOccured() 

    #graphs.createSurvivalGraph( durations, eventOccurred)
    #graphs.createHazardGraph(durations, eventOccurred)

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



def main(): 
    paths = collectPaths("./data")

    print("collecting duration from " + paths[0]) 

    run(paths[1])
    run(paths[2])
    #run(paths[10])
    collectDurationsAndEvents()





def main2(): 
    paths = collectPaths("./data")

    executor = concurrent.futures.ProcessPoolExecutor(10)
    futures = [] 
    for path in paths: 
        future = executor.submit( run, path )
        futures.append( future ) 

    concurrent.futures.wait(futures)


#Collect the following information 
#   -Serial Number
#   -Alive? 
def run( path ): 

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
            
            #if it is alive, update it's time alive. 
            if int(failure) == 0: 

                qresult = c.execute( "SELECT * FROM Survival WHERE SerialNumber = ?", (serialNumber,)).fetchall()

                #if we already have an entry for this drive. 
                if len(qresult) > 0: 
                    c.execute( "UPDATE Survival SET DaysAlive = DaysAlive + 1 where SerialNumber = ?", (serialNumber,))

                else: 
                    c.execute("INSERT INTO Survival VALUES(?,?,?)", ( date, serialNumber,1))


    conn.commit()
    c.close()
    conn.close()


main()
