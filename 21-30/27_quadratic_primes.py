import math

# check if number is prime
def prime(n):
    divisors = set()
    for i in range(2, int(math.sqrt(abs(n))) + 1):
        if n % i == 0:
            divisors.add(n)
            divisors.add(n/i)
    return len(divisors) == 0

# quadratic function n^2 + an + b 
def quad(a, b, n):
    return (n**2 + a*n + b)

abvals = []
numprimes = []
for a in range(-1000, 1000):  # |a| < 1000
    for b in range(-1000, 1001):  # |b| <= 1000
        n = 0  # starting from n = 0
        indiv = []  # storing primes we get with consecutive ns
        while True:
            num = quad(a, b, n)  # getting the quad
            if prime(num):  # if it's prime we add to list
                indiv.append(num)
            else:
                break  # if not prime, we finish our primes list and move onto next a,b
            n += 1  # if it was prime, we now check next conseq n value
        abvals.append((a, b))  # storing our ab values for reference (will have same index and #primes)
        numprimes.append(len(indiv))  # how many consecutive primes we got

maxa, maxb = abvals[numprimes.index(max(numprimes))]  # ab are at the index of the max number of primes
print(maxa * maxb)