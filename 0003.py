"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Answer:

"""

import math

value = 600851475143
orig_value = 600851475143

maximum = 775147 
sieve = []
for i in range(maximum + 1):
    sieve.append(True) 

sieve[0] = None
factor = 2
index = 1
while factor < maximum + 1:
    index = factor
    while index + factor < maximum+1:
        index = index + factor
        sieve[index] = False
    factor = factor + 1
    while factor < maximum + 1 and sieve[factor] == False:
        factor = factor + 1

divisor = 2
while value > 1:
    if value % divisor == 0:
        value = value / divisor
        #print("Divisor: {}".format(divisor))
    else:
        for i in range(divisor + 1, maximum + 1):
            if sieve[i]:
                divisor = i
                break

print("Greatest prime divisor of {} is {}".format(orig_value, divisor))
