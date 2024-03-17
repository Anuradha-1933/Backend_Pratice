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


def get_db():
    database=mysql.connector.connect(**confi) 
    return database

