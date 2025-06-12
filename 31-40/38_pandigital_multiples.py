def pandigital(n):
    condition2 = len(n) == 9
    condition1 = "1" in n and "2" in n and "3" in n and "4" in n and "5" in n and "6" in n and "7" in n and "8" in n and "9" in n
    return (condition1 and condition2)

concat_list = set()
i = 1
while True:

    for k in range(1, 10000):
        concat = ""
        for j in range(1, i):
            product = k * j
            concat += str(product)

        if pandigital(concat):
            concat_list.add(int(concat))
        
        if len(concat) > 9:
            break

    i += 1

    if len(concat) >= 9:
        break

print(max(concat_list))