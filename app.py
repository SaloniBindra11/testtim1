import pandas as pd
import datetime


l=["airbus_india_101_20200711T124523.csv","airbus_india_102_20180913T064523.csv","airbus_india_103_20190203T055043.csv","airbus_india_104_20210409T064503.csv","airbus_india_105_20190409T064503.csv"]



date=[]
l2=[]
d=[]
tt1=[]
tt=[]

# Sorting timestamps
def getSortedTimestamp(l,tt):

  for i in range(len(l)):
    
    s1=l[i].split('_')
    s1=list(s1[-1].split('.'))
    tt1 =pd.Timestamp(s1[0]).strftime('%Y-%m-%d %H:%M:%S')
    
    tt.append(tt1)
    
  tt=sorted(tt)

  return tt

print("\n")
tt=getSortedTimestamp(l,tt)
print("sorted timestamps are")
print(tt)

# Get latest 2 files

def getLatestFiles(tt,date,l2):
  
  
  date1=tt[len(tt)-1]
  
  date2=tt[len(tt)-2]
  #print(date2)
  f1=date1.split("-")
  f2=date2.split("-")
  #print(f1)
  #print(f2)
  
  for i in range(len(l)):
    if f1[0]+f1[1] in l[i]:
      
      l2.append(l[i])
      
    if f2[0]+f2[1] in l[i]:
      
      l2.append(l[i])
      
    
  date.append(date1)
  date.append(date2)

  return date,l2

print("\n")
d=getLatestFiles(tt,date,l2)
print("latest 2 timestamps are",date)
print("\n")
print("latest 2 files are",l2)







