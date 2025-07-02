#1. Let's make our function func from the previous mission more useful. Let it take an argument arg inside brackets. If you have any trouble, see the hints below the description.

#2. Return the argument value without any changes using keyword return.

#----------------------------------------------------------------------------------------------------------------------------------------#

# Taken from mission Empty Function

# 1. Define a function without arguments
# write your code here
def func():
    pass
    
# 2. Fill the function body with placeholder
# write your code here
pass


# 1. In the above function add argument 'arg' inside brackets.
# 2. Return the same argument using keyword 'return'.
def func(arg):
    return arg

print("Example:")
print(func(3))

# These "asserts" are used for self-checking
assert func(3) == 3
assert func("string") == "string"
assert func(True) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
