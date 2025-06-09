from math import factorial as f

gridsize = 20
# the number of moves is essentially how many combinations we can get from 2*n total moves (n right, n down) taking n at a time
# how many ways can you choose positions for 3 rights (or 3 downs) in a 6 move sequence?
# aka, which 3 of the total 6 moves are right? (the rest is just down)
# nCr = n! / (r! (n-r)!)
moves = int(f(2 * gridsize) / (f(gridsize) * f(2 * gridsize - gridsize)))

print(moves)