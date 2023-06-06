from flask import Flask
import pyodbc

app = Flask(__name__)

driver = '{ODBC Driver 18 for SQL Server}'
database = 'people'
server = 'tcp:assignment1.database.windows.net,1433'
username = "axb5500"
password = "Akash_Beer"
conn= pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor() #cursor 
cursor.execute('''Select * from all_day''')
check_username=cursor.fetchall()
print(check_username)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"