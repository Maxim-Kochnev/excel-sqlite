import sqlite3
import os.path
import openpyxl


def create_db(db_path):
    db = sqlite3.connect(db_path)
    db.close()
    print(f"[INFO] New database was created successfully.")


def create_table(db_path, headers):
    db = sqlite3.connect(db_path)
    c = db.cursor()

    command = "CREATE TABLE articles ("
    for header in headers:
        for header_part in header:
            command += header_part
            command += " "
        command += ", "
        # command += str(header[0] + " " + header[1] + ", ")
    command = command[:-2]
    command += ")"

    print(command)
    c.execute(command)

    db.commit()
    db.close()
    print(f"[INFO] New table was created successfully.")


# def get_headers_from_xlsx():
#     pass


def main():
    # если нет указанной БД, создаем ее
    db_name = "my_data.db"
    db_dir = "db"
    db_path = db_dir + "/" + db_name
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


if __name__ == "__main__":
    main()
