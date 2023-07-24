from sympy import nextprime

def get_next_prime(num):
    return nextprime(num)

n = int(input())

print(get_next_prime(n))
