import requests
import re
import json
import os
from os.path import exists
import pandas as pd
pd.set_option('display.max_colwidth', 100)

#http://google.github.io/proto-lens/installing-protoc.html
#https://habr.com/ru/post/680320/?ysclid=l6xpo6itvm552340478
from google.protobuf.json_format import MessageToJson#protobuf
import offers_pb2#
def get_files_in_current_dir():
    print("Список файлов в текущей директории:")
    files = list(filter(lambda x: os.path.isfile(x), os.listdir(".")))
    ret = []
    for file in files:
        if file.endswith('.xlsx'):
            if file == "5ka.xlsx":
                ret.append(file)
            if file == "lenta-super.xlsx":
                ret.append(file)
            if file == "eurospar.xlsx":
                ret.append(file)
            if file == "perekrestok.xlsx":
                ret.append(file)
            if file == "dixy.xlsx":
                ret.append(file)
    print(ret)
    return ret
def parse_page(city = "moskva", shop = "lenta-super", page_num = 25):
    """
    :param city: location of the shop
    :param shop: shop name
    :param page_num: parsed page number
    :return:  json.dumps
    """
    url = f"https://squark.edadeal.ru/web/search/offers?count=30&locality={city}&page={page_num}&retailer={shop}"
    data = requests.get(url, allow_redirects=True)  # data.content is a protobuf message
    offers = offers_pb2.Offers()  # protobuf structure
    offers.ParseFromString(data.content)  # parse binary data
    products: str = MessageToJson(offers)  # convert protobuf message to json
    products = json.loads(products)
    ret = json.dumps(products, indent=4, ensure_ascii=False, )
    return products
class ED:
    city = "moskva"
    shop = "lenta-super"
    GOODS = 'goods.xlsx'
    good = 'Молоко'
    num = 1
    def __init__(self, CITY = city, SHOP = shop):
        self.city = CITY
        self.shop = SHOP
    def load_xlsx(self,search_goods=GOODS):
        self.search_goods = search_goods
        self.excel_data_df = pd.read_excel(search_goods, sheet_name='Sheet1')

        return self.excel_data_df
    def add_xlsx(self,add_good=good):
        self.add_good = add_good
        df = pd.DataFrame({
            'name': [self.add_good],#В названии первая буква заглавная
            'find': 0})
        self.excel_data_df = pd.concat([self.excel_data_df, df])
        self.excel_data_df = self.excel_data_df.drop_duplicates(subset=['name'])
        self.excel_data_df.reset_index(inplace=True, drop=True)
        self.excel_data_df.to_excel(self.GOODS,index = False)
        print(self.excel_data_df)
        text = f'В файл {self.GOODS} добавлен товар: {self.add_good}'
        return text
    def save_username(self,message_chat):
        self.add_good = message_chat.first_name
        chat_id = message_chat.id
        chat_first_name = message_chat.first_name
        chat_last_name = message_chat.last_name
        chat_username = message_chat.username
        self.excel_data_df = pd.read_excel("names.xlsx", sheet_name='Sheet1')
        df = pd.DataFrame({
            'chat_id': [chat_id],
            'first_name': [chat_first_name],
            'last_name': [chat_last_name],
            'username': [chat_username]})
        self.excel_data_df = pd.concat([self.excel_data_df, df])
        self.excel_data_df = self.excel_data_df.drop_duplicates(subset=['chat_id'])
        self.excel_data_df.reset_index(inplace=True, drop=True)
        self.excel_data_df.to_excel('names.xlsx',index = False)
        print(self.excel_data_df)
        text = f'В пользователь {self.add_good}'
        return text
    def del_good_xlsx(self,del_num=num):
        self.del_num = int(del_num)
        self.excel_data_df.drop(labels=[self.del_num], axis=0, errors='ignore',inplace=True)
        self.excel_data_df.reset_index(inplace=True, drop=True)
        self.excel_data_df.to_excel(self.GOODS,index = False)
        text = f'В файле {self.GOODS} удален товар № {self.del_num}'
        return text
    def get_df_discount(self):
        #TODO пропускать повторное за день создание df_res
        #лучшее решение - это подождать
        i = 1
        df_res = pd.DataFrame()
        ret = parse_page(city=self.city, shop=self.shop, page_num=i)
        print("запрос на сайт, ждите....")
        while (len(ret)>0):#перебор страниц
            df = pd.json_normalize(ret['offer'])
            df_res = pd.concat([df_res, df])
            i = i + 1
            ret = parse_page(city=self.city, shop=self.shop, page_num=i)
        df_res.reset_index(inplace=True, drop=True)
        self.df_res = df_res
        return df_res
    def search(self):
        data_frame = pd.DataFrame()
        for good in self.excel_data_df.name:
            count = 0
            for good_discount in self.df_res.name:
                result = re.match(good.lower(), good_discount.lower())
                if ((result is None) == False):
                    #print(count, good_discount)
                    df = pd.DataFrame({
                    'count': [count],
                    'good': [good],
                    'name': [good_discount]})
                    data_frame = pd.concat([data_frame, df])
                count = count + 1
        data = data_frame.merge(self.df_res, on=['name'], how='left')
        data = data.drop_duplicates(subset=['name'])
        data.to_excel(f"{self.shop}.xlsx", index=False)
        print(f"Данные выгружены в файл {self.shop}.xlsx")
        return f"{self.shop}.xlsx"
    def send_file(self,token,chat_id):
        url = f'https://api.telegram.org/bot{token}/'
        method = url + 'sendDocument'
        filename = f"{self.shop}.xlsx"
        if exists(filename):
            with open(filename, "rb") as filexlsx:
                files = {"document": filexlsx}
                title = filename
                r = requests.post(method, data={"chat_id": chat_id, "caption": title}, files=files)
                if r.status_code != 200:
                    raise Exception("send error")
                else:
                    return f"Файл отправлен."
        else:
            return f"Файл не сформирован."
    def send_users(self,token,chat_id):
        url = f'https://api.telegram.org/bot{token}/'
        method = url + 'sendDocument'
        filename = f"names.xlsx"
        if exists(filename):
            with open(filename, "rb") as filexlsx:
                files = {"document": filexlsx}
                title = filename
                r = requests.post(method, data={"chat_id": chat_id, "caption": title}, files=files)
                if r.status_code != 200:
                    raise Exception("send error")
                else:
                    return f"Файл отправлен."
        else:
            return f"Файл не сформирован."
    def send_all(self,token,chat_id):
        files = get_files_in_current_dir()
        self.all_data_df = pd.DataFrame()
        if len(files) == 0:
            return False

        for file in files:
            df = pd.read_excel(file, sheet_name='Sheet1')
            df['shop'] = file
            self.all_data_df = pd.concat([self.all_data_df , df])
            try:
                if os.path.exists(file):  # Объект найден
                    os.remove(file)
                    print('Файл удалён: {}'.format(file))
            except:
                print("Ошибка удаления файла/папки.")
        self.all_data_df.sort_values(['good','priceAfter'], ascending=[True, True], kind="mergesort", inplace=True)
        filename = f"all.xlsx"
        self.all_data_df.to_excel(filename, index=False)
        url = f'https://api.telegram.org/bot{token}/'
        method = url + 'sendDocument'
        if exists(filename):
            with open(filename, "rb") as filexlsx:
                files = {"document": filexlsx}
                title = filename
                r = requests.post(method, data={"chat_id": chat_id, "caption": title}, files=files)
                if r.status_code != 200:
                    raise Exception("send error")
                else:
                    return True
        else:
            return False