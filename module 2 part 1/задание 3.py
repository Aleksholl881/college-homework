metr = int(input("введите количество метров: "))
operation = input("ведите что вам нужно(мили/дюймы/ярды): ")
if operation == "мили":
    result = metr / 1609.344
    print(result)
elif operation == "дюймы":
    result = metr * 39.36
    print(result)
elif operation == "ярды":
    result = metr /  0.9144
    print(result)
else:
    print("вы ввели слово неправильно")