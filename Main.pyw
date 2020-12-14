# from PIL import ImageTk
# from PIL import Image as imgfunc
import multiprocessing as mt
from win10toast import ToastNotifier
from time import sleep
from tkinter import *
import csv
import datetime

#2020 ThatCodeAddict
#V1.1 of SPP
#EM Technologies - Software Branch

toaster = ToastNotifier()
class setupwhole():
    def setup():
        def submit2(root, periodentries):
            periodnames = []
            for i in periodentries:
                try:
                    a = i.get()
                except:
                    pass
                else:
                    a = i.get()
                    periodnames.append(a)
            fh = open("Periods.csv",'w')
            for i in range(len(periodnames)):
                fh.write(str(i+1) + "," + str(periodnames[i])+"\n")
            fh.close()
            root.destroy()

        def submit(root):
            num = entry1.get()
            if num.isnumeric() == False:
                return
            else:
                root.destroy()
                root2 = Tk()
                root2.title("Planner")
                root2.iconbitmap("Logo.ico")
                root2.geometry("250x" + str(int(num)*50 + 100))
                root2.resizable(width=False, height=False)


                label1 = Label(root2, text="Planner Setup")
                label1.pack(side=TOP)
                periodentries = []
                for i in range(0, int(num)):
                    label = Label(root2, text="Enter Name Of Period: " + str(i+1))
                    entry = Entry(root2, width="10")
                    periodentries.append(label)
                    periodentries.append(entry)

                a = 0
                b = 1

                for i in periodentries: # 1L 1E  
                    if a == 3:
                        a = 0
                        b = b+1
                        i.pack(side=TOP, pady=b)
                    else:
                        i.pack(side=TOP, pady=b)
                        
                submit = Button(root2, text="Submit", padx=10, pady=2, command=lambda:submit2(root2, periodentries))
                submit.pack(side=TOP, pady=b+2)

                root2.mainloop()

        root = Tk()
        root.title("Planner")
        root.geometry("250x115")
        root.iconbitmap("Logo.ico")

        label1 = Label(root, text="Planner Setup")
        label2 = Label(root, text="Enter Number Of Periods")
        entry1 = Entry(root, width="5")
        button1 = Button(root, text="Submit", padx=50, pady=2, borderwidth=1, command=lambda:submit(root))

        label1.pack(side=TOP)
        label2.pack(side=TOP, pady=3)
        entry1.pack(side=TOP, pady=5)
        button1.pack(side=TOP,pady=7)

        root.mainloop()

def main():
    try:
        fh = open("Planner.csv",'r')
        fh.close()
        fh = open("Periods.csv", 'r')
        fh.close()
    except:
        fh = open("Planner.csv", 'w')
        fh.write("Class\Period,Homework Name,Date Assigned,Due Date,Status,If Called")
        fh.close()
        fh = open("Periods.csv", 'w')
        fh.close()
        setup()
    else:
        root = Tk()
        root.title("Planner")
        root.iconbitmap("Logo.ico")
        root.geometry('300x450')


        #---------------------------------#
        class add_reminder_whole():
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


                button = Button(root2, text="Submit", padx=50, pady=2, command=lambda:add_reminder_whole.submit(root2,entry,entry2,entry3,entry4,entry5))

                entry.insert(0, "My Assignment")

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
            
            def submit(root2, entry, entry2, entry3, entry4, entry5):
                name = entry.get()
                month = entry2.get()
                day = entry3.get()
                year = entry4.get()
                period = entry5.get()
                currentdate = str(datetime.date.today())
                date = currentdate.split("-")

                periods = []
                periodnames = []
                fh = open("Periods.csv",'r')
                reader = csv.reader(fh)
                for line in reader:
                    periods.append(line[0])
                    periodnames.append(line[1])
                fh.close()
                

                if period.isnumeric() == False:
                    return
                elif len(periods) < int(period):
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
                                        if int(month) == 2:
                                            if int(day) > 28:
                                                return
                                            else:
                                                fh = open("Planner.csv",'a')
                                                fh.write("\n"+period+","+name+","+currentdate+","+year+"-"+month+"-"+day+",Not Started,0")
                                                fh.close()
                                                root2.destroy()
                                                change_status["state"] = "normal"
                                                remove_hw["state"] = "normal"
                                        else:
                                            fh = open("Planner.csv",'a')
                                            fh.write("\n"+period+","+name+","+currentdate+","+year+"-"+month+"-"+day+",Not Started,0")
                                            fh.close()
                                            root2.destroy()
                                            change_status["state"] = "normal"
                                            remove_hw["state"] = "normal"
                                            
                                            

                                    else:
                                        return
                                            
                            else:
                                return
                    else:
                        return
        #---------------------------------#
        class change_status_whole():
            def change_status():
                root2 = Tk()
                root2.title("Planner")
                root2.geometry("200x200")
                root2.iconbitmap("Logo.ico")
                fh = open("Planner.csv", "r")
                reader = csv.reader(fh)

                periods = []
                names = []
                statuses = []

                combined = []

                for line in reader:
                    periods.append(line[0])
                    names.append(line[1])
                    statuses.append(line[4])
                
                names.pop(0)
                periods.pop(0)
                statuses.pop(0)

                for i in range(len(names)):
                    combined.append(names[i]+", Period "+ periods[i])

                if len(names) == 0:
                    return
                else:
                    
                    entry1 = Entry(root2, width=25)
                    entry1.insert(0, "Change Homework Status")


                    variable = Variable(root2)
                    variable.set(combined[0])

                    menu = OptionMenu(root2, variable, *combined)

                    statuslist = [
                        "Not Started",
                        "In Progress",
                        "Finished"
                    ]

                    variable2 = Variable(root2)
                    variable2.set(statuslist[1])

                    menu2 = OptionMenu(root2, variable2, *statuslist)

                    submit = Button(root2, text="Submit", padx=40, pady=2, command=lambda:change_status_whole.submit(root2, variable, variable2, entry1, combined, statuses))

                    entry1.pack(side=TOP)
                    menu.pack(side=TOP, pady=2)
                    menu2.pack(side=TOP, pady=4)
                    submit.pack(side=TOP, pady=6)

            def submit(root2, menu, menu2, entry1, combined, statuses):
                assignment = menu.get()
                statuspref = menu2.get()
                
                for i in range(len(combined)):
                    if combined[i] == assignment:
                        if statuses[i] == statuspref:
                            entry1.delete(0, END)
                            entry1.insert(0, "Status Error")
                            return
                        else:
                            fh = open("Planner.csv",'r')
                            reader = csv.reader(fh)

                            periods = []
                            names = []
                            datedoc = []
                            datedue = []
                            status = []
                            ifcalled =  []
                            combined = []

                            for line in reader:
                                periods.append(line[0])
                                names.append(line[1])
                                datedoc.append(line[2])
                                datedue.append(line[3])
                                status.append(line[4])
                                ifcalled.append(line[5])
                            
                            periods.pop(0)
                            names.pop(0)
                            datedoc.pop(0)
                            datedue.pop(0)
                            status.pop(0)
                            ifcalled.pop(0)

                            status[i] = statuspref
                            fh = open("Planner.csv",'w')
                            fh.write("Class\Period,Homework Name,Date Documented,Due Date,Status,If Called")
                            for i in range(len(names)):
                                fh.write("\n"+periods[i]+","+names[i]+","+datedoc[i]+","+datedue[i]+","+status[i]+","+ifcalled[i])
                            fh.close()
                            root2.destroy()
                            break
                return
        #---------------------------------#
        class remove_reminder_whole():
            def remove_reminder():
                root3 = Tk()
                root3.title("Planner")
                root3.geometry("300x75")
                root3.iconbitmap("Logo.ico")
                fh = open("Planner.csv",'r')
                reader = csv.reader(fh)

                periods = []
                names = []
                combined = []

                for line in reader:
                    periods.append(line[0])
                    names.append(line[1])
                            
                periods.pop(0)
                names.pop(0)

                for i in range(len(names)):
                    combined.append(names[i] + ", Period "+periods[i])
                
                variable = Variable(root3)
                variable.set(combined[0])
                menu = OptionMenu(root3, variable, *combined)

                submit = Button(root3, text="Submit", padx=40, pady=2, command=lambda:remove_reminder_whole.check(variable, root3))

                menu.pack(side=TOP)
                submit.pack(side=TOP, pady=3)

            def check(variable, root3):
                root4 = Tk()
                root4.title("Planner")
                root4.geometry("250x150")
                root4.iconbitmap("Logo.ico")

                label = Label(root4, text="Are You Sure You Want To Delete This?")
                label2 = Label(root4, text="THIS CANNOT BE UNDONE!!")

                no = Button(root4, text="No", padx=5, pady=5, command=lambda:remove_reminder_whole.Pass(root3, root4))
                yes = Button(root4, text="Yes", padx=5, pady=5, command=lambda:remove_reminder_whole.remove(variable, root3, root4))
                
                label.pack(side=TOP)
                label2.pack(side=TOP, pady=1)
                no.pack(side=TOP, pady=4)
                yes.pack(side=TOP, pady=8)

            def Pass(root3, root4):
                root4.destroy()
                root3.destroy()

            def remove(variable,root3, root4):
                assignment = variable.get()

                fh = open("Planner.csv",'r')
                reader = csv.reader(fh)

                periods = []
                names = []
                datedoc = []
                datedue = []
                status = []
                ifcalled = []
                combined = []

                for line in reader:
                    periods.append(line[0])
                    names.append(line[1])
                    datedoc.append(line[2])
                    datedue.append(line[3])
                    status.append(line[4])
                    ifcalled.append(line[5])
                            
                periods.pop(0)
                names.pop(0)
                datedoc.pop(0)
                datedue.pop(0)
                status.pop(0)
                ifcalled.pop(0)

                fh.close()

                for i in range(len(names)):
                    combined.append(names[i] + ", Period "+periods[i])
                
                for i in range(len(names)):
                    if combined[i] == variable:
                        b = i
                
                periods.pop(i)
                names.pop(i)
                datedoc.pop(i)
                datedue.pop(i)
                status.pop(i)
                ifcalled.pop(i)

                if len(names) == 0:
                    remove_hw["state"] = "disabled"
                    change_status["state"] = "disabled"

                fh = open("Planner.csv", 'w')
                fh.write("Class\Period,Homework Name,Date Documented,Due Date,Status,If Called")
                for i in range(len(names)):
                    fh.write("\n"+periods[i]+","+names[i]+","+datedoc[i]+","+datedue[i]+","+status[i]+","+ifcalled[i])
                fh.close()

                root3.destroy()
                root4.destroy()


                
            




        #---------------------------------#

        names = []
        fh = open("Planner.csv",'r')
        reader = csv.reader(fh)
        for line in reader:
            names.append(line[1])
        names.pop(0)

        # photo = imgfunc.open(r'Logo.png')
        # resized = photo.resize((210,200), imgfunc.ANTIALIAS)
        # new_photo = ImageTk.PhotoImage(resized)

        canvas = Canvas(root, width = 220, height = 210)

        add_hw = Button(root, text="Add Homework", padx=50, pady=2, borderwidth=1, command=add_reminder_whole.add_reminder)
        remove_hw = Button(root, text="Remove Homework", padx=40, pady=2, borderwidth=1, command=remove_reminder_whole.remove_reminder)
        change_status = Button(root, text="Change Homework Status", padx=22, pady=2, borderwidth=1, command=change_status_whole.change_status)
        setup = Button(root, text="Open Setup", padx=61, pady=2, borderwidth=1, command=setupwhole.setup)
        # canvas.create_image(20,20, anchor=NW, image=photo)

        canvas.pack(side=TOP)
        add_hw.pack(side=TOP, pady=9)
        remove_hw.pack(side=TOP, pady=11)
        change_status.pack(side=TOP, pady=13)
        setup.pack(side=TOP, pady=15)
        

        if len(names) == 0:
            change_status["state"] = "disabled"
            remove_hw["state"] = "disabled"

        print(datetime.date.today())
        print(datetime.datetime.now())

        root.mainloop()

def hwcheck():
    while True:
        sleep(2)
        dateNow = datetime.date.today()
        fh = open("Planner.csv",'r')
        reader = csv.reader(fh)

        periods = []
        names = []
        datedoc = []
        datedue = []
        status = []
        ifcalled = []

        for line in reader:
            periods.append(line[0])
            names.append(line[1])
            datedoc.append(line[2])
            datedue.append(line[3])
            status.append(line[4])
            ifcalled.append(line[5])
        if len(names) == 0:
            continue
        
        else:
            periods.pop(0)
            names.pop(0)
            datedoc.pop(0)
            datedue.pop(0)
            status.pop(0)
            ifcalled.pop(0)
            fh.close()
            if len(names) == 0:
                pass
            else:
                periodnames = []
                fh = open("Periods.csv",'r')
                reader = csv.reader(fh)
                for line in reader:
                    periodnames.append(line[1])

                for i in range(len(datedue)):
                    if datedue[i] == str(dateNow):
                        if status[i] == "Not Started" or "In Progress":
                            if ifcalled[i] == "0" or "1":
                                toaster.show_toast("Planner System", "Your Assignment '"+names[i]+"' For "+periodnames[i]+" Is Due Today!", duration = 10, icon_path="Logo.ico")
                                ifcalled[i] = "2"
                                fh = open("Planner.csv", 'w')
                                fh.write("Class\Period,Homework Name,Date Documented,Due Date,Status,If Called")
                                for i in range(len(names)):
                                    fh.write("\n"+periods[i]+","+names[i]+","+datedoc[i]+","+datedue[i]+","+status[i]+","+ifcalled[i])
                                fh.close()
                                
                    dateNow = datetime.date.today()
                    dateNow = str(dateNow).split("-")
                    dateduetemp = str(datedue[i]).split("-")

                    if str(int(dateNow[2])+1) == str(dateduetemp[2]):
                        if ifcalled[i] == "0":
                            toaster.show_toast("Planner System", "Your Assignment '"+names[i]+"' For " + periodnames[i] + " Is Due Tomorrow!", duration = 10, icon_path="Logo.ico")
                            ifcalled[i] = "1"
                            fh = open("Planner.csv", 'w')
                            fh.write("Class\Period,Homework Name,Date Documented,Due Date,Status,If Called")
                            for i in range(len(names)):
                                fh.write("\n"+periods[i]+","+names[i]+","+datedoc[i]+","+datedue[i]+","+status[i]+","+ifcalled[i])
                            fh.close()

def notification():
    toaster.show_toast("Planner System", "System Has Started!", duration = 5, icon_path="Logo.ico")

                

if __name__ == "__main__":
    t1 = mt.Process(target=main)
    t2 = mt.Process(target=hwcheck)
    t3 = mt.Process(target=notification)

    t1.start()
    t2.start()
    t3.start()

#2020 ThatCodeAddict
