from itertools import zip_longest

# 1. Не используя библиотеки для парсинга, распарсить (получить определённые
# данные) файл логов web-сервера nginx_logs.txt.
# Получить список кортежей вида:
# (<remote_addr>, <request_type>, <requested_resource>). Код должен работать
# даже с файлами, размер которых превышает объем ОЗУ компьютера.

req = []
with open('nginx_logs.txt', 'r') as file:
    for i in file:
        req.append((i[:i.find(' ')],
                    i[i.find('"') + 1:i.find(' ', i.find('"'))],
                    i[i.find(' ', i.find('"')) + 1:
                      i.find('HTTP', i.find('"')) - 1]))

# print(req)

# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов
# по данным файла логов из предыдущего задания.

cnt = {}
for i in req:
    cnt[i[0]] = cnt.setdefault(i[0], 0) + 1

mxm = 0
for i, j in cnt.items():
    if j > mxm:
        mxm = j
        ip = i
print(ip)

# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом —
# данные об их хобби. Известно, что при хранении данных используется принцип:
# одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них
# словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
# Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше
# записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот —
# выходим из скрипта с кодом «1». При решении задачи считать, что объём данных
# в файлах во много раз меньше объема ОЗУ.

# with open('users.csv', 'r') as users,\
#         open('hobby.csv', 'r') as hobby,\
#         open('us_hob.csv', 'w') as us_hob:
#     usr = [i.strip() for i in users]
#     hbb = [i.strip() for i in hobby]
#     if len(usr) < len(hbb):
#         exit(1)
#     else:
#         ushob = {i: j for i, j in zip_longest(usr, hbb) if i is not None}
#         print(*[f'{i}: {j}' for i, j in ushob.items()], sep='\n',
#               file=us_hob)

# 4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах
# превышает объём ОЗУ (разумеется, не нужно реально создавать такие большие
# файлы, это просто задел на будущее проекта). Также реализовать парсинг
# данных из файлов — получить отдельно фамилию, имя и отчество для
# пользователей и название каждого хобби: преобразовать в какой-нибудь
# контейнерный тип (список, кортеж, множество, словарь). Обосновать выбор
# типа. Подумать, какие могут возникнуть проблемы при парсинге. В словаре
# должны храниться данные, полученные в результате парсинга.

# 5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки,
# чтобы можно было задать путь к обоим исходным файлам и путь к выходному
# файлу со словарём. Проверить работу скрипта для случая, когда все файлы
# находятся в разных папках.

with open(input(), 'r') as users,\
        open(input(), 'r') as hobby,\
        open(input(), 'w') as us_hob:
    usr = [i.strip().split(',') for i in users]
    hbb = [i.strip().split(',') for i in hobby]
    if len(usr) < len(hbb):
        exit(1)
    else:
        ushob = {' '.join(i): ', '.join(j) for i, j in zip_longest(usr, hbb)
                 if i is not None}
        print(*[f'{i}: {j}' for i, j in ushob.items()], sep='\n', file=us_hob)
