def is_palindrom(word):
    reverse_word = word[::-1]
    return reverse_word == word

print(is_palindrom(("Madam").lower()))