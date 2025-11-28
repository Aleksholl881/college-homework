import webbrowser
import time
def main():
    products = {
        "Телефон": frozenset({"техника", "электроника"}),
        "Самурайский меч": frozenset({"редкое", "оружие"}),
        "Холодильник": frozenset({"техника", "бытовое"}),
        "Ноутбук": frozenset({"техника", "электроника"}),
        "Золотое кольцо": frozenset({"редкое", "украшение"})
    }

    def find_by_category(category):
        result = set()
        for product, categories in products.items():
            if category in categories:
                result.add(product)
        return result

    while True:
        print("1. Добавить товар")
        print("2. Вывести все товары")
        print("3. Найти товары по категории")
        print("4. Выйти")

        choice = input("Выберите действие (1-4): ").strip()

        if choice == "1":
            product_name = input("Введите название товара: ").strip()

            if product_name in products:
                print("Ошибка: товар с таким названием уже существует!")
                continue

            categories_input = input("Введите категории через запятую: ").strip()
            categories_list = [cat.strip() for cat in categories_input.split(",") if cat.strip()]

            if not categories_list:
                print("нужно указать хотя бы одну категорию!")
                continue

            products[product_name] = frozenset(categories_list)
            print(f"Товар '{product_name}' успешно добавлен!")

        elif choice == "2":
            if not products:
                print("Список товаров пуст!")
                continue

            sorted_products = sorted(products.items(), key=lambda item: len(item[0]))

            for product, categories in sorted_products:
                categories_str = ", ".join(sorted(categories))
                print(f"• {product}: {categories_str}")

        elif choice == "3":
            category = input("Введите категорию для поиска: ").strip().lower()

            if not category:
                print("Ошибка: категория не может быть пустой!")
                continue

            found_products = find_by_category(category)

            if found_products:
                print(f"\nТовары в категории '{category}':")
                print("-" * 40)

                sorted_found = sorted(found_products, key=lambda product: len(product))

                for product in sorted_found:
                    print(f"• {product}")
            else:
                print(f"Товары в категории '{category}' не найдены.")

        elif choice == "4":
            print("До свидания!")
            break

        else:
            print("ты идиот? неумеешь писать цифры? ладно держи видос.")
            time.sleep(3)
            url = "https://youtu.be/vBqCrs3_kiA?si=F1gmk7xOvNX19B9f"
            webbrowser.open(url)

def demonstrate_lambda_sorting():

    sample_products = {
        "Телефон": frozenset({"техника", "электроника"}),
        "Меч": frozenset({"редкое", "оружие"}),
        "Холодильник": frozenset({"техника", "бытовое"}),
        "Ноутбук": frozenset({"техника", "электроника"})
    }

    sorted_by_length = sorted(sample_products.items(), key=lambda item: len(item[0]))
    print("1. По длине названия:")
    for product, _ in sorted_by_length:
        print(f"   {product} ({len(product)} символов)")
print(demonstrate_lambda_sorting())


if __name__ == "__main__":
    main()