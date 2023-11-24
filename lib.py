import sqlite3
def getById(id):
    try:
        sqlite_connection = sqlite3.connect('laba.db')
        cursor = sqlite_connection.cursor()


        sqlite_insert_with_param = """select * from users where id = ?"""
        data = (str(id),)


        cursor.execute(sqlite_insert_with_param,data)
        res = cursor.fetchall()
        sqlite_connection.commit()



        cursor.close()
        return res[0]



    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def getLatestId():
    try:
        sqlite_connection = sqlite3.connect('laba.db')
        cursor = sqlite_connection.cursor()


        sqlite_insert_with_param = """select MAX(id) from users """



        cursor.execute(sqlite_insert_with_param)
        res = cursor.fetchall()
        sqlite_connection.commit()



        cursor.close()
        return int(res[0][0])



    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def getByName(name):
    try:
        sqlite_connection = sqlite3.connect('laba.db')
        cursor = sqlite_connection.cursor()


        sqlite_insert_with_param = """select message from users where name = ?"""
        data = (str(name),)


        cursor.execute(sqlite_insert_with_param,data)
        res = cursor.fetchall()
        sqlite_connection.commit()



        cursor.close()
        return res[0][0]



    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def add(name,message):
    if len(message) == 0:
        return "Message cant be empty"

    try:
        sqlite_connection = sqlite3.connect('laba.db')
        cursor = sqlite_connection.cursor()


        sqlite_insert_with_param = """INSERT INTO users
                             (name,message)
                             VALUES (?, ?);"""

        data_tuple = (str(name),str(message),)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqlite_connection.commit()


        cursor.close()
        return "Success"

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def update(id,message):
    if id > getLatestId():
        return "Theres no user with such an ID"
    try:
        sqlite_connection = sqlite3.connect('laba.db')
        cursor = sqlite_connection.cursor()


        sqlite_update_with_param = """update users set message = ? where id = ?"""

        data_tuple = (str(message),int(id),)
        cursor.execute(sqlite_update_with_param, data_tuple)
        sqlite_connection.commit()


        cursor.close()
        return "Success"

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")



def delete(id):
    try:
        getById(id)
    except IndexError:
        return None


    try:
        sqlite_connection = sqlite3.connect('laba.db')
        cursor = sqlite_connection.cursor()
        sqlite_delete_with_param = """delete from users where id = ?"""
        data_tuple = (int(id),)
        cursor.execute(sqlite_delete_with_param, data_tuple)
        sqlite_connection.commit()
        cursor.close()
        return "Success"
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


