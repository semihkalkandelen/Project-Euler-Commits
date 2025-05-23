"""Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""

def fibonacci():
    val1, val2 = 0, 1
    sums = 0
    for i in range(10):
        val1, val2 = val2, val1 + val2
        if val2 %2 ==0:
            sums += val2
    return(sums)

print(fibonacci())