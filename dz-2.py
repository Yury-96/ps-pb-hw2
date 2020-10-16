account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}
user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}
user_list = [user1, user2, user3, user4]


key = input('Введите ключ (name или account):')
key = key.lower()
try:
    user1[key]
    print(f"значение ключа {key} для юзера 1 = {user1[key]}")
    print(f"значение ключа {key} для юзера 2 = {user2[key]}")
    print(f"значение ключа {key} для юзера 3 = {user3[key]}")
    print(f"значение ключа {key} для юзера 4 = {user4[key]}")
except KeyError:
    print('Введенный ключ не найден')


try:
    numer = input('Введите порядковый номер:')
    result = int(str(numer[0])) # проверяем, является ли первый символ строки "numer" цифрой
    numer = int(numer) # проверяем, является ли строка "numer" числом
    result = 1/numer # проверяем, является ли введенное число нулём
    result = user_list[numer-1] # проверяем, есть ли в списке элемент (юзер) с введенным индексом
    print('Данные по юзеру №', numer, ':')
    print('имя:', user_list[numer-1]['name'])
    print('возраст:', user_list[numer-1]['age'])
    print('логин', user_list[numer-1]['account']['login'])
    print('пароль:', user_list[numer-1]['account']['password'])
except:
    print('Пользователь с указанным номером не найден')



try:
    numer = input('Введите номер пользователя, которого нужно переместить в конец: ')
    result = int(str(numer[0])) # проверяем, является ли первый символ строки "numer" цифрой
    numer = int(numer) # проверяем, является ли строка "numer" числом
    result = 1/numer # проверяем, является ли введенное число нулём
    result = user_list[numer-1] # проверяем, есть ли в списке элемент (юзер) с введенным индексом
    print('Список до изменения:')
    print(user_list)
    print('Пользователь с именем', user_list[numer-1]['name'], 'перемещён в конец' )
    element = user_list.pop(numer-1)
    user_list.append(element)
    print('Список после изменения:')
    print(user_list)
except:
    print('Пользователь с указанным номером не найден')


mean = (user1['age']+user2['age']+user3['age']+user4['age'])/4
print('Средний возраст пользователей:', mean)
