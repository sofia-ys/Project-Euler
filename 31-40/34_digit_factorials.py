import math 

def check_factorial(n):
    nstr = str(n)
    sum = 0
    for digit in nstr:
        sum += math.factorial(int(digit))
    
    return sum == n

# finding the mathematical limit for when the sum of factorials cannot be biiger
digit = 1
limit_sum = 1
while limit_sum >= digit:
    limit_sum = int(len(str(digit))) * math.factorial(9)

    print(limit_sum, digit)

    digit *= 10

limit = limit_sum

i = 3  # ignoring 1! and 2!
factorial_sums = []

while i < limit:
    if check_factorial(i):
        factorial_sums.append(i)

    i += 1

print(sum(factorial_sums))