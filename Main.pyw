from PIL import ImageTk
from PIL import Image as imgfunc
import multiprocessing as mt
from win10toast import ToastNotifier
from tkinter import *
import csv
import datetime

#2020 ThatCodeAddict
#V 1.0 of DPP

toaster = ToastNotifier()
def main():
    root = Tk()
    root.title("Planner")
    root.iconbitmap("Logo.ico")
    root.geometry('300x350')

    try:
        fh = open("Planner.dp",'r')
        fh.close()
    except:
        fh = open("Planner.dp", 'w')
        fh.close()

    #---------------------------------#
    def add_reminder():
        root2 = Tk()
        root2.title("Planner")
        root2.geometry("300x320")
        root2.iconbitmap("Logo.ico")
        
        text = Label(root2, text="Add Assignment Name")
        entry = Entry(root2, width=30, borderwidth=1)

        text3 = Label(root2, text="Enter Period")
        entry5 = Entry(root2, width=5, borderwidth=1)

        text2 = Label(root2, text="Enter Due Date")
        entry2 = Entry(root2, width=5, borderwidth=1)
        entry3 = Entry(root2, width=5, borderwidth=1)
        entry4 = Entry(root2, width=5, borderwidth=1)


        button = Button(root2, text="Submit", padx=50, pady=2, command=lambda:submit(root2, entry,entry2,entry3,entry4, entry5, text, text2, text3, button))

        entry.insert(0, "My Reminder")

        date = str(datetime.date.today()).split("-")

        entry2.insert(0, date[1])
        entry3.insert(0, str(int(date[2])+1))
        entry4.insert(0, date[0])


        text.pack(side=TOP, pady=4)
        entry.pack(side=TOP, pady=5)
        text3.pack(side=TOP, pady=6)
        entry5.pack(side=TOP, pady=7)
        text2.pack(side=TOP, pady=8)
        entry2.pack(side=TOP, pady=9)
        entry3.pack(side=TOP, pady=10)
        entry4.pack(side=TOP, pady=11)

        button.pack(side=TOP, pady=6)
    
    def submit(root2, entry, entry2, entry3, entry4, entry5, text, text2, text3, button):
        name = entry.get()
        month = entry2.get()
        day = entry3.get()
        year = entry4.get()
        period = entry5.get()
        date = str(datetime.date.today()).split("-")
        if period.isnumeric() == False:
            return
        else:
            if year.isnumeric() == True:
                if int(year) < int(date[0]):
                    return
                else:
                    if day.isnumeric() == True:
                        if int(day) > 31:
                            return
                        else:
                            if month.isnumeric() == True:
                                fh = open("Planner.dp",'a')
                                fh.write(name+","+year+"-"+day+"-"+month+","+period+",0"+"\n")
                                fh.close()

                                entry.delete(0, END)
                                entry2.delete(0, END)
                                entry3.delete(0, END)
                                entry4.delete(0, END)
                                entry5.delete(0, END)
                            else:
                                return
                    else:
                        return
            else:
                return
        
        root2.destroy()

        photo = imgfunc.open('Logo.png')
        resized = photo.resize((210,200), imgfunc.ANTIALIAS)
        new_photo = ImageTk.PhotoImage(resized)

        canvas = Canvas(root, width = 220, height = 210)

        add_hw = Button(root, text="Add Homework", padx=50, pady=2, borderwidth=1, command=add_reminder)
        canvas.create_image(20,20, anchor=NW, image=new_photo)

        canvas.pack(side=TOP)
        add_hw.pack(side=TOP, pady=9)
        
    #---------------------------------#

    photo = imgfunc.open(r'Logo.png')
    resized = photo.resize((210,200), imgfunc.ANTIALIAS)
    new_photo = ImageTk.PhotoImage(resized)

    canvas = Canvas(root, width = 220, height = 210)

    add_hw = Button(root, text="Add Homework", padx=50, pady=2, borderwidth=1, command=add_reminder)
    canvas.create_image(20,20, anchor=NW, image=new_photo)

    canvas.pack(side=TOP)
    add_hw.pack(side=TOP, pady=9)

    print(datetime.date.today())
    print(datetime.datetime.now())

    root.mainloop()

def notification():
    toaster.show_toast("Planner System", "System Has Started", duration = 5, icon_path="Logo.ico")

def hwcheck():
    dateNow = datetime.date.today()
    while True:
        fh = open("Planner.dp",'r')
        reader = csv.reader(fh)
        name = []
        date = []
        period = []
        stats = []
        for line in reader:
            name.append(line[0])
            date.append(line[1])
            period.append(line[2])
            stats.append(line[3])
        for i in range(len(date)):
            if date[i] == str(dateNow):
                if stats[i] == "0" or "1":
                    toaster.show_toast("Planner System", "Your Assignment '"+name[i]+"' For Period "+period[i]+" Is Due Today!", duration = 5, icon_path="Logo.ico")
                    name.pop(i)
                    date.pop(i)
                    period.pop(i)
                    stats.pop(i)

                    for j in range(len(name)):
                        fh = open("Planner.dp",'w')
                        fh.write(name[j]+","+date[j]+","+period[j]+","+stats[j]+"\n")
                        fh.close()
            dateNow2 = date[i].split("-")
            dateNow2 = int(dateNow2[1])+1
            dateNow3 = str(datetime.date.today())
            dateNow3 = int(dateNow3[1])+1

            if str(dateNow2) == str(dateNow3):
                if stats[i] == "0":
                    toaster.show_toast("Planner System", "Your Assignment '"+name[i]+"' For Period "+period[i]+" Is Due Tomorrow!", duration = 5, icon_path="Logo.ico")
                    stats[i] == "1"
                    for j in range(len(name)):
                        fh = open("Planner.dp",'w')
                        fh.write(name[j]+","+date[j]+","+period[j]+","+stats[j]+"\n")
                        fh.close()

                

if __name__ == "__main__":
    t1 = mt.Process(target=main)
    t2 = mt.Process(target=notification)
    t3 = mt.Process(target=hwcheck)

    t1.start()
    t2.start()
    t3.start()

#2020 ThatCodeAddict
