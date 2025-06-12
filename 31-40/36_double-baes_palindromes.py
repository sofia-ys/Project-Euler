def palindrome(n):
    for i in range(len(str(n))//2):
        if str(n)[i] != str(n)[-i -1]:
            return False
    return True

pal_bin = []
for i in range(1, 1000000):
    # if number in base 10 (i) and number in binary (without leading b0)
    if palindrome(i) and palindrome(int(str(bin(i))[2:])):
        pal_bin.append(i)

print(sum(pal_bin))