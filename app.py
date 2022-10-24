import sqlite3
import os
import openpyxl

# создание БД
def create_db(db_path):
    db = sqlite3.connect(db_path)
    db.close()
    print(f"[INFO] New database was created successfully.")


# создание таблицы в БД
def create_table(db_path, headers):
    db = sqlite3.connect(db_path)
    c = db.cursor()

    command = "CREATE TABLE articles ("
    for header in headers:
        for header_part in header:
            command += f'{header_part} '
        command = f'{command[:-1]}, '
    command = f'{command[:-2]})'

    print(command)
    c.execute(command)

    db.commit()
    db.close()
    print(f"[INFO] New table was created successfully.")


# def get_headers_from_xlsx():
#     pass

# def menu():
#     # проверка наличия БД, вывод списка созданных БД
#     db_dir = "db"

#     # вывод меню



# вывод списка файлов и папок
def print_file_list():
    for root, dirs, files in os.walk("."):
        print(f'root: {root}')
        print(f'directories:')
        for dir in dirs:
            print(dir)
        print(f'files:')
        for filename in files:
            print(filename)



def main():
    # если нет указанной БД, создаем ее
    db_name = "my_data.db"
    db_dir = "db"
    db_path = f'{db_dir}/{db_name}'
    check_base = os.path.exists(db_path)
    
    if not check_base:
        create_db(db_path)
        # headers = get_headers_from_xlsx()
        headers = [
            ("time", "DateTime"),
            ("event", "text"),
            ("tags", "text"),
            ("adding_time", "DateTime")
        ]
        create_table(db_path, headers)

    # вывод списка файлов и папок
    print_file_list()




if __name__ == "__main__":
    main()
