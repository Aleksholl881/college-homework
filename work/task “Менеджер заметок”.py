notes = [
    "идея | придумать сюжет для игры",
    "покупки | купить молоко",
    "учёба | выучить модули в Python",
]

with open('notes.txt', 'w', encoding='utf-8') as file:
    for note in notes:
        file.write(note + '\n')

print("Файл notes.txt успешно создан!")
print(f"Добавлено {len(notes)} заметок.")

def load_notes():
    notes = []
    try:
        with open("notes.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:  # проверяем, что строка не пустая
                    # ИСПРАВЛЕНО: добавлены пробелы вокруг разделителя
                    parts = line.split(" | ", 1)
                    if len(parts) == 2:
                        category = parts[0].strip()
                        text = parts[1].strip()
                        notes.append((category, text))
    except FileNotFoundError:
        print("Файл notes.txt не найден. Будет создан при добавлении первой заметки.")
    except Exception as e:
        print(f"Ошибка при загрузке заметок: {e}")

    return notes


def save_notes(notes):
    try:
        with open("notes.txt", "w", encoding="utf-8") as f:
            for category, text in notes:
                f.write(f"{category} | {text}\n")
    except Exception as e:
        print(f"Ошибка при сохранении заметок: {e}")

def add_note():
    print("\n--- Добавление новой заметки ---")
    category = input("Введите категорию: ").strip()
    text = input("Введите текст заметки: ").strip()

    if not category or not text:
        print("Категория и текст не могут быть пустыми!")
        return

    try:
        with open("notes.txt", "a", encoding="utf-8") as f:
            f.write(f"{category} | {text}\n")
        print("Заметка успешно добавлена!")
    except Exception as e:
        print(f"Ошибка при добавлении заметки: {e}")

def find_by_category(category):
    notes = load_notes()
    if not notes:
        print("Заметок нет или файл пуст.")
        return []

    result = [note for note in notes if note[0].strip().lower() == category.strip().lower()]

    if result:
        print(f"\n--- Заметки в категории '{category}' ---")
        for cat, text in result:
            print(f"• {text}")
    else:
        print(f"Заметок в категории '{category}' не найдено.")

    return result

def search_word(word):
    notes = load_notes()
    if not notes:
        print("Заметок нет или файл пуст.")
        return []

    result = [note for note in notes if word.lower() in note[1].lower()]

    if result:
        print(f"\n--- Заметки, содержащие слово '{word}' ---")
        for cat, text in result:
            print(f"[{cat}] {text}")
    else:
        print(f"Заметок со словом '{word}' не найдено.")

    return result

def show_all_notes():
    notes = load_notes()
    if not notes:
        print("Заметок нет или файл пуст.")
        return

    print("\n Все заметки ")
    for i, (category, text) in enumerate(notes, 1):
        print(f"{i}. [{category}] {text}")

def main():
    while True:

        print("МЕНЕДЖЕР ЗАМЕТОК")
        print("1. Добавить заметку")
        print("2. Показать все заметки")
        print("3. Найти по категории")
        print("4. Поиск по слову")
        print("5. Выход")

        choice = input("\nВыберите действие (1-5): ")

        if choice == "1":
            add_note()

        elif choice == "2":
            show_all_notes()

        elif choice == "3":
            category = input("Введите категорию для поиска: ").strip()
            if category:
                find_by_category(category)
            else:
                print("Категория не может быть пустой!")

        elif choice == "4":
            word = input("Введите слово для поиска: ").strip()
            if word:
                search_word(word)
            else:
                print("Слово для поиска не может быть пустым!")

        elif choice == "5":
            print("Выход из программы. До свидания!")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите от 1 до 5.")

        input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()