
n = 1
dfrac = ""
while len(dfrac) < 1000000:
    dfrac += str(n)
    n += 1

product = 1
for i in range(7):  # up to 1e6
    # print(10**i - 1)
    product *= int(dfrac[10**i - 1])

print(product)