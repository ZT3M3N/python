#Identify whether a given integer is positive, negative, or zero and return a respective string: "positive", "negative" or "zero".

#----------------------------------------------------------------------------------------------------------------------------------------#

def determine_sign(num: int) -> str:
    # your code here
    if (num < 0):
        return "negative"
    elif(num == 0):
        return "zero"
    else:
        return "positive"


print("Example:")
print(determine_sign(11))

# These "asserts" are used for self-checking
assert determine_sign(5) == "positive"
assert determine_sign(0) == "zero"
assert determine_sign(-10) == "negative"
assert determine_sign(1) == "positive"
assert determine_sign(-1) == "negative"
assert determine_sign(999) == "positive"
assert determine_sign(-1000) == "negative"
assert determine_sign(123456789) == "positive"
assert determine_sign(-987654321) == "negative"
assert determine_sign(2) == "positive"

print("The mission is done! Click 'Check Solution' to earn rewards!")
