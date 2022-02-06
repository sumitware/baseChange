#Created on Sat Feb  5 23:31:57 2022 @author: Sumitm@
from datetime import datetime

def base36(n):
   AlphabetSet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   if n < 36:
      return AlphabetSet[n]
   else:
      return base36(n//36) + AlphabetSet[n%36]


date2str = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
print(date2str)
# removal of :,-,.
date2str = date2str.replace(":","")
date2str = date2str.replace("-","") 
date2str = date2str.replace(".","") 
date2str = date2str.replace(" ","") 
# =============================================================================
print(date2str[2:])
# print(date2str[2:-16])
# print(date2str[4:-14])
# print(date2str[6:-12])
# print(date2str[8:-10])
# print(date2str[10:-6])
# 
# print(base36(int(date2str[2:-16])) # converting YY into 1 char base32
# print(base36(int(date2str[4:-14])) # converting MM into 1 char base32
# print(base36(int(date2str[6:-12])) # converting DD into 1 char base32
# print(base36(int(date2str[8:-10])) # converting hh into 1 char base32
# print(base36(int(date2str[10:-6])) # converting mmss into 3 char base32
# =============================================================================
print(base36(int(date2str[2:-16]))+ base36(int(date2str[4:-14]))+ base36(int(date2str[6:-12]))+base36(int(date2str[8:-10]))+
base36(int(date2str[10:-6])))

