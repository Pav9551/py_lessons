"""
Домашнее задание № 5
"""
from py_сommander import *
from bill import bill_game
from victory import victory_game
response = 'N'# Переменная на выход

# Меню программы
while response != 'stop':
    help_command();
    response = input('Укажите номер пункта меню (help - для вывода списка меню) -> ')
    if response == '1':  # Создать папку
        create_dir()
        pass
    elif response == '2':  # Удалить (файл/папку)
        del_file_or_dir()
        pass
    elif response == '3':  # Копировать (файл/папку)
        copy_file_or_dir()
        pass
    elif response == '4':  # Просмотр содержимого рабочей директории
        find_all_in_current_dir()
        pass
    elif response == '5':  # Посмотреть только папки
        get_dir_in_current_dir()
        pass
    elif response == '6':  # Посмотреть только файлы
        get_files_in_current_dir()
        pass
    elif response == '7':  # Просмотр информации об операционной системе
        get_system_info()
        pass
    elif response == '8':  # Создатель программы
        print(f"Создатель программы: Морозов Павел.")
        print(f"Дата создания программы: 15.12.2020")
        print()
    elif response == '9':  # Играть в викторину
        victory_game()
    elif response == '10':  # Мой банковский счет
        bill_game()
        pass
    elif response == '11':  # Cохранить содержимое рабочей директории в файл
        save_files_and_dirs()
        pass

    elif (response.lower() == 'help'):  # help
        help_command();
        pass
    elif (response == '0') or (response.lower() == 'stop'):  # Выход
        print('Выход из программы...')
        break
    else:
        print("Повторите ввод.")
