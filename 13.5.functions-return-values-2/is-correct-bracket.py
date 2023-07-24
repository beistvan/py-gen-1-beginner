def is_correct_bracket(text):
    s = 0
    for c in text:
        if c == '(':
            s += 1
        elif c == ')':
            s -= 1
            if s < 0:
                return False
    return s == 0

txt = input()

print(is_correct_bracket(txt))
