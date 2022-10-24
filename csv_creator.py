def creat_csv():
    FILE_NAME = "data_base.csv"
    with open (FILE_NAME, "w", encoding = 'UTF-8') as f:
        f.write("Фамилия, Имя, Отчество, Должность, номер телефона \n")
