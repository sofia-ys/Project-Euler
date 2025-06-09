x = 3
fib = [1, 1]  # base cases
while len(str(fib[-1])) < 1000:
    fib.append(fib[x-2] + fib[x-3])  # accounting for indexing from 0
    x += 1

print(len(fib))