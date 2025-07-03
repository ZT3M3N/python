# Given two strings and a permissible number of character differences, determine if the strings can be considered approximately equal.

def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
    # your code here
    for i in range(max(len(str1), len(str2))):
        try:
            if str1[i] != str2[i]: threshold -= 1
        except IndexError:
            threshold -= 1
    
    return threshold >=0


print("Example:")
print(fuzzy_string_match("apple", "appel", 2))

# These "asserts" are used for self-checking
assert fuzzy_string_match("apple", "appel", 2) == True
assert fuzzy_string_match("apple", "bpple", 1) == True
assert fuzzy_string_match("apple", "bpple", 0) == False
assert fuzzy_string_match("apple", "apples", 1) == True
assert fuzzy_string_match("apple", "bpples", 2) == True
assert fuzzy_string_match("apple", "apxle", 1) == True
assert fuzzy_string_match("apple", "pxxli", 3) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
