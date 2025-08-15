import random as rnd

stay_win = 0
switch_win = 0

for i in range(1000000):
    doors = ["goat", "goat", "car"]
    choices = [0, 1, 2]

    rnd.shuffle(doors)
    choice = rnd.choice(choices)
    choices.pop(choice)
    show = rnd.choice(choices)
    
    if doors[show] == "goat":
        for el in choices:
            if el != show:
                switch = el
    else:
        switch = show

    if doors[choice] == "car":
        stay_win += 1
    elif doors[switch] == "car":
        switch_win += 1

print(f"Stay: {stay_win/10000:.2f}%")
print(f"Switch: {switch_win/10000:.2f}%")