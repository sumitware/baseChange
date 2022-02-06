# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 22:57:36 2022

@author: 91983
"""

# Random number generator 
from datetime import datetime

dt_obj = datetime.strptime('20.12.2016 09:38:42,76',
                           '%d.%m.%Y %H:%M:%S,%f')
millisec = dt_obj.timestamp() * 1000

print(millisec)

print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'))
date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))

print(date_s)

def base36encode(number, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    """Converts an integer to a base36 string."""
    if not isinstance(number, (int, long)):
        raise TypeError('number must be an integer')

    base36 = ''
    sign = ''

    if number < 0:
        sign = '-'
        number = -number

    if 0 <= number < len(alphabet):
        return sign + alphabet[number]

    while number != 0:
        number, i = divmod(number, len(alphabet))
        base36 = alphabet[i] + base36

    return sign + base36


date_q=base36encode('141293')