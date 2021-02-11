from loto_lib import *
response = 'N'# Переменная на выход
# Меню программы
while response != 'stop':
    help_command();
    response = input('Укажите номер пункта меню (help - для вывода списка меню) -> ')
    if response == '1':  # Играть против компьютера
        user_vs_comp()
        pass
    elif response == '2':  # Играть против друг-друга
        user_vs_user()
        pass
    elif response == '3':  # Компьютер против компьютера
        comp_vs_comp()
        pass

    elif (response.lower() == 'help'):  # help
        help_command();
        pass
    elif (response == '0') or (response.lower() == 'stop'):  # Выход
        print('Выход из программы...')
        break
    else:
        print("Повторите ввод.")