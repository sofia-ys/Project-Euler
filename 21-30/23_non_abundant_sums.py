import math

def abundant(n):  # function to determine whether a number is abundant
    divisors = []
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:  # checking if it divides without remainder
            divisors.extend((i, n/i))  # adding it to our divisors list
    return n < (sum(divisors) + 1)  # a number is abundant if it is less than the sum of its divisors

def check_sum(n, abundant_nums):
    for num1 in abundant_nums:
        for num2 in abundant_nums:
            if n == num1 + num2:
                return True

abundant_nums = []
not_abundant = []
for i in range(28123):
    if abundant(i):
        abundant_nums.append(i)
    else:
        not_abundant.append(i)

not_sum = []
for num in not_abundant:
    if not check_sum(num, abundant_nums):
        not_sum.append(num)

print(len(not_sum))