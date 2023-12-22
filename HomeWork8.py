import json

def Contact_add(PhoneBook, name, number):
    PhoneBook[name] = number
    save_PhoneBook(PhoneBook)

def delete_contact(PhoneBook, name):
    del PhoneBook[name]
    save_PhoneBook(PhoneBook)

def change_contact(PhoneBook, name, new_number):
    PhoneBook[name] = new_number
    save_PhoneBook(PhoneBook)

def show_PhoneBook(PhoneBook):
    print("Телефонный справочник:")
    for name, number in PhoneBook.items():
        print(f"{name}: {number}")

def save_PhoneBook(PhoneBook):
    with open('PhoneBook.json', 'w') as file:
        json.dump(PhoneBook, file)

def import_PhoneBook():
    try:
        with open('PhoneBook.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def search_contact(PhoneBook, name):
    if name in PhoneBook:
        return PhoneBook[name]
    else:
        return None

def main_menu():
    PhoneBook = import_PhoneBook()

    while True:
        print("\nГлавное меню:")
        print("1. Показать все контакты")
        print("2. Добавить контакт")
        print("3. Удалить контакт")
        print("4. Изменить контакт")
        print("5. Поиск контакта")
        print("6. Выход")

        choise = input("Введите номер операции: ")

        if choise == "1":
            show_PhoneBook(PhoneBook)
        elif choise == "2":
            name = input("Введите имя контакта: ")
            number = input("Введите номер контакта: ")
            Contact_add(PhoneBook, name, number)
        elif choise == "3":
            name = input("Введите имя контакта для удаления: ")
            delete_contact(PhoneBook, name)
        elif choise == "4":
            name = input("Введите имя контакта для изменения: ")
            new_number = input("Введите новый номер контакта: ")
            change_contact(PhoneBook, name, new_number)
        elif choise == "5":
            name = input("Введите имя контакта для поиска: ")
            result = search_contact(PhoneBook, name)
            
            if result:
                print(f"Контакт найден: {name}: {result}")
            else:
                print("Контакт не найден")
        elif choise == "6":
            save_PhoneBook(PhoneBook)
            print("До свидания!")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

main_menu()