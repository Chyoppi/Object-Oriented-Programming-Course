"""Task 4, Please write a function named factorials(n: int), 
which returns the factorials of the numbers 1 to n in a dictionary. 
The number is the key, and the factorial of that number is the value mapped to it.
"""

def factorials(n: int):
    fact = [1] * (n + 1)
    for x in range(2, n + 1):
        fact[x] = fact[x - 1] * x
    return fact


#Making sure the function works correctly
k = factorials(5)
print(k[1])
print(k[3])
print(k[5])