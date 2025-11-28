import random

list_size = 20
min_value = -100
max_value = 100

numbers = [random.randint(min_value, max_value) for _ in range(list_size)]

min_element = min(numbers)
max_element = max(numbers)

negative_count = 0
positive_count = 0
zero_count = 0

for num in numbers:

    if num < 0:
        negative_count += 1
    elif num > 0:
        positive_count += 1
    else:
        zero_count += 1

print(f"Список: {numbers}")
print(f"Мин число: {min_element}")
print(f"Макс число: {max_element}")
print(f"Количество отрицательных чисел: {negative_count}")
print(f"Количество положительных чисел: {positive_count}")
print(f"Количество нулей: {zero_count}")