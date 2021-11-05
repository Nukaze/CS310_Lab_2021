# CS310 127G Week10-11 Lab8 Anupun Khumthong 1640705560
# university database Program  #nukaze-
import time
import os

def show_originstudents():
    print("- All original students table -".center(40))
    with open('stdlst.txt','r') as dbstd:
        line = dbstd.read().splitlines()
        for std in line:
            print(std)
        print("Total original Students = {}".format(len(line)))
    print("")

def show_femaletable():
    print("- All Female students table -".center(40))
    with open('femalestdlst.txt','r') as dbfemale:
        line = dbfemale.read().splitlines()
        for std in line:
            print(std)
        ###print("Total Female Students = {}\n".format(len(line))) work
    print("")

def show_maletable():
    print("- All Male students table -".center(40))
    with open('malestdlst.txt', 'r') as dbmale:
        line = dbmale.read().splitlines()
        for std in line:
            print(std)
        ###print("Total Male Students = {}\n".format(len(line))) work
    print("")

def show_y1table():
    print("- All 1st year students table -".center(40))
    with open('year1stdlst.txt', 'r') as dby1:
        line = dby1.read().splitlines()
        for std in line:
            print(std)
    print("")

def show_y2table():
    print("- All 2nd year students table -".center(40))
    with open('year2stdlst.txt', 'r') as dby2:
        line = dby2.read().splitlines()
        for std in line:
            print(std)
    print("")

def show_y3table():
    print("- All 3rd year students table -".center(40))
    with open('year3stdlst.txt', 'r') as dby3:
        line = dby3.read().splitlines()
        for std in line:
            print(std)
    print("")

def show_y4table():
    print("- All 4th year students table -".center(40))
    with open('year4stdlst.txt', 'r') as dby4:
        line = dby4.read().splitlines()
        for std in line:
            print(std)
    print("")

def show_yetctable():
    print("- All other year students table -".center(40))
    with open('yearetcstdlst.txt', 'r') as dbyetc:
        line = dbyetc.read().splitlines()
        for std in line:
            print(std)
    print("")

def show_menu():
    uiclear()
    print("[ Bangkok University database ]\n - Please select menu below")
    print("[X] End Program\n[A] All Table\n[M] Male Table \n[F] Female Table\n[1] Year 1\n[2] Year 2\n[3] Year 3 \n[4] Year 4\n[0] Other Year \n")
    m = input("Enter your menu > ")
    menu = m.upper()
    uiclear()
    print("- You Choose [%s] Menu -"%menu)
    if menu == "A":
        show_originstudents()
        show_maletable()
        show_femaletable()
        show_y1table()
        show_y2table()
        show_y3table()
        show_y4table()
        show_yetctable()
        navigate()
    elif menu == "M":
        show_maletable()
        navigate()
    elif menu == "F":
        show_femaletable()
        navigate()
    elif menu == "1":
        show_y1table()
        navigate()
    elif menu == "2":
        show_y2table()
        navigate()
    elif menu == "3":
        show_y3table()
        navigate()
    elif menu == "4":
        show_y4table()
        navigate()
    elif menu == "0":
        show_yetctable()
        navigate()
    elif menu == "X":
        quit("Exiting..")
    else:
        print("Invalid menu! Please try again.")
        time.sleep(2.5)
        show_menu()

def navigate():
    nav = input("Press any key to back to the menu or Press [x] to exit the program\n> ")
    if nav.upper() == "X":
        uiclear()
        quit("Exiting..")
    else:
        show_menu()

uiclear = lambda: os.system('cls')
with open('stdlst.txt','r') as dbstd:
    qtyfemale, qtymale = 0, 0
    qtyy1, qtyy2, qtyy3, qtyy4, qtyyetc = 0, 0, 0, 0, 0
    dbmale = open('malestdlst.txt', 'w');dbfemale = open('femalestdlst.txt', 'w')
    dby1 = open('year1stdlst.txt', 'w')
    dby2 = open('year2stdlst.txt', 'w')
    dby3 = open('year3stdlst.txt', 'w')
    dby4 = open('year4stdlst.txt', 'w')
    dbyetc = open('yearetcstdlst.txt', 'w')
    line = dbstd.read().splitlines()
    for std in line:
        data = std.split()
        std.split()
        #gender
        if data[-1].upper() == "F":
            dbfemale.write(std + '\n')
            qtyfemale += 1
        if data[-1].upper() == "M":
            dbmale.write(std + '\n')
            qtymale += 1
        #year
        if int(data[4]) == 1:
            dby1.write(std + '\n')
            qtyy1 += 1
        if int(data[4]) == 2:
            dby2.write(std + '\n')
            qtyy2 += 1
        if int(data[4]) == 3:
            dby3.write(std + '\n')
            qtyy3 += 1
        if int(data[4]) == 4:
            dby4.write(std + '\n')
            qtyy4 += 1
        if int(data[4]) > 4 or int(data[4]) < 1:
            dbyetc.write(std + '\n')
            qtyyetc += 1
    #writeppl
    dbfemale.write("Total Female students = {}".format(qtyfemale))
    dbmale.write("Total Male students = {}".format(qtymale))
    dby1.write("Total 1st year Students = {}".format(qtyy1))
    dby2.write("Total 2nd year Students = {}".format(qtyy2))
    dby3.write("Total 3rd year Students = {}".format(qtyy3))
    dby4.write("Total 4th year Students = {}".format(qtyy4))
    dbyetc.write("Total Other year Students = {}".format(qtyyetc))
    #close dbfile
    dbmale.close();dbfemale.close()
    dby1.close();dby2.close();dby3.close();dby4.close();dbyetc.close()
show_menu()