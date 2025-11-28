products = {
    "Фрукты": [("Яблоки", 15, 60), ("Бананы", 10, 80)],
    "Овощи": [("Морковь", 20, 30),("картошка",30,45)]
}

for category, items in products.items():
    print(f"{category}:")
    for item in items:
        name, quantity, price = item
        print(f"  {name} — {quantity} шт., {price} руб.")
    print()

most_expensive = None
max_price = 0

for category, items in products.items():
    for item in items:
        name, quantity, price = item
        if price > max_price:
            max_price = price
            most_expensive = (name, quantity, price)
print(f"самый дорогой товар: {most_expensive}")

for category, items in products.items():
    for item in items:
        name, quantity, price = item
        max_price = quantity*price

max_category = None
max_total = 0

for category, items in products.items():
    total_quantity = sum(quantity for _, quantity, _ in items)
    if total_quantity > max_total:
        max_total = total_quantity
        max_category = category

print(f"общая сумма товаров: {max_price}")
print(f"больше вего товаров в: {max_category}")
