ones = []
eightynines = []

def square_digit(i):
    sum = 0
    istr = str(i)
    for ch in istr:
        sum += int(ch)**2
    return sum

def chain(num):
    while True:
        # print(num)
        num = square_digit(num)
        if num == 1:
            return ones.append(1)
        if num == 89:
            return eightynines.append(1)

for i in range(1, 10000000):
    chain(i)

print(len(eightynines))