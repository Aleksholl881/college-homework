num = input("Введите целое число: ")

result_str = ""
for digit in num:
    if digit != '3' and digit != '6':
        result_str += digit

if result_str == "" or result_str == "-":
    result = 0
else:
    result = int(result_str)

print(f"Результат: {result}")