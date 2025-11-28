number_a = int(input("введите число: "))
operation = input("введите операцию(+, -, *, /,): ")
number_b = int(input("введите число: "))
if operation == "+":
    result = number_a + number_b
    print(f"{number_a} + {number_b} = {result}")

elif operation == "-":
    result = number_a - number_b
    print(f"{number_a} - {number_b} = {result}")

elif operation == "*":
    result = number_a * number_b
    print(f"{number_a} * {number_b} = {result}")

elif operation == "/":
    result = number_a / number_b
    print(f"{number_a} / {number_b} = {result}")
else:
    print("ошибка")