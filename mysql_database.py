import mysql.connector

def mysql_db():
    connection = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    passwd= 'password',
                    database='houses'
                )
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM houses.house')
    records = cursor.fetchall()
    return records
