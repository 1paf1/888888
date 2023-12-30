# hello

# Зчитуємо три цифри від користувача
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))

# Вибір операції від користувача
operation = input("Виберіть операцію (max, min, avg): ")

# Обчислення та виведення результату
if operation == "max":
    result = max(num1, num2, num3)
    print(f"Максимум: {result}")
elif operation == "min":
    result = min(num1, num2, num3)
    print(f"Мінімум: {result}")
elif operation == "avg":
    result = (num1 + num2 + num3) / 3
    print(f"Середнє арифметичне: {result}")
else:
    print("Невірна операція. Будь ласка, виберіть 'max', 'min' або 'avg'.")
