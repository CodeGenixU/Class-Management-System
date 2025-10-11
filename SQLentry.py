import mysql.connector as Mysql

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

mysql = Mysql.connect(host = h , user = u , password = p , database = d)
sql = mysql.cursor()

with open("SQL.txt","r") as fh :
    s = " "
    while s :
        s = fh.readline()
        if "insert" in s or "update" in s :
            sql.execute(s)
            mysql.commit()
        elif "select" in s :
            sql.execute(s)
            sql.fetchall()
        else :
            sql.execute(s)

mysql.close()

print("Data done!!")
