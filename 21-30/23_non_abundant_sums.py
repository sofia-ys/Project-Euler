import math

def abundant(n):  # function to determine whether a number is abundant
    divisors = {1}  # always includes 1, that way we can skip to checking from 2
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:  # checking if it divides without remainder
            divisors.add(i)
            divisors.add(n//i)  # adding it to our divisors list
    return n < (sum(divisors))  # a number is abundant if it is less than the sum of its divisors

upper_limit = 28123

abundant_nums = []
for i in range(1, upper_limit + 1):  # +1 because the integer 28123 could be 28122 + 1 or something
    if abundant(i):
        abundant_nums.append(i)

abundant_sums = set()  # sums of all abundnat numbers
for j in range(len(abundant_nums)):
    for k in range(j, len(abundant_nums)):  # since same lsit, we can half the comparisons
        if abundant_nums[j] + abundant_nums[k] <= upper_limit:
            abundant_sums.add(abundant_nums[j] + abundant_nums[k])

not_sum = set()
for n in range(1, upper_limit + 1):
    if n not in abundant_sums:
        not_sum.add(n)

print(sum(not_sum))