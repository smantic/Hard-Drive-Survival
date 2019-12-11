#!/usr/bin/python3.6


import sqlite3
import statsmodels.api as sm  
from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
from lifelines import NelsonAalenFitter

#durations = [11, 74, 71, 76, 28, 92, 89, 48, 90, 39, 63, 36, 54, 64, 34, 73, 94, 37, 56, 76]
#event_observed = [1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1]

def createSurvivalGraph( durations, event_observed ): 
    kmf = KaplanMeierFitter()
    kmf.fit(durations, event_observed)
    kmf.plot(ci_show=False)

    plt.title("Hard Drive Kaplan Meier Survival Analysis")
    plt.ylabel("Probability a Hard Drive Survives")
    plt.show()



def createHazardGraph( durations, event_observed ): 
    naf = NelsonAalenFitter()
    naf.fit(durations, event_observed)
    naf.plot(ci_show=False)

    plt.title("Hard Drive Nelson-Aalen Hazard Estimate")
    plt.ylabel("Cumulative Hazard")
    plt.show()



def linearRegression(): 
    df_csv = pd.read_csv()

def normalProbablityPlot(): 

    conn = sqlite3.connect("./survival.db")
    c = conn.cursor()

    qresult = c.execute( "SELECT daysAlive FROM Survival" ).fetchall()
    durations = [ int(qresult[i][0]) for i in range(0, len( qresult )) ] 

    ax4 = plt.subplot(224)
    x = stats.norm.rvs(loc=0, scale=1, size=len(durations))

    stats.probplot( durations,plot=plt ) 
    plt.show()

    c.close()
    conn.close()




def histogram( attribute ): 
    conn = sqlite3.connect("./survival.db")
    c = conn.cursor()

    qresult = c.execute( "SELECT daysAlive FROM Survival ORDER BY firstDate ASC" ).fetchall()
    durations = [ int(qresult[i][0]) for i in range(0, len( qresult )) ] 

    x = plt.hist(durations, bins='auto')
    plt.title("Histogram of " + attribute)
    plt.show()

    c.close()
    conn.close()

def histogramCSV( attribute, df): 
    pd.DataFrame.hist( df, attribute, bins='auto' )



def averageTenure(): 
    conn = sqlite3.connect("./survival.db")
    c = conn.cursor()

    qresult = c.execute( "SELECT daysAlive, firstDate FROM Survival ORDER BY firstDate ASC" ).fetchall()
    durations = [ int(qresult[i][0]) for i in range(0, len( qresult )) ] 

    totalAlive = sum(durations)
    
    c.close()
    conn.close()
    
    return totalAlive // len(durations)



def createSurvivalGraphs( ): 

    conn = sqlite3.connect("./survival.db")
    c = conn.cursor()

    qresult = c.execute( "SELECT daysAlive FROM Survival ORDER BY firstDate ASC" ).fetchall()
    durations = [ int(qresult[i][0]) for i in range(0, len( qresult )) ] 

    qresult = c.execute("SELECT eventOccured FROM Survival ORDER BY firstDate ASC").fetchall()
    eventOccurred = [ int(qresult[i][0]) for i in range(0, len(qresult)) ]

    createSurvivalGraph( durations, eventOccurred)
    createHazardGraph(durations, eventOccurred)

    c.close()
    conn.close()


def createSubSurvialGraph( attribute, value ): 

    conn = sqlite3.connect("./survival.db")
    c = conn.cursor()

    qresult = c.execute( "SELECT daysAlive FROM Survival WHERE ? = ? ORDER BY firstDate ASC", (attribute, value) ).fetchall()
    durations = [ int(qresult[i][0]) for i in range(0, len( qresult )) ] 

    qresult = c.execute("SELECT eventOccured FROM Survival WHERE ?=? ORDER BY firstDate ASC", (attribute, value)).fetchall()
    eventOccurred = [ int(qresult[i][0]) for i in range(0, len(qresult)) ]

    createSurvivalGraph( durations, eventOccurred)

    c.close()
    conn.close()


