num = 20
status = True
i = 0

# chekcing if a value is divisible by 1 through num
def divisible(x):
    divisible = False
    for j in range(1, num + 1):
        if x % j == 0:
            divisible = False  # we want to break our while loop when all numbers are divisible
        else:
            divisible = True
            break
    return divisible

while status:
    i = i + num  # adjusting counter, we know it has to be divisible by num so can skip anything not a multiple of num
    status = divisible(i)  # checking if divisible up to num

print(i)