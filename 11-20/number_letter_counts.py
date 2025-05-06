from num2words import num2words as n2w

target = 1000 + 1  # our target number + 1 because indexing <3
lst = []
for i in range(1, target):  # creating our list of numbers from 1 to target
    lst.append(i)

sum = 0

for num in lst:  # for each number in the list
    str = n2w(num)  # we convert it to a string so we can go character by character
    for ch in str:
        if ch.isalpha():  # if the character is a letter
            sum += 1  # we add one to the sum

print(sum)