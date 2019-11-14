year_of_birth = input('Введите год рождения А.С.Пушкина:  ')
if int(year_of_birth) == 1799:
    print('Верно')
    day_of_birth = input('Введите день рождения А.С.Пушкина:  ')
    if day_of_birth == "06.06":
        print('Верно')
    else:
        print('Неверный день рождения!')

else:
    print('Неверный год рождения!')