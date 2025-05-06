# odd or even check, true if even
def even(x):
    if x % 2 == 0:
        return True
    else:
        return False
    
# collatz function
def collatz(x):
    if even(x):
        x = int(x / 2)
    else:
        x = int(3 * x + 1)
    return x

sequenceMax = 0
num = 0

for i in range(1, 1000000):
    
    run = True
    sequence = []
    counter = i

    # find the collatz sequence for each number
    while run:
        i = collatz(i)
        sequence.append(i)

        if i == 1:
            run = False
    
    if len(sequence) > sequenceMax:
        sequenceMax = len(sequence)
        num = counter

print(num)