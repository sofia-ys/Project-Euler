fifth_sums = set()  # no repeats
i = 2  # not starting from 1

while True:
    digsum = 0
    for digit in str(i):
        digsum += int(digit)**5
    if digsum == i:
        fifth_sums.add(i)

    i += 1

    if i > 10e5:
        break

print(fifth_sums)
print(sum(fifth_sums))
