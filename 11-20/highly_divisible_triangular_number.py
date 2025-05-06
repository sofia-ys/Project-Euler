import math as m

# initialising
triangular = [0]
status = True
i = 0
num = 5

def divisors(x):
    div = []
    for j in range(1, int(m.sqrt(x)) + 1):  # divisors come in pairs so we only have to check up to the square root
        if x % j == 0:
            div.append(j)
    return 2 * len(div)  # just multiply by 2 to account for the pair


while status:
    i = i + 1  # counter
    triangular.append(triangular[i - 1] + i)  # calculate each triangular number

    if divisors(triangular[i]) > 500:  # check if it has more than 500 divisors
        status = False

print(triangular[i])