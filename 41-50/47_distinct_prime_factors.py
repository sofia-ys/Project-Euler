import time

start = time.time()

def factors(n):  # function to find all factors of a number
    divisors = []
    for i in range(2, n):
        if n % i == 0:  # checking if it divides without remainder
            divisors.append(i)
    return divisors

def prime(n):
    return factors(n) == []

def conseq(list, n):
    ndx = list.index(n)
    return (list[ndx - 1] == list[ndx] - 1) and (list[ndx - 2] == list[ndx] - 2) and (list[ndx - 3] == list[ndx] - 3)

run = True
n = 4
fourPrime = []
conseqPrimes = []
while run:
    divisors = factors(n)
    primes = []
    for num in divisors:
        if prime(num):
            primes.append(num)

    if len(primes) == 4:  
        fourPrime.append(n)

    if len(fourPrime) > 4:  # we need at least 4 conseq numbers so it has to be at least 4 in the list
        if conseq(fourPrime, fourPrime[-1]):
            conseqPrimes.append(fourPrime[-4])
            conseqPrimes.append(fourPrime[-3])
            conseqPrimes.append(fourPrime[-2])
            conseqPrimes.append(fourPrime[-1])
            run = False

    n = n + 1
    if n % 100 == 0:
        print(n)

end = time.time()

print(conseqPrimes, (end - start))