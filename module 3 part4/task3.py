start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))
for a in range(start, end + 1):
    for b in range(1,11):
        result = a * b
        print(f"{a} × {b} = {result}")