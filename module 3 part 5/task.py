
def print_figure_a(size=5):
    for i in range(size):
        print('*' * size)

def print_figure_b(size=5):
    for i in range(1, size + 1):
        print('*' * i)

def print_figure_c(size=5):
    for i in range(1, size + 1):
        print(' ' * (size - i) + '*' * i)

def print_figure_d(size=5):
    for i in range(1, size + 1):
        spaces = ' ' * (size - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

def print_figure_e(size=5):
    # Верхняя часть
    for i in range(1, size + 1):
        spaces = ' ' * (size - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)
    # Нижняя часть
    for i in range(size - 1, 0, -1):
        spaces = ' ' * (size - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

def print_figure_f(size=5):
    """Песочные часы"""
    # Верхняя часть
    for i in range(size, 0, -1):
        spaces = ' ' * (size - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)
    # Нижняя часть
    for i in range(2, size + 1):
        spaces = ' ' * (size - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

def print_figure_g(size=5):
    """Крест"""
    mid = size // 2
    for i in range(size):
        if i == mid:
            print('*' * size)
        else:
            spaces = ' ' * mid
            print(spaces + '*' + spaces)

def print_figure_h(size=5):
    """Плюс"""
    mid = size // 2
    for i in range(size):
        if i == mid:
            print('*' * size)
        else:
            spaces = ' ' * mid
            print(spaces + '*' + spaces)

def print_figure_i(size=5):
    """Квадрат с пустотой"""
    for i in range(size):
        if i == 0 or i == size - 1:
            print('*' * size)
        else:
            print('*' + ' ' * (size - 2) + '*')

def print_figure_j(size=5):
    """Стрелка вправо"""
    mid = size // 2
    for i in range(size):
        if i < mid:
            print('*' * (i + 1))
        elif i == mid:
            print('*' * size)
        else:
            print('*' * (size - i))
def show_menu():
    """Показать меню с фигурами"""
    print("\n" + "="*50)
    print("ВЫВОД ФИГУР ИЗ ЗВЕЗДОЧЕК")
    print("="*50)
    print("a - Прямоугольник")
    print("б - Прямоугольный треугольник слева")
    print("в - Прямоугольный треугольник справа")
    print("г - Равнобедренный треугольник")
    print("д - Ромб")
    print("e - Песочные часы")
    print("ж - Крест")
    print("з - Плюс")
    print("и - Квадрат с пустотой")
    print("к - Стрелка вправо")
    print("0 - Выход")
    print("="*50)

def main():
    """Основная функция программы"""
    figures = {
        'а': print_figure_a,
        'б': print_figure_b,
        'в': print_figure_c,
        'г': print_figure_d,
        'д': print_figure_e,
        'е': print_figure_f,
        'ж': print_figure_g,
        'з': print_figure_h,
        'и': print_figure_i,
        'к': print_figure_j
    }

    while True:
        show_menu()
        choice = input("Выберите фигуру (a-к) или 0 для выхода: ")

        if choice == '0':
            print("До свидания!")
            break

        if choice in figures:
            try:
                size = int(input("Введите размер фигуры (по умолчанию 5): ") or "5")
                if size < 1:
                    print("Размер должен быть положительным числом!")
                    continue

                print(f"\nФигура '{choice}':")
                figures[choice](size)

            except ValueError:
                print("Пожалуйста, введите корректное число!")
        else:
            print("Неверный выбор! Пожалуйста, выберите фигуру из меню.")

if __name__ == "__main__":
    main()
root.mainloop()