start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))
primes = []

for num in range(start, end + 1):
    if num < 2:
        continue

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(num)

print("Найдены следующие простые числа:")
for prime in primes:
    print(prime, end=" ")