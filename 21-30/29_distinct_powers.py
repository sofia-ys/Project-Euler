
terms = set()  # ensuring distinct numebrs
for a in range(2, 101):
    for b in range(2, 101):
        terms.add(a**b)

print(len(terms))