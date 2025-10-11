import tkinter as tk
import mysql.connector as mysql
import First_interface as fi
import main_window 
#-------------------------------------------------------------------------------
a = open("Access.txt")
for i in (a.read()).split(","):
    ii = i.split("=")
    if "host" in i :
        h = ii[1]
    elif "user" in i :
        u = ii[1]
    elif "password" in i :
        p = ii[1]
    elif "database" in i :
        d = ii[1]
a.close()
#-------------------------------------------------------------------------------

#--------------------------------------------------------------------------------

try:
    sql = mysql.connect(host=h, user=u, password=p, database=d)
    sql.close()
    main_window.mw()
except Exception:
                sql = mysql.connect(host=h, user=u, password=p)
                c = sql.cursor()
                c.execute("CREATE DATABASE " + d +";")
                c.execute("use " + d + ";")
                c.execute("""
                CREATE TABLE maintable (
                    Rollno INT,
                    Name VARCHAR(50),
                    FathersName VARCHAR(50),
                    MothersName VARCHAR(50),
                    Admnno INT PRIMARY KEY
                )""")
                
                c.execute("""
                CREATE TABLE attendance (
                    Rollno INT,
                    Name VARCHAR(50)
                )""")
                
                c.execute("""
                CREATE TABLE test (
                    Testname VARCHAR(10),
                    Physics INT,
                    Chemistry INT,
                    Maths INT,
                    English INT,
                    CS INT,
                    PHE INT
                )""")
                
                sql.commit()
                fi.swagat()
                sql.close()
