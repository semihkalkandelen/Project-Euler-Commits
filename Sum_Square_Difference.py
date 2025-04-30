"""The sum of the squares of the first ten natural numbers is,

1² +2²+...+10² = 385.

The square of the sum of the first ten natural numbers is,

(1+2+...+10)² = 55² = 3025.

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385 = 2640.

Find the difference between the sum of the squares of the first twenty natural numbers and the square of the sum."""


def first20():
    mydict = dict()
    for j in range(20):
        sumofsquare = 0
        squareofsum = 0
        for i in range(j+1):
            sumofsquare += i
            squareofsum += i**2
        sumofsquare = sumofsquare**2    
        answer = sumofsquare - squareofsum
        mydict[j] = answer
    return mydict

print(first20())