x = int(input("Введите число x: "))
y = int(input("Введите степень y: "))

result = 1

if y >= 0:
    for i in range(y):
        result *= x
else:
    for i in range(-y):
        result *= x
    result = 1 / result

print(f"{x} в степени {y} = {result}")
