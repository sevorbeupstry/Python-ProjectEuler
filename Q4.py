# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import string


def isPalindrome(palindrome):
    """Return whether a string is a palindrome"""
    if len(palindrome)<=1:
        return True
    else:
        return palindrome[0] == palindrome[-1] and isPalindrome(palindrome[1:-1]) 
    # palindrome[-1] represents the last digit. one before the first.. 
    # and palindrome[1:-1] represents the rest of the characters after first and last removed

def factors(n):
    listoffactors = []
    for i in range(1,1000000):
        if n%i == 0:
            listoffactors.append(i)
    return listoffactors

def isFactorDigit(num, digit):
    isBroken = False
    fcts = factors(num)
    for i in range(0, len(fcts)):
        for j in range(0, len(fcts)):
            cond = num == fcts[i] * fcts[j] and len(str(fcts[i]))==digit and len(str(fcts[j]))==digit
            if cond:
                print(fcts[i],fcts[j])
                isBroken = True
                break
        if isBroken:
            break
    return cond

# print(isFactorDigit(9009, 2))


# listofpalindromes=[]
for num in range(1000000,10000, -1):
    if not isPalindrome(str(num)):
        continue
    if isFactorDigit(num, 3):
    # listofpalindromes.append(num)
        break
        
print(num)