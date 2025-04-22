sum = 0  # initialising
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:  # check if number is a multiple of 3 or 5
        sum = sum + i  # if it is, add it to the sum

print(sum)