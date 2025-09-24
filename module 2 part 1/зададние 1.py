first_number = int(input())
second_number = int(input())
third_number = int(input())
operation = input("Выберите операцию (сумма/произведение): ")
if operation == "сумма":
    print(second_number + third_number + first_number)
elif operation == "произведение":
    print(second_number * third_number * first_number)