import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='CS485',
                             password='WinonaState',
                             db='CS485',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Search for Students
        userInput = input("Enter a student's first name to search for: ")
        sql = "SELECT * from Students where FirstName = " + "'" + userInput + "'"
        
        # execute the SQL command
        cursor.execute(sql)
        
        # get the results
        for result in cursor:
            print (result)
        
      
        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes. 
        # connection.commit()
        

finally:
    connection.close()
