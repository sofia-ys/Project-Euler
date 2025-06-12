def pandigital(n):
    n = str(n)
    condition = "1" in n and "2" in n and "3" in n and "4" in n and "5" in n and "6" in n and "7" in n and "8" in n and "9" in n
    return condition

def isvalid(a, b):
    product = a * b
    string = str(product) + str(a) + str(b)
    return (len(string) == 9)

pandigits = set()
for i in range(1000):
    for j in range(i, 9000):  # avoiding duplicates by starting j at the i value
        if isvalid(i, j):
            product = i * j
            digit = str(product) + str(i) + str(j) 

            if pandigital(digit):
                pandigits.add(product)

print(sum(pandigits))