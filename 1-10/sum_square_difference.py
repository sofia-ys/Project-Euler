# initialising
sumSqr = 0
sqrSum = 0
num = 100

for i in range(num + 1):
    sumSqr = sumSqr + i**2  # computing sum of squares
    sqrSum = sqrSum + i  # finding sum

sqrSum = sqrSum**2  # now finding square of sums

dif = sqrSum - sumSqr  # difference between sum of squares and square of sum
print(dif)