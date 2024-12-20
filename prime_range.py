#!/usr/bin/python

def check_prime(num):
   if(num > 1):
        for i in range(2, int(num**0.5) + 1):
         if (num % i) == 0:
             break
         else:
             print(num)
            
try:
    lower = int(input('Enter start range: '))
    upper = int(input('Enter end range: '))
except:
    exit("Make sure ranges are integers only")

import sys
if(lower < 0 or upper < 0):
    sys.exit("Ranges must be positive numbers")

print("Prime numbers between", lower, "and", upper, "are:")


