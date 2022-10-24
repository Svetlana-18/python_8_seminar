from contacts_op import get_columns
from input_data import add_contact
from contacts_op import find_contact, read_data, add_column, write_data, izm_contact, del_contact


def user_interface():
    data = read_data()
    columns = get_columns(data)
    flag = True
    while flag:
        print("\n***** ДОБРО ПОЖАЛОВАТЬ В БАЗУ ДАННЫХ! *****\n\nВыберите пункт меню для продолжения:")
        while True:
            print("1 - Найти сотрудника")
            print("2 - Добавить сотрудника")
            print("3 - Показать список всех сотрудников")
            print("4 - Изменить данные в записи о сотруднике")
            print("5 - Удалить запись о сотруднике")
            print("6 - Выход")
            choice = input()
            if choice not in ["1", "2", "3", "4", "5", "6"]:
                print("!!Выбран неверный пункт меню!! \n Попробуйте ещё раз")
                continue
            if choice == "1":
                find_contact(data)
                break
            elif choice == "2":
                add_contact(data, columns)
                break
            elif choice == "3":
                print(columns)
                print(data)
            elif choice == "4":
                 izm_contact(data)
            elif choice == "5":
                del_contact(data)
                break
            else:
                flag = False
                write_data(data, columns)
                break
