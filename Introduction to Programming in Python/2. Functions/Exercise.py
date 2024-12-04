#2. Compose a function odd() that takes three bool arguments and returns True if an odd number of arguments are True, and False otherwise.
def odd(a: bool, b: bool, c: bool):
    return (a+b+c) % 2 != 0

print(odd(True, True, False)) 

#3. Compose a function majority() that takes three bool arguments and returns True if at least two of the arguments are True, and False 
# otherwise. Do not use an if statement.
def majority(a: bool, b: bool, c: bool):
    return not (a + b + c) <= 1
print(majority(False, False, False)) 

#4. Compose a function areTriangular() that takes three numbers as arguments and returns True if they could be the sides of a triangle 
# (none of them is greater than or equal to the sum of the other two), and False otherwise.
def areTriangular(a: int, b: int, c: int) -> bool:
    return a >= 0 and b >= 0 and c >= 0 and a < b + c and b < a + c and c < a + b

print(areTriangular(0, 3, 2))  

#7. Compose a function lg() that takes an integer n as an argument and returns the largest integer not larger than the base-2 
# logarithm of n. Do not use the standard Python math module.
def lg(n: int) -> int:
    x = 0
    while 2 ** x <= n:
        x += 1
    return x - 1
print(lg(20))

#12. The following checksum formula is widely used by banks and credit card companies to validate legal account numbers:
#d0 + f(d1) + d2 + f(d3) + d4 + f(d5) + d6 + ... = 0 (mod 10)
# For example, 17327 is valid because 1 + 5 + 3 + 4 + 7 = 20, which is a multiple of 10.
def checksum(n: int) -> int:
    



    