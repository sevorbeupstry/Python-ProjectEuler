import math
def fib(n):   
    """nth number in the fibionacci series"""  
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fib(n-1)+fib(n-2)

sum1=0
for i in range(2,10000000):
    j=fib(i)
    if j > 4000000:
        break
    if j%2 == 0:
        sum1 += j
print(sum1)
