import pymysql

try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="nopassword",
        database="sales",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Connected")
    try:
        print("1. All sales \
              \n2. All saleman sales \
              \n3. Sum of purchase with specific customer \
              \n4. Name of customers by saleman \
              \n5. Sum of all bills by specific salesman \
              \n6. Description by customer \
              \n7. List of customers,where bill bigger 50")
        select = input("Input number or SELECT/INSERT/UPDATE/DELETE: ")
        if select.upper() == "SELECT":
            with connection.cursor() as cursor:
                select_table = f"SELECT * FROM `allsales`;"
                cursor.execute(select_table)
                result = cursor.fetchall()
                for i in result:
                    print(i)
        elif select.upper() == "INSERT":
            name = input("Input name of new salesman: ")
            salary = input("Input his salary: ")
            with connection.cursor() as cursor:
                insert = f"INSERT INTO `salesman` (name, salary) VALUES({name}, {salary})"
                cursor.execute(insert)
                connection.commit()
                print("Inserted")
        elif select.upper() == "UPDATE":
            id = input("Input id of salesman: ")
            salary = input("Input salary for updating: ")
            with connection.cursor() as cursor:
                update_table = f"UPDATE `salesman` SET salary={salary} WHERE id={id}"
                cursor.execute(update_table)
                connection.commit()
        elif select.upper() == "DELETE":
            name = input("Input name of salesman for deleting: ")
            with connection.cursor() as cursor:
                delete_table = f"DELETE FROM `salesman` WHERE name={name}"
                cursor.execute(delete_table)
                connection.commit()
        elif select == "1":
            with connection.cursor() as cursor:
                select_table = f"SELECT * FROM `allsales`;"
                cursor.execute(select_table)
                result = cursor.fetchall()
                print(result)
        elif select == "2":
            with connection.cursor() as cursor:
                select_table = f"SELECT salesman FROM `allsales`;"
                cursor.execute(select_table)
                result = cursor.fetchall()
                print(result)
        elif select == "3":
            name = "Input name of customer: "
            with connection.cursor() as cursor:
                select_table = f"SELECT sum,customer FROM `allsales` WHERE customer={name};"
                cursor.execute(select_table)
                result = cursor.fetchall()
                print(result)
        elif select == "4":
            name = "Input name of salesman: "
            with connection.cursor() as cursor:
                select_table = f"SELECT customer,salesman FROM `allsales` WHERE salesman={name};"
                cursor.execute(select_table)
                result = cursor.fetchall()
                print(result)
        elif select == "5":
            name = "Input name of salesman: "
            r = 0
            with connection.cursor() as cursor:
                select_table = f"SELECT sum FROM `allsales` WHERE salesman={name};"
                cursor.execute(select_table)
                result = cursor.fetchall()
            for i in result:
                r += int(i['sum'])
            print(r)
        elif select == "6":
            name = "Input name of customer: "
            with connection.cursor() as cursor:
                select_table = f"SELECT list FROM `allsales` WHERE customer={name};"
                cursor.execute(select_table)
                result = cursor.fetchall()
                print(result)
        elif select == "7":
            with connection.cursor() as cursor:
                select_table = f"SELECT sum,customer FROM `allsales` WHERE sum>50;"
                cursor.execute(select_table)
                result = cursor.fetchall()
                print(result)
        else:
            print("Ooops")  
    finally:
        connection.close()

except:
    print("Smthing has gone wrong")