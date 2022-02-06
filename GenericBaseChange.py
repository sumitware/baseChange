# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 23:31:57 2022

@author: 91983
"""
from datetime import datetime


def toStr(n,base):
   convertString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]



date2str = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
print(date2str)
# removal of :,-,.
date2str = date2str.replace(":","")
date2str = date2str.replace("-","") 
date2str = date2str.replace(".","") 
date2str = date2str.replace(" ","") 
print(date2str[2:])
print(date2str[2:-16])
print(date2str[4:-14])
print(date2str[6:-12])
print(date2str[8:-10])
print(date2str[10:-6])

print(toStr(int(date2str[2:-16]),36)) # converting YY into 1 char base32
print(toStr(int(date2str[4:-14]),36)) # converting MM into 1 char base32
print(toStr(int(date2str[6:-12]),36)) # converting DD into 1 char base32
print(toStr(int(date2str[8:-10]),36)) # converting hh into 1 char base32
print(toStr(int(date2str[10:-6]),36)) # converting mmss into 3 char base32
#print(toStr(int(date2str[2:-16]),36))+ toStr(int(date2str[4:-14]),36))+ toStr(int(date2str[6:-12]),36))+toStr(int(date2str[8:-10]),36))+
toStr(int(date2str[10:-6]),36)))


