import csv
import pandas
import matplotlib.pyplot as plt
import numpy as np

FILENAME = "allyears2k.csv"

from pandas import read_csv

all_flights = read_csv(FILENAME, sep=',', encoding='utf-8', low_memory=False)
all_flights_no_delays_short = all_flights.loc[(all_flights["IsArrDelayed"]=="NO") & (all_flights["IsDepDelayed"]=="NO"), ["Year", "UniqueCarrier", "FlightNum","DayOfWeek"]]

dayOfWeekFlight = dict(all_flights['DayOfWeek'].value_counts())

dayOfWeekFlightOnTime = dict(all_flights_no_delays_short['DayOfWeek'].value_counts())

##print (dict(all_flights['DayOfWeek'].value_counts()))
##print (len(dict(all_flights['DayOfWeek'].value_counts())))
##print()
##print (dict(all_flights_no_delays_short['DayOfWeek'].value_counts()))
##print (len(dict(all_flights_no_delays_short['DayOfWeek'].value_counts())))

##'''For taking in account only flights that are more than 10''' 
##for i in distanceOnTime:
##    if distanceOnTime[i]<=10:distanceOnTime[i]=0

'''For receiving frequency in %'''    
def frequency(nom,denom):
    #print ('Frequency(%) is following (higher is better):')
    #We create dictionary and inserting calculated values
    d={}
    try:
        for i in denom: 
            #print (i,' ',int(nom[i]/denom[i]*100),'%')
            d[i]=round(float(nom[i]/denom[i]*100),2)
    except KeyError:
        d[i]=0.00
    return d

mydict=frequency(dayOfWeekFlightOnTime,dayOfWeekFlight)

'''For setting the highest value to the first position'''
def sortByValue(x):
    y={}
    for k,v in x.items():
        y[v]=k
    return (sorted(y.items(), reverse=True))

print (sortByValue(mydict))

x=[]
for i in sortByValue(mydict):
    x.append(i[1])

y=[]
for i in sortByValue(mydict):
    y.append(i[0])
    
x=np.array(x)
y=np.array(y)


fig, ax = plt.subplots()
fit = np.polyfit(x, y, deg=1)
ax.plot(x, fit[0] * x + fit[1], color='red')
ax.scatter(x, y)

plt.xlabel('Distance, miles')
plt.ylabel('Flights without delays,%')
plt.title('Regression analysis of coming on time frequency and distance')
fig.show()

'''Some statistical key figures'''
meanX=np.mean(x)
meanY=np.mean(y)
stdX=np.std(x)
stdY=np.std(y)
coefVarX=stdX/meanX
coefVarY=stdY/meanY

'''Pearson product-moment correlation coefficient'''
def pearson(x,y):
    n=len(x)
    vals=range(n)
    # Простые суммы
    sumx=sum([float(x[i]) for i in vals])
    sumy=sum([float(y[i]) for i in vals])
    # Суммы квадратов
    sumxSq=sum([x[i]**2.0 for i in vals])
    sumySq=sum([y[i]**2.0 for i in vals])
    # Сумма произведений
    pSum=sum([x[i]*y[i] for i in vals])
    # Вычисляем коэффициент корреляции Пирсона
    num=pSum-(sumx*sumy/n)
    den=((sumxSq-pow(sumx,2)/n)*(sumySq-pow(sumy,2)/n))**.5
    if den==0: return 0
    r=num/den
    return r


print ('Mean of X axis = ',meanX)
print ('Mean of Y axis = ',meanY)
print ('Standart Deviation of X axis = ',stdX)
print ('Standart Deviation of Y axis = ',stdY)
print ('Coefficient of Variation of X axis = ',coefVarX)
print ('Coefficient of Variation of Y axis = ',coefVarY)
print ('Coefficient of Pearson correlation = ', pearson(x,y))


