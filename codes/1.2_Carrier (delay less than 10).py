import csv
import pandas


FILENAME = "allyears2k.csv"

from pandas import read_csv

all_flights = read_csv(FILENAME, sep=',', encoding='utf-8', low_memory=False)
all_flights_little_delay = all_flights.loc[(all_flights["ArrDelay"]<10), ["Year", "UniqueCarrier", "FlightNum","ArrDelay", "DepDelay"]]

uniqueCarrierFlights = dict(all_flights['UniqueCarrier'].value_counts())
uniqueCarrierFlightsDelayMax10 = dict(all_flights_little_delay['UniqueCarrier'].value_counts())


##print (dict(all_flights['UniqueCarrier'].value_counts()))
##print (len(dict(all_flights['UniqueCarrier'].value_counts())))
##print()
##print (dict(all_flights_little_delay['UniqueCarrier'].value_counts()))
##print (len(dict(all_flights_little_delay['UniqueCarrier'].value_counts())))
##print()

'''For receiving frequency in % of arrival without delay'''  
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
mydict=frequency(uniqueCarrierFlightsDelayMax10,uniqueCarrierFlights)

'''For setting the highest value to the first position'''
def sortByValue(x):
    y={}
    for k,v in x.items():
        y[v]=k
    return (sorted(y.items(), reverse=True))

print (sortByValue(mydict))

