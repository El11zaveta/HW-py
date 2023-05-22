def load_contacts():
    contacts = []
    with open('contacts.txt', 'r') as file:
        for line in file:
            contact = line.strip().split(',')
            contacts.append(contact)
    return contacts

def save_contacts(contacts):
    with open('contacts.txt', 'w') as file:
        for contact in contacts:
            file.write(','.join(contact) + '\n')

def add_contact():
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    middle_name = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    contact = [last_name, first_name, middle_name, phone_number]
    contacts.append(contact)

def display_contacts():
    if len(contacts) == 0:
        print("Телефонная книга пуста.")
    else:
        for contact in contacts:
            print("Фамилия: {}\nИмя: {}\nОтчество: {}\nНомер телефона: {}\n".format(*contact))

def search_contact():
    keyword = input("Введите фамилию или имя для поиска: ")
    found_contacts = []
    for contact in contacts:
        if keyword.lower() in [contact[0].lower(), contact[1].lower()]:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print("Контакт не найден.")
    else:
        for contact in found_contacts:
            print("Фамилия: {}\nИмя: {}\nОтчество: {}\nНомер телефона: {}\n".format(*contact))

def edit_contact():
    kw = input("Введите фамилию или имя контакта для редактирования: ")
    found_contacts = []
    for contact in contacts:
        if kw.lower() in [contact[0].lower(), contact[1].lower()]:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print("Контакт не найден.")
    elif found_contacts == 1:
        print("Найден 1 контакт:")
        display_contacts()
        contact = found_contacts[0]
        print("Введите новые данные для редактирования:")
        first_name = input("Имя: ")
        last_name = input("Фамилия: ")
        middle_name = input("Отчество: ")
        phone_number = input("Номер телефона: ")
        print("Контакт успешно отредактирован.")
        save_contacts(contacts)

def delete_contact():
    kw= input("Введите фамилию или имя контакта для удаления: ")
    found_contacts = []
    for contact in contacts:
        if kw.lower() in [contact[0].lower(), contact[1].lower()]:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print("Контакт не найден.")
    else:
        found_contacts == 1
        print("Найден 1 контакт:")
        display_contacts()
        contacts.remove(found_contacts[0])
        print("Контакт успешно удален.")
        save_contacts(contacts)
   

# Загрузка контактов из файла при запуске программы
contacts = load_contacts()

while True:
    print("Меню:")
    print("1. Просмотр контактов")
    print("2. Добавить контакт")
    print("3. Поиск контакта")
    print("4. Редактирование контакта")
    print("5. Удаление контакта")
    print("6. Выход")
    choice = input("Введите номер пункта меню: ")

    if choice == '1':
        display_contacts()
    elif choice == '2':
        add_contact()
        save_contacts(contacts)
    elif choice == '3':
        search_contact()
    elif choice == '4':
        edit_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        break
    else:
        print("Неправильный ввод. Попробуйте еще раз.")