"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 475143?"""

def primefactor():
    num = 475143
    val = 1
    for i in range(1, (num//2)+1):
        if num % i == 0 and i >= val:
            val = i
    return val        

print(primefactor())

