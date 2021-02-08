import os
import json
import shutil
import sys
import platform


def test_create_json():
    name = 'bill_json.txt'
    bill = 100
    my_list = ['a:1р.', 'b:2р.']
    save_data = {
        'bill': bill,
        'list': my_list,
    }
    load_data = {
        'bill': 0,
        'list': [],
    }
    src_answer = os.path.join(os.getcwd(), name)
    if not os.path.exists(src_answer):
        print("Это первый запуск. Создаем файл")
        with open( name, 'w', encoding='utf-8') as f:
            f.write(json.dumps(save_data))
            assert load_data['bill'] == 0

    else:
        with open(name, 'r', encoding='utf-8') as f:
            load_data = json.load(f)
            assert load_data['bill'] > 0
    #assert os.path.exists(src_answer) == True
    #assert save_data == load_data
def test_save_json():
    name = 'bill_json.txt'
    bill = 100
    my_list = ['a:1р.', 'b:2р.']
    save_data = {
        'bill': bill,
        'list': my_list,
    }
    with open(name, 'w', encoding='utf-8') as f:
        f.write(json.dumps(save_data))
        f.close()
        assert save_data['bill'] == 100












