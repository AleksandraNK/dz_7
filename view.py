def main_menu():
    commands=['Показать все контакты',
            'Открыть файл',
            'Сохранить файл',
            'Новый контакт',
            'Изменить контакт',
            'Удалить контакт',
            'Найти контакт',
            'Выйти из программы']
    print('\nВыберите пункт меню: ')
    for i in range(len(commands)):
        print(f'\t{i+1}.{commands[i]}')
    user_input=int(input('\nВведите пункт меню: '))
    return user_input
    # Добавить защиту от дурака

def show_contacts(phone_book:list):
    if len(phone_book)>0:
        for item in phone_book:
            print(f'{item[0]} {item[1]} ({item[2]})')
    else:
        print('Телефонная книга пустая или не загружена')

def load_success():
    print('Телефонная книга загружена успешно')


def save_success():
    print('Телефонная книга сохранена успешно')



def new_contact():
    name=input('Введите фамилию и имя контакта: ')
    phone=input('Введите номер телефона: ')
    comment=input('Введите комментарий к контакту: ')
    return name, phone, comment


def find_contact():
    search=input('Введите искомое значение: ')
    return search





