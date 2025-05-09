def abundant(n):  # function to determine whether a number is abundant
    divisors = []
    for i in range(1, n):
        if n % i == 0:  # checking if it divides without remainder
            divisors.append(i)  # adding it to our divisors list
    return n < sum(divisors)  # a number is abundant if it is less than the sum of its divisors

'''unfinished'''
