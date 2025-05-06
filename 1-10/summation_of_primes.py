# initialising
sum = 0
end = 2000000
primes = []

# function to check if prime
def prime(x, primes):
    if x < 2:  # 1 and 0 are not primes
        return False
    for p in primes:  # comparing to our list of primes
        if p**2 > x:  # if x is smaller than the prime squared, we've "accounted" for it so we can stop
            break
        if x % p == 0:  # if x is divisible by our prime, it's not prime for sure (since all compositite numbers are multiples of primes)
            return False
    return True

for i in range(end):
    if prime(i, primes):  # if i is a prime number
        primes.append(i)  # we'll add it to our list
        sum = sum + i  # and add it to our sum

print(sum)