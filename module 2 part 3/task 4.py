manager1 = int(input("введите продажи менеджера: "))
manager2 = int(input("введите продажи менеджера: "))
manager3 = int(input("введите продажи менеджера: "))
base_salary = 200

if manager1 < 500:
    salary1 = base_salary + manager1 * 0.03
elif manager1 < 1000:
    salary1 = base_salary + manager1 * 0.05
else:
    salary1 = base_salary + manager1 * 0.08

if manager2 < 500:
    salary2 = base_salary + manager2 * 0.03
elif manager2 < 1000:
    salary2 = base_salary + manager2 * 0.05
else:
    salary2 = base_salary + manager2 * 0.08

if manager3 < 500:
    salary3 = base_salary + manager3 * 0.03
elif manager3 < 1000:
    salary3 = base_salary + manager3 * 0.05
else:
    salary3 = base_salary + manager3 * 0.08

best_saler = max(manager1, manager2, manager3)

if best_saler == manager1:
    print(f"\nМенеджер 1:")
    print(f"Продажи: {manager1}")
    print(f"Зарплата: {salary1+200}")
    print("Лучший менеджер")
else:
    print(f"\nМенеджер 1:")
    print(f"Продажи: {manager1}")
    print(f"Зарплата: {salary1}")

if best_saler == manager2:
    print(f"\nМенеджер 2:")
    print(f"Продажи: {manager2}")
    print(f"Зарплата: {salary2+200}")
    print("Лучший менеджер")
else:
    print(f"\nМенеджер 2:")
    print(f"Продажи: {manager2}")
    print(f"Зарплата: {salary2}")

if best_saler == manager3:
    print(f"\nМенеджер 3:")
    print(f"Продажи: {manager3}")
    print(f"Зарплата: {salary3+200}")
    print("Лучший менеджер")
else:
    print(f"\nМенеджер 3:")
    print(f"Продажи: {manager3}")
    print(f"Зарплата: {salary3}")