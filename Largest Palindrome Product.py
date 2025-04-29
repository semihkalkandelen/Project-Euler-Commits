"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009= 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

#highest 3 digit number is 999. so the answer has to be lesser than 999*999 = 998001

def highestpalindrome():
    highest = 998001
    while True:
        highest -= 1
        if str(highest) == str(highest)[::-1]:
            break
    return highest

print(highestpalindrome())
