def longest_word(sentence: str) -> str:
    words = sentence.split()
    longest = words[0]
    
    for word in words[1:]:
        if len(word) > len(longest):
            longest = word
        else:
            return ""
            
    return longest

print(longest_word(""))