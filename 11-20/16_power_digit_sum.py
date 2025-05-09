number = str(2**1000)  # get the number as a string so we can iterate through the parts of it
sum = 0

for ch in number:  # for each character (which is a number) in the string 
    sum += int(ch)  # just add its value as an integer to our sum

print(sum)