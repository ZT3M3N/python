#This is an intro mission, the purpose of which is to explain how to solve missions on CheckiO. If you want to know how to get the maximum out of using CheckiO, check out our blog post "From Basic to Advance usage".

#This mission is the easiest one. Write a function that will receive 2 numbers as input and it should return the multiplication of these 2 numbers.

#----------------------------------------------------------------------------------------------------------------------------------------#

def mult_two(a: int, b: int) -> int:
    # your code here
    return a * b


print("Example")
print(mult_two(1, 2))

assert mult_two(3, 2) == 6
assert mult_two(0, 1) == 0

print("The first mission is done! Click 'Check' to earn cool rewards!")
