v = int(input("Введите скорость:"))
t = int(input("Введите количество часов движения:"))
s = (v * t) % 109
print(s)