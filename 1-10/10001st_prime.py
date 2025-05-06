import numpy as np

# initialising
status = True
j = 0
primeNums = []

# function to find the factors of a number up to its square root (so only the first half of the pairs), if this list is longer than 2, it is not prime
def prime(x):
    prime = True
    factors = []
    for i in range(1, int(np.sqrt(x)) + 1):
        if x % i == 0:
            factors.append(i)  # making a list with all the factors of a given number x
            factors.append(int(x/i))
        if len(factors) > 2:  # if this list exceeds 2 at any point, we don't have a prime number
            prime = False
            break
    return prime

while status:
    j = j + 1  # counter
    if prime(j) == True:  # if we have a prime number, add it to the list of primes
        primeNums.append(j)
    
    if len(primeNums) > 10001:  # stop calculating once we have 10001 prime numbers
        status = False

print(primeNums[-1])  # the 10001st prime number