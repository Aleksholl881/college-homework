total = 0
count = 0
maximum = None
minimum = None

while True:
    number = float(input("Введите число: "))

    if number == 7:
            print("Good bye!")
            break

    total += number
    count += 1

    if maximum is None or number > maximum:
            maximum = number
    if minimum is None or number < minimum:
            minimum = number

print(f"Сумма чисел: {total}")
print(f"Максимальное число: {maximum}")
print(f"Минимальное число: {minimum}")