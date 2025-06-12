import math

# getting the divisors of a number
def divisors(n):
    divisors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(int(n/i))
    return divisors

# finding the gcd of two numbers
def reduce(a, b):
    # finding gcd
    if a == 0 or b == 0:
        return 0, 0
    diva = divisors(a)
    divb = divisors(b)
    common = diva.intersection(divb)
    gcd = max(common)
    return int(a/gcd), int(b/gcd)  # returning a and b in their reduced form

# checking if they cancel lol
def cancel(a, b):
    ar, br = reduce(a, b)
    astr, bstr = str(a), str(b)  # getting strings of our inputs
    for i in range(2):
        for j in range(2):
            if astr[i] == bstr[j] and astr[i] != "0":  # no trivial case
                anew = astr[-i + 1] 
                bnew = bstr[-j + 1] 
                afin, bfin = reduce(int(anew), int(bnew))
                return (afin == ar and bfin == br)
    return False

digcancel = []
for num in range(10, 100):
    for denom in range(num + 1, 100):
        if cancel(num, denom):
            digcancel.append((num, denom))


nlst = []
dlst = []
for n, d in digcancel:
    nlst.append(n)
    dlst.append(d)

totn = math.prod(nlst)
totd = math.prod(dlst)

lown, lowd = reduce(totn, totd)
print(lowd)