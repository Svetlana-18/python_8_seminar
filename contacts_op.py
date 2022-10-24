from os.path import exists
from os import remove

def write_contact(user, data):
    data.append(user)


def write_data(data, columns):
    with open(FILE_NAME, "w", encoding="UTF-8") as f:
        f.write(", ".join(columns) + "\n")
        for user in data: 
            f.write(", ".join(user.values()) + "\n")


def add_column(data, column, columns):
    for user in data: 
        user[column] = ""
    columns.append(column)
    return data
        

def read_data():
    valid = exists(FILE_NAME)
    if not valid: 
        return []
    with open(FILE_NAME, "r", encoding="UTF-8") as f: 
        data = f.read()
        print(data) 
        if "\n" not in data:
            return []
        print(data.split("\n"))
        columns = data.split("\n")[0].strip().split(", ")  # строка с заголовком 
        print("\n")
        data = [{columns[i]: user.strip().split(", " )[i] if user else "" for i in range(len(columns))} for user in data.split("\n")[1:] if user] 
        # print(data)
        # print("\n")
        return data


def get_columns(data):
    if not data: 
        return ["Фамилия", "Имя", "Отчество", "Должность", "Номер телефона"]
    columns = list(data[0].keys())
    print(columns)
    return columns


def find_contact(data):
    column = input("Введите столбец поиска: ")
    val = input("Введите значение для поиска: ")
    flag = False
    for user in data:
        if column not in user:
            return "Такого столбца нет!"
        if user[column] == val: 
            print(user)
            flag = True
    if not flag: 
        print("Данные не найдены!")



def del_contact(data):
    column = input("Введите столбец поиска: ")
    val = input("Введите значение для поиска: ")
    flag = False
    for user in data:
        if column not in user:
            return "Такого столбца нет!"
        elif user[column] == val: 
               data.remove(user)
        flag = True
    if not flag: 
        print("Данные не найдены!")



FILE_NAME = "data_base.csv"

