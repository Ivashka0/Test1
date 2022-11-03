import pymysql

try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="22032007Ivan",
        database="test_python",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Connected")
    try:
        select = input("Input SELECT/INSERT/UPDATE/DELETE: ")
        if select.upper() == "SELECT":
            with connection.cursor() as cursor:
                select_table = f"SELECT * FROM `students`;"
                cursor.execute(select_table)
                result = cursor.fetchall()
                for i in result:
                    print(i)
        elif select.upper() == "INSERT":
            name = input("Input name: ")
            password = input("Input password: ")
            with connection.cursor() as cursor:
                insert = f"INSERT INTO `students` (name, password) VALUES({name}, {password})"
                cursor.execute(insert)
                connection.commit()
                print("Inserted")
        elif select.upper() == "UPDATE":
            id = input("Input id of user: ")
            password = input("Input password for updating: ")
            with connection.cursor() as cursor:
                update_table = f"UPDATE `students` SET password={password} WHERE id={id}"
                cursor.execute(update_table)
                connection.commit()
        elif select.upper() == "DELETE":
            name = input("Input name for deleting: ")
            with connection.cursor() as cursor:
                delete_table = f"DELETE FROM `students` WHERE name={name}"
                cursor.execute(delete_table)
                connection.commit()
        else:
            print("Ooops")  
    finally:
        connection.close()

except:
    print("Smthing has gone wrong")