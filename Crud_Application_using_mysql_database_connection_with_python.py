import mysql.connector

#Connect database with python
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Movies_Database"
)

while True:
    print("********************************************************")
    print("1:- CREATE DATABASE\n2:- GET LIST OF DATABASE\n3:- CREATE TABLE\n4: GET LIST OF TABLE\n5:-INSERT RECORD INTO TABLE\n6: GET ALL RECORD FROM TABLE\n7: GET SPECIFIC RECORD FROM TABLE\n8:- EXIT CODE")
    print("********************************************************")
    ch=int(input())
    if ch==1:
        #create Database
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE Movies_Database")
        print("Database created Successfully")
    
    elif ch==2:
        #Get list of Database
        mycursor = mydb.cursor()
        mycursor.execute("SHOW DATABASES")
        for x in mycursor:
            print(x) 

    elif ch==3:
        #Create Table
        mycursor = mydb.cursor()
        mycursor.execute("CREATE TABLE Movies (name_of_movie VARCHAR(255), name_of_lead_actor VARCHAR(255), name_of_lead_actress VARCHAR(255),year_of_release BIGINT(10),name_of_director VARCHAR(255))")
        print("Table Created Successfully")
    
    elif ch==4:
        #Show Tables 
        mycursor = mydb.cursor()
        mycursor.execute("SHOW TABLES")
        for x in mycursor:
            print(x) 

    elif ch==5:
        #Insert Data into movies Table
        mycursor = mydb.cursor()
        sql = "INSERT INTO movies(name_of_movie, name_of_lead_actor, name_of_lead_actress, year_of_release, name_of_director) VALUES (%s, %s, %s, %s, %s)"
        val = ("Bahubali", "Prabhas","tamanna",2018,"rajamauli")
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    
    elif ch==6:
        #Get Record From Table
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM movies")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
    elif ch==7:
        #   Get Specific Record using select query
        mycursor = mydb.cursor()
        sql = "SELECT * FROM movies WHERE name_of_lead_actor='yash'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

    elif ch==8:
        print("Execution Stoped")
        break
    else:
        print("Invalid Choice")


