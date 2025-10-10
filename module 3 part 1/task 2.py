number_one = int(input("ведите начальное число диапозона: "))
number_two = int(input("ведите конечное число диапозона: "))

print("1. все числа диапозона:")
for number in range(number_one, number_two+1):
    print(number, end=" ")

print("\n\n2. Все числа диапазона в убывающем порядке:")
for revers_number in range(number_two, number_one-1, -1):
    print(revers_number, end=" ")

print("\n\n3. Все числа диапазона кратные 7:")
for multiples7 in range(number_one, number_two):
    if multiples7 % 7 == 0:
        print(multiples7, end=" ")
print("\n\n4.количество чисел кратных 5:")
count_5 = 0
for multiples5 in range(number_one, number_two):
    if multiples5 % 5 == 0:
        count_5 += 1
        print(multiples5, end=" ")