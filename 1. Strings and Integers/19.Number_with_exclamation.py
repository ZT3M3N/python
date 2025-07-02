#This function should take a non-negative integer as an input and return the factorial of that number. The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.

def factorial(n: int) -> int:
    # your code here
    if n<2:
        return 1
    else:
        return n*factorial(n-1)


print("Example:")
print(factorial(4))

# These "asserts" are used for self-checking
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(10) == 3628800
assert factorial(15) == 1307674368000

print("The mission is done! Click 'Check Solution' to earn rewards!")
