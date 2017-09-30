import csv
import pandas
import matplotlib.pyplot as plt
import numpy as np

FILENAME = "allyears2k.csv"

from pandas import read_csv

all_flights = read_csv(FILENAME, sep=',', encoding='utf-8', low_memory=False)
#all_flights_no_delays_short = all_flights.loc[(all_flights["ArrDelay"]<=0), ["Year", "UniqueCarrier", "FlightNum","TailNum", "Origin", "Dest", "Distance"]]

#Year = dict(all_flights['Year'].value_counts())

#YearOnTime = dict(all_flights_no_delays_short['Year'].value_counts())

print ('Cancelled: ', dict(all_flights['Cancelled'].value_counts()))
print ('Quanity: ', len(dict(all_flights['Cancelled'].value_counts())))
print ()
print ('Cancellation Code: ', dict(all_flights['CancellationCode'].value_counts()))
print ('Quanity: ', len(dict(all_flights['CancellationCode'].value_counts())))
print ()
print ('Diverted: ', dict(all_flights['Diverted'].value_counts()))
print ('Quanity: ', len(dict(all_flights['Diverted'].value_counts())))
