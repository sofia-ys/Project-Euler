import numpy as np
num = 600851475143

# function to find the factors of a number up to its square root (so only the first half of the pairs)
def factors(x):
    factors = []
    for i in range(1, int(np.sqrt(x)) + 1):
        if x % i == 0:
            factors.append(i)
            factors.append(int(x/i))
    return factors

factorsNum = factors(num)  # all factors of our number

for j in range(len(factorsNum)):
    if len(factors(factorsNum[j])) == 2:  # check if each factor is prime
        factorPrime = factorsNum[j]  # replace each time we find a larger prime factor

print(factorPrime)