x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))
max = int(x > y) * x + int(x <= y) * y
print(max)