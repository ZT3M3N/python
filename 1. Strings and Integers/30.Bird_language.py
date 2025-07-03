#Stephan has a friend who happens to be a little mechbird. Recently, he was trying to teach it how to speak basic language. Today the bird spoke its first word: "hieeelalaooo". This sounds a lot like "hello", but with too many vowels. Stephan asked Nikola for help and he helped to examine how the bird changes words. With the information they discovered, we should help them to make a translation module.

#The bird converts words by two rules:
#   - after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
#   - after each vowel letter the bird appends two of the same letter (a ⇒ aaa);
#   Vowels letters == "aeiouy".

def translation(text: str) -> str:
    letters = "aeiouy"
    new = ""
    index = 0
    while index < len(text):
        if text[index] == " ":
            new += text[index]
        elif text[index] not in letters and text[index+1] in letters:
            new += text[index]
            index +=1
        elif text[index] in letters:
            if text[index:index+3] == text[index] * 3:
                new += text[index]
                index += 2
        index += 1    
    return new


print("Example:")
print(translation("hieeelalaooo"))

# These "asserts" are used for self-checking
assert translation("hieeelalaooo") == "hello"
assert translation("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translation("aaa bo cy da eee fe") == "a b c d e f"
assert translation("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")
