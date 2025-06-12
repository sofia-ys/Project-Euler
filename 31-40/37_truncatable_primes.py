import math
# check if number is prime
def prime(n):
    # if n in primelist:
    #     return True
    divisors = set()
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(abs(n))) + 1):
        if n % i == 0:
            divisors.add(n)
            divisors.add(n/i)
    if len(divisors) == 0:
        # primelist.add(n)
        return True
    return False

def trunc(n):  # direction is r (right) or l (left)
    nstr = str(n)
    for i in range(1, len(nstr)):
        # checking removing from the left
        if not prime(int(nstr[i:])):
            return False
        # removing from the right 
        if not prime(int(nstr[:-i])):
            return False
    return True  # truncatable 

truncatable = []
num = 8  # starting point since 7 is not valid
primelist = set()
while len(truncatable) < 11:

    if prime(num):  # is original number prime?
        if trunc(num):  # is is left and right truncatable?
            truncatable.append(num)
    
    num += 1
# print(primelist)
print(sum(truncatable))