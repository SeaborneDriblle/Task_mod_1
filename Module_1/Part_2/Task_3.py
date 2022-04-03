p =input("Введите пароль: ")
while len(p) <= 8 or p.islower() or p.isupper():
    print("Введите корректный пароль")
    p =input("Введите пароль: ")
else: 
    print("Пароль принят")
