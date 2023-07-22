# function declaration
def draw_triangle(fill, base):
    for j in range(1, base // 2 + 2):
        print(fill * j)
    for j in range(base // 2, 0, -1):
        print(fill * j)

# reading data
fill = input()
base = int(input())

# function call
draw_triangle(fill, base)
