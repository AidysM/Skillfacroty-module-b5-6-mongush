print("Игра крестики и нолики")
print("  0 1 2 - ось x")
for i in range(3):
    print(i, "_ _ _")

print("Два игрока вводят координаты заполняемых полей по очереди:")
gamer = ('Игрок 1', 'Игрок 2')
Pole = [['', '', ''],
        ['', '', ''],
        ['', '', '']]

n1, n2 = 0, 0
for n in range(0, 9):
    x, y = 0, 0
    if (n + 2) % 2 == 0:
        print("Игрок 1, ваш", n1 + 1, "-й ход.")
        n1 += 1
        x = int(input("Введите x:"))
        y = int(input("Введите y:"))
        if Pole[y][x] == '':
            Pole[y][x] = "X"
        else:
            print("Поле заполнено!")
    else:
        print("Игрок 2, ваш", n2 + 1, "-й ход.")
        n2 += 1
        x = int(input("Введите x: "))
        y = int(input("Введите y: "))
        if Pole[y][x] == '':
            Pole[y][x] = "O"
        else:
            print("Поле заполнено!")

    print("    0    1    2  -  столбцы x")
    for i in range(3):
        print(i, Pole[i])
    if Pole[0][0] == Pole[1][1] == Pole[2][2] == 'X' or \
            Pole[0][0] == Pole[0][1] == Pole[0][2] == 'X' or \
            Pole[1][0] == Pole[1][1] == Pole[1][2] == 'X' or \
            Pole[2][0] == Pole[2][1] == Pole[2][2] == 'X' or \
            Pole[0][0] == Pole[0][1] == Pole[0][2] == 'X' or \
            Pole[0][1] == Pole[1][1] == Pole[2][1] == 'X' or \
            Pole[0][2] == Pole[1][2] == Pole[2][2] == 'X' or \
            Pole[2][0] == Pole[1][1] == Pole[0][2] == 'X':
        print("Игрок 1 победил!")
        break
    elif Pole[0][0] == Pole[1][1] == Pole[2][2] == 'O' or \
            Pole[0][0] == Pole[0][1] == Pole[0][2] == 'O' or \
            Pole[1][0] == Pole[1][1] == Pole[1][2] == 'O' or \
            Pole[2][0] == Pole[2][1] == Pole[2][2] == 'O' or \
            Pole[0][0] == Pole[0][1] == Pole[0][2] == 'O' or \
            Pole[0][1] == Pole[1][1] == Pole[2][1] == 'O' or \
            Pole[0][2] == Pole[1][2] == Pole[2][2] == 'O' or \
            Pole[2][0] == Pole[1][1] == Pole[0][2] == 'O':
        print("Игрок 2 победил!")
        break
    if n == 8:
        print("Ничья!")
print("Конец!")
