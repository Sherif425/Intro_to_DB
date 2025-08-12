#This version uses the new mysql-connector that reads the multi statement sql scripts without
#the need for multi=True keyword in execute command
import mysql.connector

try:
    with mysql.connector.connect(
        host="localhost",
        user="dbadmin",
        password="p@SS098vc"
    ) as mysql_db:
        myCursor = mysql_db.cursor()
        
        with open('alx_book_store.sql', 'r') as file:
            sql_script = file.read()
            
        # Execute the first statement
        myCursor.execute(sql_script)
        
        # Loop to process results for all statements
        while myCursor.nextset():
            # Process the results of the current statement here
            for result in myCursor:
                print(result)
            
        print("SQL script executed successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")
    
# The 'with' statement handles closing the connection, so a 'finally' block is not strictly necessary here.