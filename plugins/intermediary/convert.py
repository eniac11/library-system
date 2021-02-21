from os import path

import sqlite3

# import pyodbc

# db = path.abspath("../../../data2000.mdb")
# connStr = (
#     r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
#     rf"DBQ={db};"
#     )
# conn = pyodbc.connect(connStr)

# cursor = conn.cursor()

# cursor.execute("select * from books where AccessNo='000001'")
   
# for row in cursor.fetchall():
#     print (row)

db = sqlite3.connect('db.sqlite3')
cur = db.cursor()

# sqlite_db_name = "intemediary.db3"

# sqlite_conn = sqlite3.connect(sqlite_db_name)
# sqlite_cur = sqlite_conn.cursor()

# # if not path.exists(sqlite_db_name):
# sqlite_cur.execute(
#         '''CREATE TABLE IF NOT EXISTS "Books"("Media Type" varchar(50),"Category" varchar(50),"Language" varchar(50),"AccessNo" varchar(50),"ISBN" varchar(50),"DeweyNo" varchar(10),"Location" varchar(9),"BookBarcode" varchar(15),"Restriction" varchar(20),"Grading" varchar(20),"PrimaryAuthor" varchar(100),"SecondaryAuthor" varchar(100),"Title1" varchar(150),"Title2" varchar(150),"Series" varchar(100),"Publisher" varchar(50),"Edition" varchar(50),"EditionDate" varchar(4),"Value" float,"AquisitionDate" varchar(20),"Annotation" longvarchar(65536),"Department" varchar(20),"Notes" longvarchar(65536),"Lent" bit,"Withdrawn" bit,"Issued" bit,"Stock" bit,"Reserve" bit,"ReturnDate" timestamp,"ReserveDate" timestamp,"ValAccessNo" varchar(7),"ValBookBarcode" varchar(15));''')
# sqlite_cur.execute('''
# CREATE TABLE IF NOT EXISTS "Aquisition"("Aquisition" varchar(20));''')
# sqlite_cur.execute('''
# CREATE TABLE IF NOT EXISTS "Borrowers"("StudentID" varchar(10),"ValStudentID" varchar(10),"Initials" varchar(15),"Surname" varchar(25),"Institution" varchar(50),"Standard" varchar(10),"Class" varchar(10),"Limit" smallint,"Granted" smallint,"Days" float,"Address1" varchar(50),"Address2" varchar(50),"Address3" varchar(50),"Address4" varchar(50),"Telephone" varchar(25),"Photo" longvarbinary);''')
# sqlite_cur.execute('''
# CREATE TABLE IF NOT EXISTS "Category"("MediaType" varchar(20));''')
# sqlite_cur.execute('''
# CREATE TABLE IF NOT EXISTS "DailyEntries"("AccessNo" varchar(50),"PrimaryAuthor" varchar(100),"Title1" varchar(150),"BookBarcode" varchar(15),"DeweyLocation" varchar(255),"Media Type" varchar(50),"Publisher" varchar(50),"Value" float,"AquisitionDate" varchar(20),"CurrentDate" timestamp);''')
# sqlite_cur.execute('''
# CREATE TABLE IF NOT EXISTS "Gradings"("Grading" varchar(20));''')
# sqlite_cur.execute('''
# CREATE TABLE IF NOT EXISTS "Keywords"("AccessNo" varchar(25),"Keywords" varchar(30),"PageNo" smallint);''')
# sqlite_cur.execute('''
# CREATE TABLE IF NOT EXISTS "Languages"("Language" varchar(20));''')
# sqlite_cur.execute('''
# CREATE TABLE IF NOT EXISTS "LoanHistory"("LoanDate" timestamp,"StudentID" varchar(10),"Initials" varchar(15),"Surname" varchar(25),"Institution" varchar(50),"Standard" varchar(15),"Class" varchar(15),"Media Type" varchar(20),"Category" varchar(20),"Language" varchar(20),"AccessNo" varchar(7),"DeweyNo" varchar(9),"Location" varchar(4),"BookBarcode" varchar(20),"Restriction" varchar(20),"PrimaryAuthor" varchar(100),"Title" varchar(150));''')
# sqlite_cur.execute('''
# CREATE TABLE IF NOT EXISTS "LoanReturn"("AccessNo" varchar(7),"BookBarcode" varchar(20),"StudentID" varchar(15),"Initials" varchar(15),"Surname" varchar(25),"Institution" varchar(50),"Standard" varchar(20),"Class" varchar(20),"Title1" varchar(150),"PrimaryAuthor" varchar(100),"Location" varchar(4),"DeweyNo" varchar(9),"Date" timestamp,"ReturnDate" timestamp,"IssueCategory" varchar(20),"Category" varchar(20),"Media Type" varchar(20));''')
# sqlite_cur.execute('''
# CREATE TABLE IF NOT EXISTS "Media Types"("Restriction" varchar(20));''')
# sqlite_cur.execute('''
# CREATE TABLE IF NOT EXISTS "Money Matters"("StudentID" varchar(15),"Credit" float,"Debit" float,"AccessNo" varchar(7),"Title" varchar(50),"Date" timestamp,"DaysOverdue" varchar(3));''')
# sqlite_cur.execute('''
# CREATE TABLE IF NOT EXISTS "Registration"("Institution" varchar(50),"Telephone" varchar(20),"Adress1" varchar(50),"Adress2" varchar(50),"Adress3" varchar(50),"Adress4" varchar(50),"SerialNo" varchar(15),"Barcode" bit,"FineFactor" float,"ReserveDays" smallint,"ExpireDate" timestamp,"Junior Primary Institution" bit,"Primary Institution" bit,"Secondary Institution" bit,"Tersiary Institution" bit,"Media Teacher" varchar(25),"Principal" varchar(25));''')
# sqlite_cur.execute('''
# CREATE TABLE IF NOT EXISTS "ReserveItems"("SerialNo" integer,"AccessNo" varchar(7),"BookBarcode" varchar(15),"StudentID" varchar(15),"Initials" varchar(15),"Surname" varchar(25),"Institution" varchar(50),"Standard" varchar(20),"Class" varchar(20),"Title1" varchar(150),"PrimaryAuthor" varchar(100),"Location" varchar(4),"DeweyNo" varchar(9),"Date" timestamp,"ReserveDate" timestamp,"Category" varchar(20),"Media Type" varchar(20),"Restriction" varchar(20));''')
# sqlite_cur.execute('''
# CREATE TABLE IF NOT EXISTS "Restrictions"("Restriction" varchar(20));''')
# sqlite_cur.execute('''
# CREATE TABLE IF NOT EXISTS "Spine Labels"("DeweyNo" varchar(50),"Location" varchar(50),"Category" varchar(50));''')
# sqlite_cur.execute('''
# CREATE TABLE IF NOT EXISTS "Standard"("Standard" varchar(20));''')
# sqlite_cur.execute('''
# CREATE TABLE IF NOT EXISTS "WithdrawalList"("AccessNo" varchar(7),"BookBarcode" varchar(50),"Title1" varchar(150),"PrimaryAuthor" varchar(100),"Location" varchar(4),"DeweyNo" varchar(9),"Date" timestamp,"Reason" varchar(55));''')
# sqlite_conn.commit()

TABLES = ['Aquisition', 'Books',
        'Borrowers',
        'Category', 'DailyEntries',
        'Gradings', 'Keywords',
        'Languages', 'LoanHistory',
        'LoanReturn', 'Media Types',
        'Money Matters', 'Registration',
        'ReserveItems', 'Spine Labels',
        'Standard', 'WithdrawalList']
# print(repr(TABLES[0]))
statement = 'SELECT * FROM "'+ TABLES[1] + '";'
# print(statement)

# cur_one = cur.fetchone()
# print(cur_one)
for val in cur.execute(statement):
        print(val)
# for table in TABLES:
    


