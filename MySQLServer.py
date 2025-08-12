import mysql.connector

try:    
    with mysql.connector.connect(
        host = "localhost",
        user = "dbadmin",
        password = "p@SS098vc",
        # database = "alx_book_store"    
    ) as mysql_db:
        myCursor = mysql_db.cursor()
        myCursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")       
        print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as err:
    print(f"Error: {err}")    
    

