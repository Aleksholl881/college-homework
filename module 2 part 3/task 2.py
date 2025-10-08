number = int(input("Введите число: "))
degree = int(input("Введите степень от 0 до 7: "))
if degree < 0 or degree > 7:
    print("ошибка")
else:
    print(number**degree)
