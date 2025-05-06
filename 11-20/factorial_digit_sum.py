from math import factorial as f

number = f(100)  # getting the factorial 
str = str(number)
sum = 0

for ch in str:  # iterating through each number in the factorial of 100
    sum += int(ch)

print(sum)