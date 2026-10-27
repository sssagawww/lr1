from csv import reader
from random import randint
import xml.dom.minidom as minidom


# Считывание таблицы из файла
def open_table():
    try:
        with open('books-en.csv', 'r', errors='ignore') as file:
            cur_table = list(reader(file, delimiter=';'))
            cur_table = cur_table[1:]
            return cur_table
    except FileNotFoundError:
        print("Файл не найден!")
        return []


table = open_table()


# Вывод количества записей с названием длиной более 30 символов
def count_titles():
    count = 0
    for row in table:
        if len(row[1]) > 30:
            count += 1
    print(f'Длина название больше 30 символов у {count} строк.')


# Поиск строки с без учета индекса
def find_string(search_line, string):
    string = string.lower()
    index = string.find(search_line.lower())
    return index


# Поиск по автору с ограничением от 200 руб
def search_author():
    search_line = input('Введите автора: ')
    amount = 0
    for row in table:
        if (find_string(search_line, row[2]) != -1) and (float(row[-1].replace(',', '.')) > 200):
            print(f'{row[1]}, {row[2]}, цена: {row[-1]}')
            amount += 1
    if amount == 0:
        print("Ничего не найдено!")
    else:
        print('Найдено позиций: ', amount)


# Создание библиографических ссылок
def generate_links():
    output_file = open('result.txt', 'w')
    nums = [randint(0, len(table)) for _ in range(20)]
    for num, i in enumerate(nums):
        output_file.write(f'{num + 1}. {table[i][2]}. {table[i][1]} - {table[i][3]}\n')
    output_file.close()
    print("Файл создан!")


# Вывод списка издательств без повторений
def find_publishers():
    publishers = set([row[4] for row in table])
    print("Список издательств")
    for num, p in enumerate(publishers):
        print(num + 1, p)


# Вывод самых популярных книг (самых скачиваемых)
def find_popular_books():
    books = [[int(row[5]), f'{row[2]}. {row[1]} - {row[5]} скачиваний'] for row in table]
    books.sort(reverse=True)
    for i in range(20):
        print(books[i][1])


# count_titles()
# search_author()
# generate_links()
# find_publishers()
# find_popular_books()


# 2 часть работы
xml_file = open('currency.xml', errors='ignore')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

nodes = dom.getElementsByTagName('Valute')
numCodes = []
charCodes = []

for node in nodes:
    for childNode in node.childNodes:
        if childNode.nodeType == 1:
            if childNode.tagName == 'NumCode':
                if childNode.firstChild.nodeType == 3:
                    numCodes.append(childNode.firstChild.data)
            if childNode.tagName == 'CharCode':
                if childNode.firstChild.nodeType == 3:
                    charCodes.append(childNode.firstChild.data)

xml_file.close()
print(numCodes)
print(charCodes)
