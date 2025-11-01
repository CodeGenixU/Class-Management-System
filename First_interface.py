import tkinter as tk
import main_window 
s1 = """We welcome you to our application . This application helps you to maintain school records with help of
databases and analyse it with the help of graph . As this application is in its starting stages , this application
has many limitation . For example - If a data is assigned then it can't be update if data is revised ,
Its not user flexible as it has limited working capabilities etc .

Since we were school students and we have many things yet to be learnt . Therefore , we are looking forward
to you , use our application , recommend us if you have any suggestion  , report any abnormal functioning of
application .

At last but not the least we 'THANK YOU' all for using our application .
"""
s2 ="""
From Abhinav Kumar
"""

def swagat():
    welcome = tk.Tk()
    welcome.geometry("1100x600")
    welcome.title("Welcome")
    wel = tk.Frame(master = welcome,bg = "#00ffff")
    wel.pack(fill = "both" , expand = True)
    l1 = tk.Label(master = wel , text = "Welcome",bg = "#00ffff" , fg = "#7F00FF",font = ("Arial",32,"italic","bold"))
    l1.pack()
    l2 = tk.Label(master = wel , text = s1 , bg =  "#00ffff" , font = ("Arial",16,"italic") )
    l2.pack()
    l3 = tk.Label(master = wel , text = s2 , bg =  "#00ffff" , fg = "green" , font = ("Arial",18,"italic","bold") )
    l3.pack()
    l4 = tk.Label(master = wel , text = "THANK YOU" , bg =  "#00ffff" , fg = "red" , font = ("Arial",20,"italic","bold") )
    l4.pack()
    def B():
        welcome.destroy()
        main_window.mw()
    b = tk.Button(master = wel , text = "OK , done" , command = B, bg = "#Ffc0cb" , fg = "#7F00FF" , font = ("Arial",10,"bold"))
    b.pack()
    welcome.mainloop()

