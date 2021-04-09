#! python3
import sys
from pprint import pp
sys.stdin = open('temp.txt', encoding='utf-8')


def mytrans(st, s, d):
    temp = str.maketrans(s, ';' * len(s), d)
    return tuple(v.strip() for v in st.translate(temp).split(';'))


# список книг
books = {k: {'name': '', 'date': 0} for k in mytrans(input(), ',', '"')}
# подготовка входных данных
data = []
for st in iter(input, '.'):
    oper, book, date, *name = mytrans(st, '"(', ')')
    dd1, mm1, yy1 = map(int, date.split('.'))
    mm2, yy2 = (mm1 + 1, yy1) if mm1 < 12 else (1, yy1 + 1)
    data.append({
        'date1': yy1*10000 + mm1*100 + dd1,
        'date2': yy2*10000 + mm2*100 + dd1,
        'oper': oper.lower(),
        'book': book,
        'name': ''.join(name)
    })
# отработка входных данных
for v in sorted(data, key=lambda x: x['date1']):
    if v['oper'] == 'вернуть':
        books[v['book']].update({'name': '', 'date': 0})
    elif v['oper'] == 'взять':
        temp = books[v['book']]
        if v['date1'] >= temp['date']:  # возврат "коллекторами"
            temp.update({'name': '', 'date': 0})
        if temp['name']:  # книга отсутствует
            print(
                f"Книга \"{v['book']}\" отсутствует. "
                f"Ее забрал(а) {temp['name']}"
            )
        else:  # выдача книги
            temp.update({'name': v['name'], 'date': v['date2']})
            print(f"Книгу \"{v['book']}\" забрал(а) {temp['name']}")
