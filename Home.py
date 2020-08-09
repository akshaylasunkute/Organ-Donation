# start from line 22
from tkinter import *
from tkinter import ttk
import time
from PIL import ImageTk, Image
from tkinter import messagebox
import datetime
import mysql.connector

# connection to mysql database
mydb = mysql.connector.connect(user="technoseed" ,password="123techno",host="localhost",database="organ")
mycursor=mydb.cursor()

def searchDonor():
    if(searchentry.get()==""):
        messagebox.showerror("Entry Error","Please enter the key value")
        return
    try:
        mycursor.execute("select * from donor where pancard='"+searchentry.get()+"'")
        record=mycursor.fetchone()
        name=record[0]+" "+record[1]+" "+record[2]
        Label(searchwindow,text="Name : "+name).place(x=50,y=130)

    except:
        messagebox.showerror("value error","please enter valid key entry")
        searchwindow.destroy()

def searchDonorwindow():
    global searchwindow
    searchwindow=Tk()
    searchwindow.geometry("500x300")
    searchwindow.title("Search Donor")
    searchwindow.resizable(0,0)

    Label(searchwindow,text="Enter the ID").place(x=50,y=100)

    global searchentry
    searchentry=Entry(searchwindow,width=20)
    searchentry.place(x=200,y=100)

    searchbutton=Button(searchwindow,text="search",command=searchDonor)
    searchbutton.place(x=400,y=100)

    searchwindow.mainloop()

# to view donors list
def viewDonorwindow():
    display = Tk()
    display.title("Donor")
    display.geometry("1100x500")
    display.resizable(0, 0)

    mycursor.execute("select * from donor")
    lencheck = len(mycursor.fetchall())
    displayview = ttk.Treeview(display, height=lencheck, columns=(1, 2, 3,4,5), show="headings", selectmode="browse")
    displayview.grid(row=0, column=0,padx=35)

    displayview.heading(1, text="ID NUMBER")
    displayview.heading(2, text="First NAME")
    displayview.heading(3, text="Middle Name")
    displayview.heading(4, text="Last NAME")
    displayview.heading(5, text="ADDRESS")

    mycursor.execute("select pancard,fname,mname,lname,address from donor")
    records=mycursor.fetchall()

    for record in records:
        displayview.insert('','end',value=record)

    display.mainloop()


def AddDonor():
    records=[ efname.get(), emname.get(), elname.get(), eaddress.get(), ecity.get(), edistrict.get(), estate.get(), ezipcode.get(), ebirth.get(), emobnum.get(), emobnum1.get(), eidcard.get()]
    for value in records:
        if value=="":
            messagebox.showerror("Value Error","Please Fill All Fields")
            break
    que1= "insert into donor values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    value1=( efname.get(), emname.get(), elname.get(), eaddress.get(), ecity.get(), edistrict.get(), estate.get(), ezipcode.get(), ebirth.get(),  eidcard.get(),genderchoice.get(), eye1.get(), kidney1.get(), heart1.get(), lungs1.get(), liver1.get(), pancreas1.get(), small1.get(), skin1.get(),bloodchoice.get())
    mycursor.execute(que1,value1)
    mydb.commit()
    value2=(eidcard.get(),emobnum.get())
    value3=(eidcard.get(),emobnum1.get())
    que2="insert into mobnum values(%s,%s)"
    mycursor.execute(que2,value2)
    mydb.commit()
    mycursor.execute(que2, value3)
    mydb.commit()
    newwindow.destroy()


def AddDonorwindow():
    global newwindow
    newwindow = Tk()
    newwindow.geometry("640x600")
    newwindow.resizable(0, 0)
    newwindow.title("ADD DONOR")
    fname = Label(newwindow, text="Enter the First Name :\t")
    mname = Label(newwindow, text="Enter the Middle Name :\t")
    lname = Label(newwindow, text="Enter the Last Name :\t")
    address = Label(newwindow, text="Enter the Address :\t\t")
    city = Label(newwindow, text="Enter the City :\t\t")
    district = Label(newwindow, text="Enter the District :\t\t")
    state = Label(newwindow, text="Enter the State :\t\t")
    zipcode = Label(newwindow, text="Enter the Zip Code :\t")
    birth = Label(newwindow, text="Enter the Birth Date :\t")
    mobnum = Label(newwindow, text="Enter the Mobile Number :\t")
    idcard = Label(newwindow, text="Enter the Pan Card Number :\t")
    gender = Label(newwindow, text="Select the Gender :\t")
    organchoose = Label(newwindow, text="choose the Organs :\t")
    blood = Label(newwindow, text="Select the Blood Group :\t")

    global efname, emname, elname, eaddress, ecity, edistrict, estate, ezipcode, ebirth, emobnum, emobnum1, eidcard

    efname = Entry(newwindow)
    emname = Entry(newwindow)
    elname = Entry(newwindow)
    eaddress = Entry(newwindow)
    ecity = Entry(newwindow)
    edistrict = Entry(newwindow)
    estate = Entry(newwindow)
    ezipcode = Entry(newwindow)
    ebirth = Entry(newwindow)
    emobnum = Entry(newwindow)
    emobnum1 = Entry(newwindow)
    eidcard = Entry(newwindow)

    global genderchoice,bloodchoice

    genderchoice = StringVar(newwindow)
    egender = OptionMenu(newwindow, genderchoice, "Male", "Female")
    genderchoice.set("select")

    bloodchoice = StringVar(newwindow)
    bloodchoice.set("select")
    eblood = OptionMenu(newwindow, bloodchoice, "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-")

    global eye1, kidney1, heart1, lungs1, liver1, pancreas1, small1, skin1

    eye1 = IntVar(newwindow)
    kidney1 = IntVar(newwindow)
    heart1 = IntVar(newwindow)
    lungs1 = IntVar(newwindow)
    liver1 = IntVar(newwindow)
    pancreas1 = IntVar(newwindow)
    small1 = IntVar(newwindow)
    skin1 = IntVar(newwindow)

    global eeye
    eeye = Checkbutton(newwindow, text="Eyes", variable=eye1, onvalue=1,offvalue=0)
    eeye.grid(row=13, column=0)

    ekidney = Checkbutton(newwindow, text="Kidney", variable=kidney1, onvalue=1,offvalue=0)
    ekidney.grid(row=13, column=1)

    eheart = Checkbutton(newwindow, text="Heart", variable=heart1, onvalue=1,offvalue=0)
    eheart.grid(row=13, column=2)

    elungs = Checkbutton(newwindow, text="Lungs", variable=lungs1, onvalue=1,offvalue=0)
    elungs.grid(row=14, column=0)

    eliver = Checkbutton(newwindow, text="Liver", variable=liver1, onvalue=1,offvalue=0)
    eliver.grid(row=14, column=1)

    epancreas = Checkbutton(newwindow, text="Pancreas", variable=pancreas1, onvalue=1,offvalue=0)
    epancreas.grid(row=14, column=2)

    esmall = Checkbutton(newwindow, text="Small Intestine", variable=small1, onvalue=1,offvalue=0)
    esmall.grid(row=15, column=0)

    eskin = Checkbutton(newwindow, text="Skin", variable=skin1, onvalue=1,offvalue=0)
    eskin.grid(row=15, column=1)

    fname.grid(row=0, column=0, padx=20, pady=5)
    mname.grid(row=1, column=0, pady=5)
    lname.grid(row=2, column=0, pady=5)
    address.grid(row=3, column=0, pady=5)
    city.grid(row=4, column=0, pady=5)
    district.grid(row=5, column=0, pady=5)
    state.grid(row=6, column=0, pady=5)
    zipcode.grid(row=7, column=0, pady=5)
    birth.grid(row=8, column=0, pady=5)
    mobnum.grid(row=9, column=0, pady=5)
    idcard.grid(row=10, column=0, pady=5)
    gender.grid(row=11, column=0, pady=5)
    organchoose.grid(row=12, column=0, pady=5)
    blood.grid(row=16, column=0, pady=10)

    efname.grid(row=0, column=1)
    emname.grid(row=1, column=1)
    elname.grid(row=2, column=1)
    eaddress.grid(row=3, column=1)
    ecity.grid(row=4, column=1)
    edistrict.grid(row=5, column=1)
    estate.grid(row=6, column=1)
    ezipcode.grid(row=7, column=1)
    ebirth.grid(row=8, column=1)
    emobnum.grid(row=9, column=1)
    emobnum1.grid(row=9, column=2)
    eidcard.grid(row=10, column=1)
    egender.grid(row=11, column=1)
    eblood.grid(row=16, column=1)

    Button(newwindow, text="SUBMIT", bg="orange",command=AddDonor).grid(row=17, column=1, pady=10, ipadx=20, ipady=5)

    newwindow.mainloop()


def dateandtimefun():
    # save login time and date in last login table
    mycursor.execute("delete from lastlogin")
    nowdate = datetime.datetime.now()
    logintime = nowdate.time()
    logindate = nowdate.date()
    que = "Insert into lastlogin values(%s,%s)"
    value = (logindate, logintime)
    mycursor.execute(que, value)
    mydb.commit()
    time.sleep(1)

# if login is successful then first window will appear
def firstwindow():
    dateandtimefun()
    # create new window
    Firstwindow = Tk()
    Firstwindow.geometry("900x450")
    Firstwindow.title("Organ Donation")
    Firstwindow.resizable(0,0)

    # creates two tabs in Firstwindow
    tabs=ttk.Notebook(Firstwindow)
    tab1=Frame(tabs)
    tab2 = Frame(tabs)
    tabs.add(tab1,text="\t\t\t                   First                 \t\t\t")
    tabs.add(tab2,text="\t\t\t                  Second                 \t\t\t")
    tabs.pack(expan=1, fill="both", padx=10, pady=10)
    Firstwindow.configure(bg="light blue")
    Label(tab1,text="Welcome To Organ Donation System").place(x=200,y=200)
    AddBut=Button(tab2,text="Add Donor",width=12,command=AddDonorwindow)
    AddBut.place(x=50,y=50)

    viewdonor = Button(tab2, text="View Donor", width=12, command=viewDonorwindow)
    viewdonor.place(x=50, y=100)

    searchdonor = Button(tab2, text="Search Donor", width=12, command=searchDonorwindow)
    searchdonor.place(x=50, y=150)

    Firstwindow.mainloop()

# check the username and password if valid then come to this code
def checkadmin():
        if username.get()=="":
            messagebox.showwarning("info","please enter user name")
            return
        elif password.get()=="":
            messagebox.showwarning("info", "please enter Password")
            return
        que="select * from ADMIN where user_name=%s and password=%s"
        value=(username.get(),password.get())
        mycursor.execute(que,value)
        record=mycursor.fetchall()
        if len(record)==0:
            messagebox.showerror("Data Error","Enter valid username or password")
            username.delete(0, END)
            password.delete(0, END)
        else:
            username.delete(0,END)
            password.delete(0,END)
            root.destroy()
            firstwindow()

# main loop
def main():
    global root
    root = Tk()
    root.geometry("700x500+50+50")
    root.title("Organ Donation")
    root.resizable(0,0)

    # Background image for login screen
    backimg=ImageTk.PhotoImage(Image.open("organ.jpg"))
    back=Label(root,image=backimg)
    back.place(x=0,y=0,relwidth=1,relheight=1)

    mycursor.execute("select lastdate,lasttime from lastlogin")
    dateandtime=mycursor.fetchone()
    Label(root,text="Last Login Date "+str(dateandtime[1]),bg="white",fg="blue").place(x=515,y=50)
    Label(root, text="Last Login Date " + str(dateandtime[0]), bg="white",fg="blue").place(x=515, y=70)

    L1= Label(root,text="Organ Donation",bg="red",font=("times new roman",31))
    L1.pack(side=TOP,fill=X)
    L2= Label(root,text="Organ Donation",bg="red",font=("times new roman",31))
    L2.pack(side=BOTTOM,fill=X)

    # Labels for username and password
    L3 = Label(root, text="Enter the Name :",bg="dark orange")
    L3.place(x=10,y=160)
    L4 = Label(root, text="Enter the Password :",bg="dark orange")
    L4.place(x=10,y=190)

    global username,password

    # Entry boxes for username and screen
    username = Entry(root,width=25)
    username.place(x=150, y=160)

    bullet = "\u2022" # for password field
    password = Entry(root,show=bullet,width=25)
    password.place(x=150, y=190)

    # submit button to check given login credentials are correct or not (call to checkadmin function)
    submitbut = Button(root, text="submit",bg="aqua",command=checkadmin)
    submitbut.place(x=120, y=220)

    root.mainloop()

#first call
if __name__ == '__main__':
    main()
