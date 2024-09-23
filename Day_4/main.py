"""
def sum(a, b):
    result = a + b
    return result
print(sum(10, 20))

def duplicate(a):
    a *= 10

if __name__ == '__main__':
    m = 100
    duplicate(m)
    print(m)

"""

from math import *

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def sumN(a):
    sum = 0
    for i in range(1, a + 1):
        sum += i
    return sum
    
def sumEv(n):
    sum = 0
    while n != 0:
        temp = n % 10
        if temp % 2 == 0:
            sum += temp
        n //= 10
    return sum

def sumPrime(n):
    sum = 0
    while n != 0:
        temp = n % 10
        if isPrime(temp):
            sum += temp
        n //= 10
    return sum

def transf(n):
    result = 0
    while n != 0:
        temp = n % 10 
        result = result * 10 + temp
        n //= 10
    return result

if __name__ == '__main__':
    print(isPrime(4))
    print(sumN(4))
    print(sumEv(1024))
    print(sumPrime(1235))
    print(transf(1234))