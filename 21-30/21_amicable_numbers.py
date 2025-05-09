import numpy as np

def d(n):  # function to find all divisors of any number
    divisors = []
    for i in range(1, n):
        if n % i == 0:  # checking if it divides without remainder
            divisors.append(i)
    return sum(divisors)

amicable = []
for i in range(1, 10000):
    if i == d(d(i)) and i != d(i):  # d(a) = b and d(b) = a where a != b
        amicable.append(i)  # if we meet the conditions we add it to our list

print(sum(amicable))