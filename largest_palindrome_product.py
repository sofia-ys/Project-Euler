# initialising 
product = 0
palindromeStatus = False
palindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j  # calculating the product of each three digit number
        productStr = str(product)  # turning into a string to compare each digit
        for k in range(int(len(productStr)/2)):  
            if productStr[k] == productStr[-(k+1)]:  # checking if the first integer is the same as the last and so on
                palindromeStatus = True
            else:
                palindromeStatus = False  # if any integer is not equal to its equivalent on the opposite side, it is not a palindrome
                break
        if palindromeStatus == True:
            if product > palindrome:  # only store if the palindrome is larger than any previous ones
                palindrome = product

print(palindrome)