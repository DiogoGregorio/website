def invert_and_check_palindrome(word: str):
    if word is None:
        return "NULL ERROR"
    
    clean = word.strip()
    if not clean:
        return "empty word"
    
    reversed_word = clean[::-1]
    
    if clean.lower() == reversed_word.lower():
        palindrome_status = "It is a palindrome"
    else:
        palindrome_status = "It is NOT a palindrome"
    
    return reversed_word, palindrome_status

word = input("word: ")

output = invert_and_check_palindrome(word)

print(output)