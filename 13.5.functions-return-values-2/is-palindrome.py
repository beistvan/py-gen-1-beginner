def is_palindrome(text):
    txt = list(i for i in text.upper() if i not in '.,!?- ')
    return txt == txt[::-1]

txt = input()

print(is_palindrome(txt))
