# initialising
fib = [1]  # fibonacci sequence
i = 0  # counter
sum = 0  # sum
status = True  # while loop controller


while status:
    fib.append(fib[i] + fib[i-1])  # compute next number in fibonacci sequence
    if fib[i] % 2 == 0:  # check if even 
        sum = sum + fib[i]  # if even, add it to the sum
    i = i + 1  # adjust counter for next loop
    if fib[i] > 4000000:  # check if loop should break
        status = False

print(sum)