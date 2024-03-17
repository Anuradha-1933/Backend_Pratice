import mysql.connector

# database = mysql.connector.connect( 
# database connnection configureation
confi={
     "host" : "localhost",
     "port":"3306",
    "user": "root",
    "passwd":"12345678",
    "database":"Student"
}
try:
    database=mysql.connector.connect(**confi) #unpacking function ** operator
# )
    print(database)
    cursorObject = database.cursor() 
    cursorObject.execute("SELECT * FROM Student")
    rows=cursorObject.fetchall()
    print(rows)
    for row in rows:
        print(row[1])
# insert new record to table
    cursorObject.execute("insert into Student values(1,'Anu','yadav','yanu@123.gmail.com','234 main road stv','chennai')")
    database.commit()
    insert_sql="INSERT INTO Student (FirstName, LastName, Email, AddressLine, City) values (%c,%c,%c,%c)"
    insert_val=(2,"Asshi","Singh","yanur345@gmail.com","123dfe","Delhi")
    cursorObject.execute(insert_sql,insert_val)

except Exception as e:
    print(e)
finally:
    database.close()

def get_db():
    database=mysql.connector.connect(**confi) 
    return database

