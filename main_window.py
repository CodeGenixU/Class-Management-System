import tkinter as tk
import mysql.connector as Mysql
import test_window
import output_window
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

#-------------------------------------------------------------------------------
def mw():
    global h,u,p,d
    try:
        mysql = Mysql.connect(host = h , user = u , password = p , database = d)
        sql = mysql.cursor()
    except Mysql.Error as err:
        if err.errno == 1049:  # Unknown database
            print(f"Database '{d}' not found. Please run the main application first to create the database.")
            return
        else:
            print(f"Database connection error: {err}")
            return
    #-------------------------------------------------------------------------------

    win = tk.Tk()
    win.geometry("1000x600")
    win.title("Main Window")
    #-------------------------------------------------------------------------------
    F1 = tk.Frame(master = win , bg = "#FFA500")
    F1.pack(fill = "both" , expand = True )
    #-------------------------------------------------------------------------------
    LF1 = tk.Label(master = F1 , text = "Input centre" , bg = "#FFA500" , fg = "red" , font = ("Arial",24,"bold","underline"))
    LF1.pack(fill = "both" , expand = True)
    #-------------------------------------------------------------------------------
    F11 = tk.Frame(master = win , bg = "#FFA500")
    F11.pack(fill = "both" , expand = True )
    #-------------------------------------------------------------------------------
    LF112 = tk.Label(master = F11 , text = "Name" , bg = "#FFA500" , fg = "red" , font = ("Arial",12))
    LF112.pack(side = tk.LEFT )
    #-------------------------------------------------------------------------------
    E1 = tk.Entry(master = F11 )
    E1.pack(side = tk.LEFT , padx = 30)
    #-------------------------------------------------------------------------------
    LF113 = tk.Label(master = F11 , text = "Father 's Name" , bg = "#FFA500" , fg = "red" , font = ("Arial",12))
    LF113.pack(side = tk.LEFT , padx = 30)
    #-------------------------------------------------------------------------------
    E2 = tk.Entry(master = F11)
    E2.pack(side = tk.LEFT , padx = 30)
    #-------------------------------------------------------------------------------
    LF114 = tk.Label(master = F11 , text = "Mother 's Name" , bg = "#FFA500" , fg = "red" , font = ("Arial",12))
    LF114.pack(side = tk.LEFT , padx = 30)
    #-------------------------------------------------------------------------------
    E3 = tk.Entry(master = F11 )
    E3.pack(side = tk.LEFT)
    #-------------------------------------------------------------------------------
    F12 = tk.Frame(master = win , bg = "#FFA500")
    F12.pack(fill = "both" , expand = True )
    #-------------------------------------------------------------------------------
    LF115 = tk.Label(master = F12 , text = "Roll no." , bg = "#FFA500" , fg = "red" , font = ("Arial",12))
    LF115.pack(side = tk.LEFT , padx = 60)
    #-------------------------------------------------------------------------------
    E4 = tk.Entry(master = F12 )
    E4.pack(side = tk.LEFT , padx = 60)
    #-------------------------------------------------------------------------------
    E5 = tk.Entry(master = F12 )
    E5.pack(side = tk.RIGHT , padx = 60)
    #-------------------------------------------------------------------------------
    LF116 = tk.Label(master = F12 , text = "Admn. no." , bg = "#FFA500" , fg = "red" , font = ("Arial",12))
    LF116.pack(side = tk.RIGHT , padx = 60)
    #-------------------------------------------------------------------------------
    F13 = tk.Frame(master = win , bg = "#FFA500")
    F13.pack(fill = "both" , expand = True )
    #-------------------------------------------------------------------------------
    global Lb1
    Lb1 = ""

    def b1():
        #---------------------------------------------------------------------
        global Lb1
        while Lb1 :
            Lb1.destroy()
            Lb1 = ""
        #----------------------------------------------------------------------------
        l = []
        w = 0
        #------------------------------------------------------------------------
        for i in (E1,E2,E3,E4,E5):
            e = i.get()
            tt = ""
            #---------------------------------------------------------
            for o in e :
                if o != " " :
                    tt += o
            #--------------------------------------------------------------
            if i in (E1,E2,E3):
                if tt.isalpha() != True  :
                    w += 1
            elif i in (E4,E5):
                if tt.isdigit() != True :
                    w += 1
            l.append(str(e))
        #------------------------------------------------------------------
        if w != 0 :
            Lb1 = tk.Label(master = F13 , text = "Please enter valid data!!!",font = ("Arial",16))
            Lb1.pack()
            return
        else :
            for i in (E1,E2,E3,E4,E5) :
                i.delete(0,tk.END)
        k = l[3]
        l.pop(3)
        l.insert(0,k)
        ll = tuple(l)
        cmd = "insert into maintable values"+str(ll)+";"
        sql.execute(cmd)
        mysql.commit()
        cd = "insert into attendance values"+str(tuple(l[0:2]))+";"
        sql.execute("desc attendance;") 
        cmd = cd[0:len(cd)-2] + ",'A'"*((len(sql.fetchall()))-2)+");"
        sql.execute(cmd)
        mysql.commit()
        sql.execute("select * from maintable order by Rollno ;")
        sql.fetchall()
        sql.execute("select * from attendance order by Rollno ;")
        sql.fetchall()

    #-------------------------------------------------------------------------------    
    B1 = tk.Button(master = F13 , text = "Enter data", command = b1 , bg = "red" , fg = "#FFA500" , width = 10 , height = 2 )
    B1.pack(side = tk.BOTTOM)
    #-------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------
    F2 = tk.Frame(master = win , bg = "white")
    F2.pack(fill = "both" , expand = True)
    #-------------------------------------------------------------------------------
    LF21 = tk.Label(master = F2 , text = "Attendance input centre" , bg = "white" , fg = "#9400d3" , font = ("Arial",24,"bold","underline"))
    LF21.pack(fill = "both" , expand = True)
    #-------------------------------------------------------------------------------
    LF22 = tk.Label(master = F2 , text = "Enter Roll. no. (with commas)" , bg = "white" , fg = "#9400d3" , font =("Arial",16) )
    LF22.pack(side = tk.LEFT)
    #-------------------------------------------------------------------------------
    E7 = tk.Entry(master = F2 ,width  = 50 , bg = "#9400d3" , fg = "white" )
    E7.pack(side = tk.LEFT)
    #-------------------------------------------------------------------------------
    F21 = tk.Frame(master = win , bg = "white")
    F21.pack(fill = "both" , expand = True)
    #-------------------------------------------------------------------------------
    ED = tk.Entry(master = F21 ,width  = 10 , bg = "#9400d3" , fg = "white" )
    ED.pack(side = tk.LEFT)
    #-------------------------------------------------------------------------------
    EM = tk.Entry(master = F21 ,width  = 10 , bg = "#9400d3" , fg = "white" )
    EM.pack(side = tk.LEFT,padx = 100)
    #-------------------------------------------------------------------------------
    EY = tk.Entry(master = F21 ,width  = 10 , bg = "#9400d3" , fg = "white" )
    EY.pack(side = tk.LEFT)
    #-------------------------------------------------------------------------------
    F23 = tk.Frame(master = win , bg = "white")
    F23.pack(fill = "both" , expand = True)
    #-------------------------------------------------------------------------------
    LF231 = tk.Label(master = F23 , text = "Date" , bg = "white" , fg = "#9400d3" , font =("Arial",16) )
    LF231.pack(side = tk.LEFT)
    #-------------------------------------------------------------------------------
    LF232 = tk.Label(master = F23 , text = "Month" , bg = "white" , fg = "#9400d3" , font =("Arial",16) )
    LF232.pack(side = tk.LEFT,padx = 110)
    #-------------------------------------------------------------------------------
    LF233 = tk.Label(master = F23 , text = "Year" , bg = "white" , fg = "#9400d3" , font =("Arial",16) )
    LF233.pack(side = tk.LEFT)
    #-------------------------------------------------------------------------------
    global Lb21
    global Lb22
    Lb21 = Lb22 = ""
    def b2():
        global Lb21
        global Lb22
        while Lb21 :
            Lb21.destroy()
            Lb21 = ""
        while Lb22 :
            Lb22.destroy()
            Lb22 = ""
            
        l = []
        r = E7.get()
        for i in r.split(","):
            if int(i.isdigit()) != 1 :
                Lb21 = tk.Label(master = F2 , text = "Please enter valid data !!" , font = ("Arial",16))
                Lb21.pack()
                return
            l.append(i)
        D = ED.get()
        M = EM.get()
        Y = EY.get()
        
        for i in (D,M,Y):
            if int(i.isdigit()) != 1 :
                Lb22 = tk.Label(master = F2 , text = "Please enter valid data !!" , font = ("Arial",16))
                Lb22.pack()
                return

        month = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",
                7:"July",8:"August",9:"September",10:"October",11:"November",
                12:"December"}
        
        if (Lb21 == "") and (Lb22 == "") :
            E7.delete(0,tk.END)
            ED.delete(0,tk.END)
            EM.delete(0,tk.END)
            EY.delete(0,tk.END)
        date = month[int(M)] + str(D)+"y"+str(Y)
        cd = "alter table attendance add("+date+" varchar(1) DEFAULT'P');"
        sql.execute(cd)
        mysql.commit()
        for i in l :
            cd = "update attendance set " + date + " ='A' where Rollno = " + str(i) + ";"
            sql.execute(cd)
            mysql.commit()
    #-------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------
    F22 = tk.Frame(master = win , bg = "white")
    F22.pack(fill = "both" , expand = True)
    #-------------------------------------------------------------------------------
    B2 = tk.Button(master = F22 , text = "Enter attendance", command = b2 , bg = "#9400d3" , fg = "white" , width = 15 , height = 2 )
    B2.pack(side = tk.BOTTOM)
    #-------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------
    F3u = tk.Frame(master = win , bg = "green")
    F3u.pack(fill = "both" , expand = True)
    #---------------------------------------------------------------------------------
    F3l = tk.Frame(master = win , bg = "green")
    F3l.pack(fill = "both" , expand = True)
    #--------------------------------------------------------------------------------
    def me():
        mysql.close()
        win.destroy()
        test_window.tw()
    #---------------------------------------------------------------------------------
    def quit():
        mysql.close()
        win.destroy()
    #---------------------------------------------------------------------------------
    ME = tk.Button(master = F3u , text = "Marks Entry", command = me , width = 10 , height = 2 )
    ME.pack(side = tk.LEFT , padx = 40)
    #----------------------------------------------------------------------------------
    def output():
        mysql.close()
        win.destroy()
        output_window.ow()
    #----------------------------------------------------------------------------------
    OW = tk.Button(master = F3u , text = "Dashboard", command = output , width = 10 , height = 2 )
    OW.pack(side = tk.LEFT , padx = 40)
    #---------------------------------------------------------------------------------
    def sd():
        mysql = Mysql.connect(host = h , user = u , password = p )
        sql = mysql.cursor()
        sql.execute("drop database " + d + ";")
        mysql.close()
        win.destroy()
    #---------------------------------------------------------------------------------
    SD = tk.Button(master = F3l , text = " ", command = sd , bg = "green" , fg = "green" , width = 2 , height = 1 )
    SD.pack(side = tk.RIGHT)
    #-------------------------------------------------------------------------------
    QB = tk.Button(master = F3u , text = "Quit", command = quit , width = 10 , height = 2 )
    QB.pack(side = tk.LEFT , padx = 40)
    win.mainloop()

