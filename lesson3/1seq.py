print('Введите длину списка: ')
count = int(input())#ввод
my_list = []
for number in range(count):
    print('Введите {} элемент:'.format(number+1))
    element = int(input())#ввод элемента
    my_list.append(element)
my_list.sort()#сортировка
print(my_list)

