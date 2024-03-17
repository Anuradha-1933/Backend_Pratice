from fastapi import FastAPI
import imsert
app=FastAPI() #exposing your method over the broswer
nums=[]
@app.get("/")#this is a route that will be called when you hit this url in the browser
def greet():
    return "Hello,Anuradha Yadav"
# print(greet())

@app.get('/greetByName/{name}')
def getByName(name:str):
    return "Hello,Anuradha Yadav" +name

@app.get('/getNums')
def greetByName():
  return nums

@app.get('/updateNums/{num}')
def greetByName(num: int):
  nums.append(num)
  return nums


@app.get('/Student/{EmployeeID}')
def getStudentbyId(EmployeeID: int):
   database=imsert.get_db()
   cursorObject=database.cursor()
   cursorObject.execute( f"select *from Student where EmployeeID={EmployeeID}")
   rows=cursorObject.fetchall()
   return rows


# POST is used to send data to a server to create/update into database a resource
@app.post('/Student')
def UpdateStudentbyId(data: dict):
   database=imsert.get_db()
   cursorObject=database.cursor()
   EmployeeID= data['EmployeeID']
   FirstName=data['FirstName']
   LastName=data['LastName']
   Email=data['Email']
   AddressLine=data['AddressLine']
   City=data['City']
   cursorObject.execute( f"insert into Student values ({EmployeeID},'{FirstName}','{LastName}','{Email}','{AddressLine}','{City}')")
   database.commit()
   return getStudentbyId(EmployeeID)

# to update the database thruogh the put cammand
@app.put('/Student')
def updateCustomerById(data: dict):
  database = imsert.get_db()
  cursorObject = database.cursor()
  EmployeeID= data['EmployeeID']
  FirstName= data['FirstName']
  LastName = data['LastName']
  EmployeeID= data['EmployeeID']
  cursorObject.execute(f"update Student set FirstName='{FirstName}',LastName='{LastName}' where EmployeeID={EmployeeID}")
  database.commit()
  return getStudentbyId(EmployeeID)

# to delete particular touple in database
@app.delete('/Student/{EmployeeID}')
def deleteStudentbyId( EmployeeID: int):
  database=imsert.get_db()
  cursorObject=database.cursor()
  data=getStudentbyId(EmployeeID)
  if data:
    cursorObject.execute( f"delete from Student where EmployeeID={EmployeeID}")
    database.commit()
    return f"record with  EmployeeID={EmployeeID} hs been deleted"
  else:
    return f"there is No record found for the  EmployeeID={EmployeeID}"
  

  
 

