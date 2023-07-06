a, b, c = input()
a, b, c = int(a), int(b), int(c)
print("Number is not interesting" if  max(a, b, c) - min(a, b, c) == sum([a, b, c]) - max(a, b, c) - min(a, b, c) else "Number is interesting")
