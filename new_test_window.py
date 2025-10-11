import tkinter as tk
import mysql.connector as Mysql

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
#---------------------------------------------------------------------------------------------------------------------
def ntw():
    global h,u,p,d
    mysql = Mysql.connect(host = h , user = u , password = p , database = d)
    sql = mysql.cursor()
    #-------------------------------------------------------------------------------

    win = tk.Tk()
    win.geometry("500x300")


    #---------------------------------------------------------------------------------------------------------------------

    mysql = Mysql.connect(host = h , user = u , password = p , database = d)
    sql = mysql.cursor()

    #---------------------------------------------------------------------------------------------------------------------

    NTF1 = tk.Frame(master = win , bg = "#032B44")
    NTF1.pack(fill = "both" , expand = True )

    #---------------------------------------------------------------------------------------------------------------------

    R = tk.Label(master = NTF1 , text = "Please Enter test name without using any special character including space " , bg = "#032B44" , fg = "#3A3D41" , font = ("Arial",10,"bold"))
    R.pack() 

    #---------------------------------------------------------------------------------------------------------------------

    NTL = tk.Label(master = NTF1 , text = "Enter test name : " , bg = "#B2E6CE" , fg = "#3A3D41" , font = ("Arial",16,"bold"))
    NTL.pack(side = tk.LEFT)

    #---------------------------------------------------------------------------------------------------------------------

    NTE = tk.Entry(master = NTF1 )
    NTE.pack(side = tk.LEFT , padx = 4)

    #---------------------------------------------------------------------------------------------------------------------

    NTF2 = tk.Frame(master = win  , bg = "#032B44")
    NTF2.pack(fill = "both" , expand = True )

    #---------------------------------------------------------------------------------------------------------------------

    FML = tk.Label(master = NTF2 , text = "Enter full marks of - " , bg = "#B2E6CE" , fg = "#3A3D41"  , font = ("Arial",12,"bold"))
    FML.pack()

    #---------------------------------------------------------------------------------------------------------------------

    NTEF1 = tk.Frame(master = win  , bg = "#032B44")
    NTEF1.pack(fill = "both" , expand = True )

    #---------------------------------------------------------------------------------------------------------------------

    NTEF2 = tk.Frame(master = win  , bg = "#032B44")
    NTEF2.pack(fill = "both" , expand = True ) 

    #---------------------------------------------------------------------------------------------------------------------

    NTEF3 = tk.Frame(master = win  , bg = "#032B44")
    NTEF3.pack(fill = "both" , expand = True )

    #---------------------------------------------------------------------------------------------------------------------
    PML = tk.Label(master  = NTEF1 , text = "Physics" , bg = "#B2E6CE"  , fg = "#3A3D41" , width = 8)
    PML.pack(side = tk.LEFT , padx = 10)

    #---------------------------------------------------------------------------------------------------------------------

    PME = tk.Entry(master = NTEF1)
    PME.pack(side = tk.LEFT)

    #---------------------------------------------------------------------------------------------------------------------

    CME = tk.Entry(master = NTEF1)
    CME.pack(side = tk.RIGHT , padx = 10)

    #---------------------------------------------------------------------------------------------------------------------

    CML = tk.Label(master  = NTEF1 , text = "Chemistry" , bg = "#B2E6CE"  , fg = "#3A3D41" , width = 8)
    CML.pack(side = tk.RIGHT)

    #---------------------------------------------------------------------------------------------------------------------

    MML = tk.Label(master  = NTEF2 , text = "Maths" , bg = "#B2E6CE"  , fg = "#3A3D41" , width = 8)
    MML.pack(side = tk.LEFT , padx = 10)

    #---------------------------------------------------------------------------------------------------------------------

    MME = tk.Entry(master = NTEF2)
    MME.pack(side = tk.LEFT)

    #---------------------------------------------------------------------------------------------------------------------

    EME = tk.Entry(master = NTEF2)
    EME.pack(side = tk.RIGHT , padx = 10)

    #---------------------------------------------------------------------------------------------------------------------

    EML = tk.Label(master  = NTEF2 , text = "English" , bg = "#B2E6CE"  , fg = "#3A3D41" , width = 8)
    EML.pack(side = tk.RIGHT)

    #---------------------------------------------------------------------------------------------------------------------

    CSML = tk.Label(master  = NTEF3 , text = "CS" , bg = "#B2E6CE"  , fg = "#3A3D41" , width = 8)
    CSML.pack(side = tk.LEFT , padx = 10)

    #---------------------------------------------------------------------------------------------------------------------

    CSME = tk.Entry(master = NTEF3)
    CSME.pack(side = tk.LEFT)

    #---------------------------------------------------------------------------------------------------------------------

    PHEME = tk.Entry(master = NTEF3)
    PHEME.pack(side = tk.RIGHT , padx = 10)

    #---------------------------------------------------------------------------------------------------------------------

    PHEML = tk.Label(master  = NTEF3 , text = "P.H.E." , bg = "#B2E6CE" , fg = "#3A3D41" , width = 8)
    PHEML.pack(side = tk.RIGHT)

    #---------------------------------------------------------------------------------------------------------------------

    global MW
    MW = ""
    def adb():
        ml =[]
        global MW
        while MW :
            MW.destroy()
            MW = ""
        test = NTE.get()
        ml.append(test)
        for i in (PME,CME,MME,EME,CSME,PHEME) :
            m = i.get()
            if m.isdigit() != True :
                MW = tk.Label(master = R , text = "Please enter valid marks !!!")
                MW.pack()
                break
            ml.append(int(m))
        if MW == "" :
            win.destroy()
        cmd = "insert into test values" + str(tuple(ml)) + ";"
        sql.execute(cmd)
        mysql.commit()
        cmd = "create table " + test + " (Rollno INT ,Name Varchar(50), Physics INT DEFAULT'0', Chemistry INT DEFAULT'0', Maths INT DEFAULT'0', English INT DEFAULT'0', CS INT DEFAULT'0', PHE INT DEFAULT'0' , Percentage INT DEFAULT'0');"
        sql.execute(cmd)
        cmd = "insert into " + test.lower() + " (Rollno,Name) select Rollno,Name from maintable;"
        sql.execute(cmd)
        mysql.commit()
    #---------------------------------------------------------------------------------------------------------------------

    def back():
        mysql.close()
        win.destroy()

        
    #---------------------------------------------------------------------------------------------------------------------

    NTBF = tk.Frame(master = win  , bg = "#032B44")
    NTBF.pack(fill = "both" , expand = True )

    #---------------------------------------------------------------------------------------------------------------------

    BB = tk.Button(master = NTBF , text = "Back" , command = back ,  bg = "#B2E6CE" , fg = "#3A3D41" , width = 5 , height = 1)
    BB.pack(side = tk.RIGHT , padx = 40 )

    #---------------------------------------------------------------------------------------------------------------------

    ADB = tk.Button(master = NTBF , text = "Add" , command = adb , bg = "#B2E6CE" , fg = "#3A3D41"  , width = 5 , height = 1)
    ADB.pack(side = tk.RIGHT , padx = 40)

    #----------------------------------------------------------------------------------------------------------------------
    win.mainloop()

