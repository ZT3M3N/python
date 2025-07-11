#In a given string you need to check if one symbol goes right after another. If so - return True, otherwise - False.

#If one of the symbols is not in the given word - your function should return False. If two seeking symbols are the same - your function should return False.

def goes_after(word: str, first: str, second: str) -> bool:
    word = word.lower()
    # your code here
    if(-1 < word.find(first + second)):
        return True
    else:
        return False


print("Example:")
print(goes_after("world", "w", "o"))

# These "asserts" are used for self-checking
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
