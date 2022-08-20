from edadeal import ED

lenta = ED(CITY = "moskva", SHOP = "lenta-super")#создаем экземпляр класса
pyterochka = ED(CITY = "moskva", SHOP = "5ka")#создаем экземпляр класса
perekrestok = ED(CITY = "moskva", SHOP = "perekrestok")#создаем экземпляр класса
eurospar = ED(CITY = "moskva", SHOP = "eurospar")#создаем экземпляр класса
ans = ''
while not (ans == '0'):
    print('Поиск товаров со скидками из списка содержащегося в файле goods.xlsx в магазинах:')
    print('1 - Лента супермаркет')
    print('2 - Пятерочка')
    print('3 - Перекресток')
    print('4 - Спар')
    print('0 - завершить программу')
    ans = input('Введите пункт меню: ')
    if ans == '1':
        lenta.load_xlsx('goods.xlsx')  # загружаем интересующие нас товары
        lenta.get_df_discount()  # запрашиваем список товаров со скидками
        lenta.search()
        print()
    if ans == '2':
        pyterochka.load_xlsx('goods.xlsx')  # загружаем интересующие нас товары
        pyterochka.get_df_discount()  # запрашиваем список товаров со скидками
        pyterochka.search()
        print()
    if ans == '3':
        perekrestok.load_xlsx('goods.xlsx')  # загружаем интересующие нас товары
        perekrestok.get_df_discount()  # запрашиваем список товаров со скидками
        perekrestok.search()
        print()
    if ans == '4':
        eurospar.load_xlsx('goods.xlsx')  # загружаем интересующие нас товары
        eurospar.get_df_discount()  # запрашиваем список товаров со скидками
        eurospar.search()
        print()

