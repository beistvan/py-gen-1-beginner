# function declaration
def print_digit_sum(num):
    print(sum(int(i) for i in str(num)))

# read data
n = int(input())

# function call
print_digit_sum(n)
