n = int(input())
print(f"Sum of digits = {n // 100 + n % 100 // 10 + n % 10}")
print(f"Product of digits = {n // 100 * (n % 100 // 10) * (n % 10)}")
