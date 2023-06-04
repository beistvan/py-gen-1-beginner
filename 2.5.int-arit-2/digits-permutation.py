n = int(input())
a, b, c = n // 100, n % 100 // 10, n % 10
print(f"{a}{b}{c}\n{a}{c}{b}\n{b}{a}{c}\n{b}{c}{a}\n{c}{a}{b}\n{c}{b}{a}")