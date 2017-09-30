import csv
import pandas


FILENAME = "allyears2k.csv"

from pandas import read_csv

all_flights = read_csv(FILENAME, sep=',', encoding='utf-8', low_memory=False)
all_flights_no_delays_short = all_flights.loc[(all_flights["IsArrDelayed"]=="NO"), ["Year", "UniqueCarrier", "FlightNum","TailNum", "Origin", "Dest"]]

uniqueCarrierFlights = dict(all_flights['UniqueCarrier'].value_counts())
uniqueCarrierFlightsOnTime = dict(all_flights_no_delays_short['UniqueCarrier'].value_counts())

'''For receiving frequency in %'''  
def frequency(nom,denom):
    #print ('Frequency(%) is following (higher is better):')
    #We create dictionary and inserting calculated values
    d={}
    for i in denom: 
        #print (i,' ',int(nom[i]/denom[i]*100),'%')
        d[i]=round(float(nom[i]/denom[i]*100),2)
    #We are sorting dictionary according key
    #for j in sorted(d.values()):
    #   print (j)
    return d
mydict=frequency(uniqueCarrierFlightsOnTime,uniqueCarrierFlights)

'''For setting the highest value to the first position'''
def sortByValue(x):
    y={}
    for k,v in x.items():
        y[v]=k
    return (sorted(y.items(), reverse=True))

print (sortByValue(mydict))

