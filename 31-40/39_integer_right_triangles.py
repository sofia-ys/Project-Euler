import math

def perimeter(p):
    solutions = set()
    for a in range(1, p//2):
        for b in range(1, (p-a)//2):
            c = math.sqrt(a**2 + b**2)
            if (a + b + c) == p:
                solutions.add(tuple(sorted((a, b, c))))  # avoiding duplicate tuples
    return solutions

triangles = []
for p in range(1, 1001):
    triangles.append(len(perimeter(p)))

print(triangles.index(max(triangles)) + 1)  # + 1 because index from 0