import csv
import xml.etree.ElementTree as ET

# путь
books_file = 'books.csv'

# 30
with open(books_file, 'r', encoding='windows-1251') as f:
    reader = csv.DictReader(f, delimiter=';')
    long_titles_count = sum(1 for row in reader if len(row['Название']) > 30)
print(f'Количество записей с названием длиннее 30 символов: {long_titles_count}')

# поиск
def search_books_by_author(author):
    results = []
    with open(books_file, 'r', encoding='windows-1251') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            if author.lower() in row['Автор (ФИО)'].lower():
                results.append(row)
    return results

search_author = input("Введите ФИО автора для поиска: ")
search_results = search_books_by_author(search_author)
if search_results:
    for result in search_results:
        print(f"Название: {result['Название']}, Автор: {result['Автор (ФИО)']}")
else:
    print("Книги не найдены.")

# ссылки
def generate_bibliography(records, output_file='bibliography.txt'):
    with open(output_file, 'w', encoding='utf-8') as f:
        for i, record in enumerate(records[:20], start=1):
            author = record['Автор (ФИО)']
            title = record['Название']
            year = record.get('Дата поступления', 'Неизвестно')[:4]
            f.write(f"{i}. {author}. {title} - {year}\n")
    print(f"Библиографические ссылки сохранены в {output_file}")

with open(books_file, 'r', encoding='windows-1251') as f:
    reader = list(csv.DictReader(f, delimiter=';'))
    generate_bibliography(reader)

# путь
xml_file = 'currency.xml'

tree = ET.parse(xml_file)
root = tree.getroot()

char_codes = []
values = []

for valute in root.findall('Valute'):
    char_code = valute.find('CharCode').text
    value = valute.find('Value').text
    char_codes.append(char_code)
    values.append(value)

print("CharCodes:", char_codes)
print("Values:", values)
