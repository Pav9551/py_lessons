# [ДЗ к уроку 18 "Веб-сайт на Flask. MVC"](https://startbootstrap.com/theme/freelancer/)

Эта вебстраничка на базе Flask сделана с применением
[Freelancer](https://startbootstrap.com/theme/freelancer/) - одного из возможных шаблонов  [Bootstrap](https://getbootstrap.com/).

## Это базовый шаблон

[![Freelancer Preview](https://assets.startbootstrap.com/img/screenshots/themes/freelancer.png)](https://startbootstrap.github.io/startbootstrap-freelancer/)

**[View Live Preview](https://startbootstrap.github.io/startbootstrap-freelancer/)**

ndencies Status](https://david-dm.org/StartBootstrap/startbootstrap-freelancer/dev-status.svg)](https://david-dm.org/StartBootstrap/startbootstrap-freelancer?type=dev)

## Установка и запуск

Перед тем как пытаться запусить, прочитайте инструкцию:

- Загрузите файлы: `git clone https://github.com/Pav9551/py_lessons/tree/lesson16_head_18`
- Зайдите в загруженный каталог: py_lessons/lesson16/startbootstrap/
- Установите необходимые модули:
```bash
$ pip install -r requirements.txt
```
- Для запуска сервера нужно набрать команды в терминале:
```bash
$ export FLASK_APP=main
$ flask run
```




## О программе

Программа парсит вакансии с сайта hh.ru и отображает требуемые навыки к кандидату. Тематика навыков зависит от запроса. Список навыков, которые хранятся в базе данных после запроса, отображаются на белом фоне. Предусмотрена кнопка, которая очищает базу данных. Главная задача программы - узнать смежные навыки, которые часто требуются с ключевым навыком.

