first_number = int(input())
second_number = int(input())
third_number = int(input())
operation = input("для выбора числа напишите (минимум/максимум/среднее):")
if operation == "минимум":
    result = min(first_number, second_number, third_number)
    print(result)
elif operation == "максимум":
    result = max(first_number, second_number, third_number)
    print(result)
elif operation == "среднее":
    result = (first_number + second_number + third_number) / 3
    print(result)