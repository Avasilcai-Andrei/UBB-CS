# Solve the problem from the second set here
from math import sqrt


def primecheck(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def twinprime(n: int) -> int:
    if n <= 2:
        return 3
    m = n + 1
    if m % 2 == 0:
        m = m + 1
    ok = bool(False)
    while not ok :
        if primecheck(m) == True and primecheck(m + 2) == True:
            return m
        m = m + 1


n = int(input("Please insert the value of n: "))
p1 = twinprime(n)
p2 = p1 + 2
print("The twin prime numbers are: ", p1, " and ", p2)
