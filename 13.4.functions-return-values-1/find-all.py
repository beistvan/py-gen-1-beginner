def find_all(target, symbol):
    s = []
    for i in range(len(target)):
        if target[i] == symbol:
            s.append(i)
    return s

s = input()
char = input()

print(find_all(s, char))
