# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import math

result=0
for i in range(0,1000):
    if i%3 == 0 or i%5 == 0:
        result += i
print(result)


def valid_num(i):
    return i if i%3 == 0 or i%5 == 0 else 0

result2 =sum(valid_num(i) for i in range(0,1000))
print(result2)