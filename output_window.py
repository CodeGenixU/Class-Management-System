import tkinter as tk
import mysql.connector as Mysql
import texttable as tt
import matplotlib.pyplot as mlt
import csv
import main_window
#-------------------------------------------------------------------------------
a = open("Access.txt")
global h,u,p,d
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
#------------------------------------------------------------------------------------
def TMD(nam) :
    mysql = Mysql.connect(host = h , user = u , password = p , database = d)
    sql = mysql.cursor()
    name = str(nam)
    sql.execute("desc " + name + " ;")
    sd = sql.fetchall()
    l = []
    for i in sd :
        l.append(i[0])
    table = tt.Texttable()
    table.header(l)
    sql.execute("select * from " + name + " order by RollNo;")
    data = " "
    while data :
        data = sql.fetchone()
        if data != None :
            table.add_row(list(data))
    sql.close()
    mysql.close()
    return table.draw()
    
#------------------------------------------------------------------------------------
def TMF(name):
    mysql = Mysql.connect(host = h , user = u , password = p , database = d)
    sql = mysql.cursor()
    f = name + ".csv"
    with open(f,"w") as fh :
        c = csv.writer(fh)
        sql.execute("desc " + name + " ;")
        sd = sql.fetchall()
        l = []
        for i in sd :
            l.append(i[0])
        c.writerow(l)
        sql.execute("select * from " + name + " order by RollNo ;")
        data = " "
        while data :
            data = sql.fetchone()
            if data != None :
                c.writerow(data)
    sql.close()
    mysql.close()
    wi = tk.Tk()
    L = tk.Label(wi , text = "Export complete!!"  )
    L.pack()
    def quit():
        wi.destroy()
    B = tk.Button(wi , text = "Close" , command = quit)
    B.pack()
#-----------------------------------------------------------------------------------
def TD(name):
    wi = tk.Tk()
    L = tk.Label(wi , text = TMD(name) , font = ("Courier",12) )
    L.pack()
    def quit():
        wi.destroy()
    B1 = tk.Button(wi , text = "Close" , command = quit)
    B1.pack()
    B2 = tk.Button(wi , text = "Export" , command = lambda : TMF(name))
    B2.pack()
    wi.mainloop()
#-----------------------------------------------------------------------------------
def ow():
    mysql = Mysql.connect(host = h , user = u , password = p , database = d)
    sql = mysql.cursor()
    #------------------------------------------------------------------------------------
    win = tk.Tk()
    win.geometry("500x300")
    #------------------------------------------------------------------------------------
    F1 = tk.Frame(win , bg = "#FFA07A" )
    F1.pack(fill = "both" , expand = True)
    #------------------------------------------------------------------------------------
    F2 = tk.Frame(win , bg = "#FFA07A" )
    F2.pack(fill = "both" , expand = True)
    #------------------------------------------------------------------------------------
    F31 = tk.Frame(win , bg = "#FFA07A" )
    F31.pack(fill = "both" , expand = True)
    #------------------------------------------------------------------------------------
    F32 = tk.Frame(win , bg = "#FFA07A" )
    F32.pack(fill = "both" , expand = True)
    #------------------------------------------------------------------------------------
    F33 = tk.Frame(win , bg = "#FFA07A" )
    F33.pack(fill = "both" , expand = True)
    #------------------------------------------------------------------------------------
    F34 = tk.Frame(win , bg = "#FFA07A" )
    F34.pack(fill = "both" , expand = True)
    #------------------------------------------------------------------------------------
    F4 = tk.Frame(win , bg = "#FFA07A" )
    F4.pack(fill = "both" , expand = True)
    #------------------------------------------------------------------------------------
    F5 = tk.Frame(win , bg = "#FFA07A" )
    F5.pack(fill = "both" , expand = True)   
    #------------------------------------------------------------------------------------
    MT = tk.Button(F1, text = "Main Table" , command = lambda : TD("maintable") , bg = "#FFD7BE" , fg = "#03A9F4" )
    MT.pack(side = tk.LEFT , padx = 30 )
    #--------------------------------------------------------------------------------------
    def ATD():
        M = []
        sql.execute("desc attendance ;")
        sd = sql.fetchall()
        tD = len(sd) - 2
        l1 = []
        for i in sd :
            l1.append(i[0])
        l = l1[0:2]
        l.append(f"No. of present days({tD})")
        table = tt.Texttable()
        table.header(l)
        M.append(l)
        sql.execute("select * from attendance order by RollNo ;")
        data = " "
        while data :
            data = sql.fetchone()
            P = 0
            if data != None :
                for i in data[2:]:
                    if i == "P":
                        P +=1
                k = list(data[0:2])
                k.append(P)
                M.append(k)
                table.add_row(k)
        Table = table.draw()
        wi = tk.Tk()
        L = tk.Label(wi , text = Table , font = ("Courier",12) )
        L.pack()
        def quit():
            wi.destroy()
        B1 = tk.Button(wi , text = "Close" , command = quit)
        B1.pack()
        def Ex(M):
            with open("attendance.csv","w") as fh :
                c = csv.writer(fh)
                c.writerows(M)
            wi = tk.Tk()
            L = tk.Label(wi , text = "Export complete!!"  )
            L.pack()
            def quit():
                wi.destroy()
            B = tk.Button(wi , text = "Close" , command = quit)
            B.pack()
            
        B2 = tk.Button(wi , text = "Export" , command = lambda : Ex(M) )
        B2.pack()
        wi.mainloop()
    #--------------------------------------------------------------------------------------
    AT = tk.Button(F1 , text = "Attendance Table" , command = ATD , bg = "#FFD7BE" , fg = "#03A9F4" )
    AT.pack(side = tk.RIGHT , padx = 30 )
    #--------------------------------------------------------------------------------------
    L = tk.Label(F2 , text = "Enter the roll no. of the student you want to search " , bg = "#FFD7BE" , fg = "#03A9F4" )
    L.pack(side = tk.LEFT , padx = 3)
    #----------------------------------------------------------------------------------------
    E = tk.Entry(F2 )
    E.pack(side = tk.LEFT)
    #-----------------------------------------------------------------------------------------
    def S():
        
        r = E.get()
        E.delete(0,tk.END)
        if r.isdigit() != True :
            pass
        DL = []
        sql.execute("desc maintable ;")
        data = []
        sqlr = sql.fetchall()
        for i in sqlr :
            data.append(i[0])
        sql.execute("select * from maintable where Rollno = '" + str(r) + "' ;")
        sqlr = sql.fetchall()
        d = dict(zip(data,sqlr[0]))
        for i in d :
            s = i + " : " + str(d[i])
            DL.append(s)
        data = []
        sql.execute("select * from test ;")
        tl = sql.fetchall()
        for i in tl :
            k = "select * from " + i[0].lower() + " where Rollno = " + str(r) + " ;"
            sql.execute(k)
            sqlr = sql.fetchall()
            if sqlr != [] :
                sqlr = list(sqlr[0][1:])
                sqlr[0] = i[0]
                data.append(sqlr)
        l = []
        sql.execute("desc test ;")
        for i in sql.fetchall() :
            l.append(i[0])
        table = tt.Texttable()
        l.append("Percentage")
        table.header(l)
        for i in data :
            table.add_row(i)
            mlt.plot(l[1:],i[1:], label = i[0])
        Table = table.draw()
        wi = tk.Tk()
        for i in DL :
            L = tk.Label(wi , text = i )
            L.pack()
        L = tk.Label(wi , text = Table , font = ("Courier",12))
        L.pack()
        def quit():
                wi.destroy()
        B = tk.Button(wi , text = "Close" , command = quit)
        B.pack()
        def Exp(DL,Table):
            x = "save.txt"
            with open(x,"w") as fh :
                for i in DL :
                    fh.write(i)
                    fh.write("\n")
                fh.write(Table)
        B2 = tk.Button(wi , text = "Export" , command = lambda : Exp(DL,Table) )
        B2.pack()
        mlt.legend()
        mlt.show()
        
    #------------------------------------------------------------------------------------------
    SB = tk.Button(F2 , text = "Search" , command = S , bg = "#FFD7BE" , fg = "#03A9F4" )
    SB.pack(side = tk.RIGHT , padx = 2 )
    #---------------------------------------------------------------------------------------------
    L = tk.Label(F31 , text = "Select the test which you want to view :- " , bg = "#FFD7BE" , fg = "#03A9F4" )
    L.pack()
    #---------------------------------------------------------------------------------------------
    sql.execute("select Testname from test")
    buttons = sql.fetchall()

    for i in buttons:
        z = i[0].lower()
        j = tk.Button(F32 , text = i[0] , command = lambda : TD(z) , bg = "#FFD7BE" , fg = "#03A9F4" , font = ("Arial",10,"bold"))
        j.pack(side = tk.LEFT , padx = 20 )
    #----------------------------------------------------------------------------------------------
    L = tk.Label(F33 , text = "Select the test which you want to analyse :- " , bg = "#FFD7BE" , fg = "#03A9F4" )
    L.pack()
    #-----------------------------------------------------------------------------------------------
    def TA(tes):
        sql.execute("desc test ;")
        data = sql.fetchall()
        l = [""]
        for i in data[1:] :
            l.append(i[0])
        d = [["Average"],["Maximum"],["No. of students of above average"],["No. of students passed"]]
        sql.execute("select * from test where Testname = '" + tes.upper() + "' ;")
        tm = []
        w = sql.fetchall()
        for i in w[0][1:] :
            z = (i*0.33)//1
            tm.append(z)
        r = 0
        for i in l[1:] :
            sql.execute("select avg(" + i + ") '" + i + "' from " + tes + " ;")
            x = sql.fetchall()
            d[0].append(x[0][0])
            sql.execute("select max(" + i + ") '" + i + "' from " + tes + " ;")
            x = sql.fetchall()
            d[1].append(x[0][0])
            sql.execute("select count(*) '" + i + "' from " + tes + " where " + i + " >= " + str(d[0][-1]) + " ;")
            x = sql.fetchall()
            d[2].append(x[0][0])
            cmd = "select count(*) '" + i + "' from " + tes + " where " + i + " >= " + str(tm[r]) + " ;"
            sql.execute(cmd)
            x = sql.fetchall()
            d[3].append(x[0][0])
            r += 1
        table = tt.Texttable()
        table.header(l)
        for i in d :
            table.add_row(i)
        T = table.draw()
        wi = tk.Tk()
        L = tk.Label(wi , text = T , font = ("Courier",12) )
        L.pack()
        def quit():
            wi.destroy()
        B1 = tk.Button(wi , text = "Close" , command = quit)
        B1.pack()
        wi.mainloop()
    #---------------------------------------------------------------------------------------------
    sql.execute("select Testname from test ;")
    buttons = sql.fetchall()

    for i in buttons:
        z = i[0].lower()
        i = tk.Button(F34 , text = i[0] , command = lambda : TA(z) , bg = "#FFD7BE" , fg = "#03A9F4" , font = ("Arial",10,"bold"))
        i.pack(side = tk.LEFT , padx = 20 )
    #-------------------------------------------------------------------------------------------------
    def Back() :
        mysql.close()
        win.destroy()
        main_window.mw()
    #-------------------------------------------------------------------------------------------------
    BB = tk.Button(F5 , text = "Back" , command = Back , bg = "#FFD7BE" , fg = "#03A9F4" )
    BB.pack()
    win.mainloop()
