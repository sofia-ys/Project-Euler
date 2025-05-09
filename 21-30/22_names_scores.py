with open("21-30\\0022_names.txt", "r") as fin:
    for line in fin:
        names = line.replace('"', "").split(",")  # making our list of names with the "" and each entry is after the comma 

names = sorted(names)  # putting it in alphabetical order
totScore = 0  # initialising total score

for idx, name in enumerate(names):  # for each name in the list of names, and we also take its index 
    value = 0  # resetting the value for each name
    for ch in name:
        value += ord(ch) - ord("A") + 1  # finding the "value" of each character in the name, using the ord("A") +1 to normalise ascii
    totScore += value * (idx + 1)  # adding the score of the name to the total score, idx + 1 because it counts from 0

print(totScore)