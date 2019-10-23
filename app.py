import pandas as pd
import os
import regex
import datetime
from datetime import timedelta

l=["airbus_india_101_20200711T124523.csv","airbus_india_102_20180913T064523.csv","airbus_india_103_20190203T055043.csv","airbus_india_104_20210409T064503.csv"]
l1=[]
ee=[]
date=[]
l2=[]
e=[]
tt=[]
t=[]
d=[]

def Readcsv(l1):

  for i in range(len(l)):
    f=open(l[i],"w+")
    f.write("hello welcome")
    contents=l[i]
    l1.append(contents)
  #print(l1)
  f.close()
  return l1


ee=Readcsv(l1)
print(ee)
print("\n")

def getSortedTimestamp(ee,t):

  for i in range(len(ee)):
    s1=regex.split("_",ee[i])
    s2=list(s1[3].split("."))
    #print(s2[0])
    tt1 = pd.Timestamp(s2[0]).strftime('%Y-%m-%d %H:%M:%S')
    tt.append(tt1)
  #print(tt)
  t=sorted(tt)

  return t

print("\n")
e=getSortedTimestamp(ee,t)
print("sorted timestamps are")
print(e)


def getLatestFiles(e,date,l2):
  
  m=len(e)
  date1=e[m-1]
  date2=e[m-2]
  f1=regex.split("-",date1)
  f2=regex.split("-",date2)
  
  
  for i in range(len(l)):
    if f1[0]+f1[1] in l[i]:
      #print("file1",l[i])
      l2.append(l[i])
    if f2[0]+f2[1] in l[i]:
      #print("file2",l[i])
      l2.append(l[i])
  date.append(date1)
  date.append(date2)

  return date,l2

print("\n")
d=getLatestFiles(e,date,l2)
print("latest 2 timestamps are",date)
print("\n")
print("latest 2 files are",l2)




