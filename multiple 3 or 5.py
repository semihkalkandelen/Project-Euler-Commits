""" we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3 5 6 9 and . The sum of these multiples is 23
Find the sum of all the multiples of 3 or 5 below 1000."""

"""
def multiple3or5():
    point = 0
    for i in range(1,1000):
        if i % 3 == 0 or i % 5 == 0:
            point +=i
    return point

print(multiple3or5())

"""

val = sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1, 10)))
print(val)
