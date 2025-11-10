text = input("введите предложения:")

count = 0
for char in text:
    if char in '.!?':
        count += 1

print(f"Количество предложений в тексте: {count}")