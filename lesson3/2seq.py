input_list = input('Введите элементы списка через запятую, двоеточее или слеш:')
'''input_list = '1;2,3/4,4,3'
input_list = '1;2;3;4;4/3e'
input_list = '1;2;3;4;4;3'
input_list = '1,2,3,4,4,3'
input_list = '1/2/3/4/4/3'''
in_status = 0;#переменная признака правильности ввода данных
input_list_rep1 = input_list.replace(';',',')#заменяем двоеточее
input_list_good = input_list_rep1.replace('/',',')#заменяем слеша
if input_list.find(',', 0,len(input_list)) > 0:
    in_status = in_status + 1#присутствует запятая
if input_list.find(';', 0,len(input_list)) > 0:
    in_status = in_status + 1#присутствует двоеточее
if input_list.find('/', 0,len(input_list)) > 0:
    in_status = in_status + 1#присутствует слеш
if (in_status == 1):#если присутствует только один из знаков, то выдаем результат
    set_of_num = set(input_list_good.split(','))#перобразуем список во множество
    print(f'Список уникальных элементов: {list(set_of_num)}')# выводим результат как список
else:
    print('так нельзя...')







