def factors(n):
    listoffactors = []
    for i in range(1,10000):
        if n%i == 0:
            listoffactors.append(i)
    return listoffactors

# def primefactors(n):
#     listofprimefactors = []
#     for factor in factors(n):
#         if len(factors(factor)) == 2:
#             listofprimefactors.append(factor)
#     return listofprimefactors

def isPrime(n):
    return factors(n)==[1,n]

def primefactors(n):
    listofprimefactors = []
    for factor in factors(n):
        if isPrime(factor):
            listofprimefactors.append(factor)
    return listofprimefactors


print(max(primefactors(600851475143)))
