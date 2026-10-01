numbers = [10, 2, 56]

total = 0

for num in numbers:
    if isinstance(num, int):
        num = abs(num)

        while num > 0:
            digit = num % 10
            total += digit
            num = num // 10

print(total)
