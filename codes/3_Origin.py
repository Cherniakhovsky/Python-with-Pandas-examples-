import csv
import pandas

FILENAME = "allyears2k.csv"

from pandas import read_csv

all_flights = read_csv(FILENAME, sep=',', encoding='utf-8', low_memory=False)
all_flights_no_delays_short = all_flights.loc[(all_flights["IsArrDelayed"]=="NO"), ["Year", "UniqueCarrier", "FlightNum","TailNum", "Origin", "Dest"]]

origin = dict(all_flights['Origin'].value_counts())

originOnTime = dict(all_flights_no_delays_short['Origin'].value_counts())

'''For taking in account only flights that are more than 10''' 
for i in originOnTime:
    if originOnTime[i]<=10:originOnTime[i]=0

'''For receiving frequency in % of arrival without delay'''    
def frequency(nom,denom):
    #print ('Frequency(%) is following (higher is better):')
    #We create dictionary and inserting calculated values
    d={}
    for i in denom:
        try:
            #print (i,' ',int(nom[i]/denom[i]*100),'%')
            d[i]=round(float(nom[i]/denom[i]*100),2)
        except KeyError:
            d[i]=0.00
    return d

mydict=frequency(originOnTime,origin)

'''For setting the highest value to the first position'''
def sortByValue(x):
    y={}
    for k,v in x.items():
        y[v]=k
    return (sorted(y.items(), reverse=True))

#print (sortByValue(mydict))

'''For showing data that is higher than 50%'''
count=0
for i in sortByValue(mydict):
    count+=1
    if i[0]<=50:break
    
print (sortByValue(mydict)[:count])




