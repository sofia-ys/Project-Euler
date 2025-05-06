# initialising
sum = 1000
status = True

while status:
    for a in range(1, sum -1):
        for b in range(a+1, sum):
            c = sum - a - b  # we already know a + b + c = 1000 so we can test only possible values of c
            if a**2 + b**2 == c**2:  # checking if this is a pythagorean triplet
                status = False  # if this is we can stop the while loop
                product = a * b * c

print(product)