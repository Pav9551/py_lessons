n = int(input("Количество человек в команде?"))
players = {'Петя':45}
for i in range(n):
    name = input("Введите имя человека:")
    if name in players:
        print(players[name])
    else:
        print("Такого человека в команде нет:")
        name = input("Имя:")
        size = input("Размер:")
        players[name] = size