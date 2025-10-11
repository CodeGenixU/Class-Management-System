import tkinter as tk
import mysql.connector as Mysql
import main_window
import new_test_window
#---------------------------------------------------------------------------------------------------------------------
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
def tw():
    global h,u,p,d
    mysql = Mysql.connect(host = h , user = u , password = p , database = d)
    sql = mysql.cursor()
    #-------------------------------------------------------------------------------

    win = tk.Tk()
    win.geometry("600x400")
    #---------------------------------------------------------------------------------------------------------------------
    def at():
        new_test_window.ntw()
    #---------------------------------------------------------------------------------------------------------------------
    FF = tk.Frame(master = win , bg = "#8B9467" )
    FF.pack(fill = 'both' , expand = True)
    #---------------------------------------------------------------------------------------------------------------------
    AT = tk.Button(master = FF , text = "Add Test" , command = at , bg = "#8B9467" , font = ("Arial",8,"bold"))
    AT.pack(side = tk.RIGHT , padx = 20)
    #---------------------------------------------------------------------------------------------------------------------
    TLF = tk.Frame(master = win , bg = "#8B9467" )
    TLF.pack(fill = 'both' , expand = True)
    #---------------------------------------------------------------------------------------------------------------------

    #---------------------------------------------------------------------------------------------------------------------
    TBF = tk.Frame(master = win , bg = "#8B9467" )
    TBF.pack( fill = 'both' , expand = True)
    #---------------------------------------------------------------------------------------------------------------------
    
        
    #---------------------------------------------------------------------------------------------------------------------
    R = tk.Frame(master = win , bg = "#8B9467")
    R.pack( fill = 'both' , expand = True)
    #---------------------------------------------------------------------------------------------------------------------
    TM1 = tk.Frame(master = win , bg = "#8B9467")
    TM1.pack( fill = 'both' , expand = True)
    #---------------------------------------------------------------------------------------------------------------------
    TM2 = tk.Frame(master = win , bg = "#8B9467")
    TM2.pack( fill = 'both' , expand = True)
    #---------------------------------------------------------------------------------------------------------------------
    TM3 = tk.Frame(master = win , bg = "#8B9467")
    TM3.pack( fill = 'both' , expand = True)
    #---------------------------------------------------------------------------------------------------------------------
    PML = tk.Label(master  = TM1 , text = "Physics" , bg = "#F5F5DC" , fg = "#00008b" , width = 8)
    PML.pack(side = tk.LEFT , padx = 10)
    #---------------------------------------------------------------------------------------------------------------------
    PME = tk.Entry(master = TM1)
    PME.pack(side = tk.LEFT)
    #---------------------------------------------------------------------------------------------------------------------
    CME = tk.Entry(master = TM1)
    CME.pack(side = tk.RIGHT , padx = 10)
    #---------------------------------------------------------------------------------------------------------------------
    CML = tk.Label(master  = TM1 , text = "Chemistry" , bg = "#F5F5DC" , fg = "#00008b" , width = 8)
    CML.pack(side = tk.RIGHT)
    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    MML = tk.Label(master  = TM2 , text = "Maths" , bg = "#F5F5DC" , fg = "#00008b" , width = 8)
    MML.pack(side = tk.LEFT , padx = 10)
    #---------------------------------------------------------------------------------------------------------------------
    MME = tk.Entry(master = TM2)
    MME.pack(side = tk.LEFT)
    #---------------------------------------------------------------------------------------------------------------------
    EME = tk.Entry(master = TM2)
    EME.pack(side = tk.RIGHT , padx = 10)
    #---------------------------------------------------------------------------------------------------------------------
    EML = tk.Label(master  = TM2 , text = "English" , bg = "#F5F5DC" , fg = "#00008b" , width = 8)
    EML.pack(side = tk.RIGHT)
    #---------------------------------------------------------------------------------------------------------------------
    CSML = tk.Label(master  = TM3 , text = "CS" , bg = "#F5F5DC" , fg = "#00008b" , width = 8)
    CSML.pack(side = tk.LEFT , padx = 10)
    #---------------------------------------------------------------------------------------------------------------------
    CSME = tk.Entry(master = TM3)
    CSME.pack(side = tk.LEFT)
    #---------------------------------------------------------------------------------------------------------------------
    PHEME = tk.Entry(master = TM3)
    PHEME.pack(side = tk.RIGHT , padx = 10)
    #---------------------------------------------------------------------------------------------------------------------
    PHEML = tk.Label(master  = TM3 , text = "P.H.E." , bg = "#F5F5DC" , fg = "#00008b" , width = 8)
    PHEML.pack(side = tk.RIGHT)
    #---------------------------------------------------------------------------------------------------------------------
    RL = tk.Label(master = R , text = "Enter Roll. no. of student : " , bg = "#F5F5DC" , fg = "#00008b")
    RL.pack(side = tk.LEFT)
    #---------------------------------------------------------------------------------------------------------------------
    RE = tk.Entry(master = R)
    RE.pack(side = tk.LEFT , padx = 10)
    #---------------------------------------------------------------------------------------------------------------------
    global RW
    global MW
    RW = ""
    MW = ""
    def rb():
        ml =[]
        global RW
        global MW
        global test
        while RW :
            RW.destroy()
            RW = ""
        while MW :
            MW.destroy()
            MW = ""
        roll = RE.get()
        if int(roll.isdigit()) != 1:
            RW = tk.Label(master = R , text = "Please enter valid Roll no. !!!")
            RW.pack()
        
        sql.execute("select * from test where Testname = '" + test + "' ;")
        FM = sql.fetchall()
        n = 1
        for i in (PME,CME,MME,EME,CSME,PHEME) :
            m = i.get()
            if (m.isdigit() != True) or (int(m) >  FM[0][n]):
                RW = tk.Label(master = R , text = "Please enter valid marks !!!")
                RW.pack()
                break
            ml.append(m)
            n += 1
        total_marks = sum(FM[0][1:7])
        marks = 0
        for i in ml :
            marks += int(i)
        ml.append((marks/total_marks)*100)
        cmd = "update " + test + " set Physics = " + str(ml[0]) + " ," + "Chemistry = " + str(ml[1]) + " ," + "Maths = " + str(ml[2]) + " ," + "English = " + str(ml[3]) + " ," + "CS = " + str(ml[4]) + " ," + "PHE = " + str(ml[5]) + " ," + "Percentage = " + str(ml[6])  + " where Rollno  = " + roll + ";"
        sql.execute(cmd)
        mysql.commit()
        for i in (PME,CME,MME,EME,CSME,PHEME,RE) :
            i.delete(0,tk.END)
        sql.execute("select * from " + test + " order by Rollno ;")
        sql.fetchall()
    #---------------------------------------------------------------------------------------------------------------------
    def back():
        mysql.close()
        win.destroy()
        main_window.mw()
    #---------------------------------------------------------------------------------------------------------------------
    def reset():
        for i in (PME,CME,MME,EME,CSME,PHEME,RE) :
            i.delete(0,tk.END)
    #---------------------------------------------------------------------------------------------------------------------
    LF = tk.Frame(master = win , bg = "#8B9467")
    LF.pack( fill = 'both' , expand = True)
    #---------------------------------------------------------------------------------------------------------------------
    BACK = tk.Button(master = LF , text = "BACK" , command = back , bg = "#F5F5DC" , fg = "#00008b")
    BACK.pack(side = tk.RIGHT , padx = 20)
    #---------------------------------------------------------------------------------------------------------------------
    

    global L
    global test
    L = ""
    test = ""

    def B(s):
        global L
        global test
        while L :
            L.destroy()
            L = ""
        L = tk.Label(master = TLF , text = s , bg = "#F5F5DC" , fg = "#00008b" , font = ("Arial",28,"italic","bold") )
        L.pack(side = tk.BOTTOM)
        test = s
        RB = tk.Button(master = LF , text = "ENTER" , command = rb , bg = "#F5F5DC" , fg = "#00008b")
        RB.pack(side = tk.RIGHT , padx = 20)

    sql.execute("select Testname from test ;")
    buttons = sql.fetchall()

    for i in buttons:
        i = tk.Button(master = TBF , text = i[0] , command = lambda v = i[0] : B(v) , bg = "#F5F5DC" , fg = "#00008b" , font = ("Arial",10,"bold"))
        i.pack(side = tk.LEFT , padx = 60//len(buttons))



    #-----------------------------------------------------------------------------------------------------------------

    #---------------------------------------------------------------------------------------------------------------------
    RESET = tk.Button(master = LF , text = "RESET" , command = reset , bg = "#F5F5DC" , fg = "#00008b")
    RESET.pack(side = tk.LEFT , padx = 20)


    win.mainloop()
