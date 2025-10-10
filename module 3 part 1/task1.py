number_one = int(input("ведите начальное число диапозона: "))
number_two = int(input("ведите конечное число диапозона: "))
for i in range(number_one, number_two):
    if i % 7 == 0:
        print(f"число {i} кратно 7")

