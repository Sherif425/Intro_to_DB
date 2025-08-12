import mysql.connector

try:    
    with mysql.connector.connect(
        host = "localhost",
        user = "dbadmin",
        password = "p@SS098vc",
        # database = "alx_book_store"    
    ) as mysql_db:
        myCursor = mysql_db.cursor()
        
        with open('alx_book_store.sql', 'r') as file:
            sql_script =file.read()
            print(sql_script)
            
        for result in myCursor.execute(sql_script, multi=True):
            print(result)
            
        print("SQL script executed successfully!")
except mysql.connector.Error as err:
    print(f"Error: {err}")    
    
finally:
    if 'mysql_db' in locals() and mysql_db.is_connected():
        myCursor.close()
        mysql_db.close()
        print("MySQL connection is closed.")    
