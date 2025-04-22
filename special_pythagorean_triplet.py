# initialising
sum = 12
done = False
pythag = ()

for a in range(1, sum - 1):  # a < b
    for b in range(a + 1, sum):  # b < c
        for c in range(b + 1, sum + 1):  # largest number can at most be the sum
            if a**2 + b**2 < c**2:
                break

            if a**2 + b**2 == c**2:
                pythag = (a, b, c)

                if a + b + c == sum:
                    done = True
                    break
        
        if a + b + c > sum:
            break

        if done == True:
            break
    
    if a + b + c > sum:
        break

    if done == True:
        break

print(pythag)