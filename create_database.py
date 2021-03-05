import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

c = conn.cursor()

c.execute("CREATE DATABASE IF NOT Exists smartroster")
conn.commit()
conn.close()

cnx = mysql.connector.connect(user='root',
                             password='',
                             host='localhost',
                             database='smartroster')
cursor =cnx.cursor()

def executeScriptsFromFile(filename):
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        try:
            if command.strip() != '':
                cursor.execute(command)
        except :
            pass

executeScriptsFromFile('SQLImportFiles/smartroster_nurses.sql')
executeScriptsFromFile('SQLImportFiles/smartroster_patients.sql')
executeScriptsFromFile('SQLImportFiles/smartroster_patient_nurse_assignments.sql')
executeScriptsFromFile('SQLImportFiles/smartroster_users.sql')    

executeScriptsFromFile('SQLImportFiles/smartroster_reference_page.sql')
conn.commit()
conn.close()