#Let's teach the Robots to distinguish words and numbers.

#You are given a string with words and numbers separated by whitespaces (one space). The words contain only letters. You should check if the string contains three words in succession. For example, the string "start 5 one two three 7 end" contains three words in succession.

def checkio(words: str) -> bool:
    # add your code here
    count = 0
    for w in words.split():
        if w.isalpha():
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False

print("Example:")
print(checkio("Hello World hello"))

# These "asserts" are used for self-checking
assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True
assert checkio("Hi") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
