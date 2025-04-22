# initialising
triangular = [1]
status = True
i = 0

while status:
    i = i + 1  # counter
    triangular.append(triangular[i - 1] + i)

    if i > 10:
        status = False

print(triangular)