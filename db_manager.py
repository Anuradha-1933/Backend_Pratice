import mysql.connector

database = mysql.connector.connect( 

    host = "localhost",

    user = "root",

    passwd="12345678",
    database="Anuradha"

)

print(database)

cursorObject = database.cursor() 
# cursorObject.execute("CREATE DATABASE test3") for creating a data a database  
# role of cursorObject is an active connection to that database
# fetchall simply means select *all from datababe
cursorObject.execute("SELECT * FROM Anuradha")
# cursorObject.execute("INSERT INTO Anuradha() VALUES (1, 'radha', 'pal', 'yanu231@gmail.com', '123', 'Chennai')")
            # .filter("City","Mumbai")
rows=cursorObject.fetchall()
print(rows)
for row in rows:
    print(row[1])
database.close()
# try:
#     cursorObject = database.cursor() 
#     cursorObject.execute("SELECT * FROM Anuradha")
#     rows=cursorObject.fetchall()
#     print(rows)
#     for row in rows:
#         print(row[1])
# except Exception as e:
#     print(e)
# finally:
#     database.close()

# unpackking operater 
# param={"p":100,"p2":200}
# def exa_fun(p1,p2):
#     print(f"p1:{p1},p2:{p2}")
# exa_fun(200,300)



    
