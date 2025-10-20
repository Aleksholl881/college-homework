count = 0

for num in range(100, 10000):
    a = num // 100
    b = (num // 10) % 10
    c = num % 10

    if a != b and a != c and b != c:
        count += 1

print(f"Количество чисел с без одинаковых цифр: {count}")