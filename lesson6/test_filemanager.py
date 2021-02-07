import os
import shutil
import sys
import platform
def getpath():
    print("Текущая папка:")
    print(os.getcwd())
def test_create_dir():
    answer = 'test_folder'#имя создаваемой папки
    temp_dir = os.path.join(os.getcwd(), answer)
    try:
        if os.path.exists(temp_dir):
            print('Указанная папка уже существует')
        else:
            os.mkdir(temp_dir)
            print('Cоздана папка: {}'.format(answer))
            print("")
    except:
        pass
    assert os.path.exists(temp_dir) == True

def test_copy_file_or_dir():
    src_answer = 'test_folder'
    dest_answer = 'test_folder' #имя копируемой папки
    if src_answer == dest_answer:
        dest_answer = dest_answer + "_copy"#имя копируемой папки
    else:
        src_answer = os.path.join(os.getcwd(), src_answer)
        dest_answer = os.path.join(os.getcwd(), dest_answer)
    if not os.path.exists(src_answer):
        print("Исходный файл/папка не найден")
    else:
        try:
            if os.path.isfile(src_answer):          # Файл
                shutil.copy2(src_answer, dest_answer)
                print("Файл успешно скопирован")
            elif os.path.isdir(src_answer):         # Директория
                shutil.copytree(src_answer, dest_answer)
                print("Каталог успешно скопирован")
        except IOError as e:
            print(f'ОШИБКА. Сообщение: {e.strerror}')
    assert os.path.exists(dest_answer) == True



def test_del_file_or_dir():
    answer = 'test_folder'#имя удаляемой папки
    temp_name = os.path.join(os.getcwd(), answer)
    try:
        if os.path.exists(temp_name):       # Объект найден
            if os.path.isfile(temp_name):   # Файл
                os.remove(temp_name)
                print('Файл удалён: {}'.format(answer))
            elif os.path.isdir(temp_name):  # Директория
                shutil.rmtree(temp_name)
                print("Папка успешно удалена")
        else:
            print("Указанный файл/папка не найдена")
    except:
        print("Ошибка удаления файла/папки.")
    assert os.path.exists(temp_name) == False
def test_del_file_or_dir_copy():
    answer = 'test_folder_copy'#имя удаляемой папки
    temp_name = os.path.join(os.getcwd(), answer)
    try:
        if os.path.exists(temp_name):       # Объект найден
            if os.path.isfile(temp_name):   # Файл
                os.remove(temp_name)
                print('Файл удалён: {}'.format(answer))
            elif os.path.isdir(temp_name):  # Директория
                shutil.rmtree(temp_name)
                print("Папка успешно удалена")
        else:
            print("Указанный файл/папка не найдена")
    except:
        print("Ошибка удаления файла/папки.")
    assert os.path.exists(temp_name) == False

def test_find_all_in_current_dir():
    getpath()
    all = []
    print("Список директорий и файлов в текущем каталоге:")
    for item in os.walk(os.getcwd()):
        all.append(item)
    dirs = all[0][1]
    print("Директории:")
    for dir in dirs:
        print(f"{dir}")
    files = all[0][2]
    print("Файлы:")
    for file in files:
        print(f"{file}")
    print(f"*************")
    assert files == ['bill.py', 'main.py', 'py_сommander.py', 'test_filemanager.py', 'test_python.py', 'victory.py']


