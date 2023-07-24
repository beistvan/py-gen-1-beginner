def convert_to_python_case(text):
    s = text[0].lower()
    for c in text[1:]:
        if c.isupper():
            s += '_' + c.lower()
        else:
            s += c
    return s

txt = input()

print(convert_to_python_case(txt))
