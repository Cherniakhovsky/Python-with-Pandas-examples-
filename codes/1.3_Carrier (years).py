import csv
import pandas
from pandas import read_csv

FILENAME = "allyears2k.csv"


all_flights = read_csv(FILENAME, sep=',', encoding='utf-8', low_memory=False)
all_flights_no_delays_short = all_flights.loc[(all_flights["IsArrDelayed"]=="NO") & (all_flights["IsDepDelayed"]=="NO"), ["Year", "UniqueCarrier", "FlightNum","TailNum", "Origin", "Dest"]]

table_all_flights_years=[]
all_years=list(all_flights['Year'].unique())
for i in all_years:
    df=all_flights.loc[(all_flights["Year"]==i), ["Year", "UniqueCarrier", "FlightNum","TailNum", "Origin", "Dest"]]
    print (i, dict(df['UniqueCarrier'].value_counts()))
