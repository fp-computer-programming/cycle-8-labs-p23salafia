def is_palindrome(word):
    word += 1
    while word != (word)[::-1]:
        word += 1
    return word

print(is_palindrome("green"))