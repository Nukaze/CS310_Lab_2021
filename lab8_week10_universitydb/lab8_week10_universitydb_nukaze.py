# CS310 127G Week09 Lab7 Anupun Khumthong 1640705560
# university database Program  #nukaze-
import time

def loadprogress():
    input("> Press any key to analysis raw data to University database ")
    print("> [ Analysing Data.. ]")
    t = 5
    print("> [",end="")
    for i in range(t):
        time.sleep(0.25)
        loadprogress = "■"*i*5
        print("%s"%loadprogress,end="")
    print("]")
    time.sleep(1)
    print("> [ 100% Database Analysis Successfully. ]")

def show_femaletable():
    with open('femalestdlst.txt','r') as dbfemale:
        line = dbfemale.read().splitlines()
        print("\n\nline female = ",line,end="\n")
        for std in line:
            print(std)
        print("Total Female Students = {}\n".format(len(line)))

def show_maletable():
    with open('malestdlst.txt', 'r') as dbmale:
        line = dbmale.read().splitlines()
        print("line male = ",line,end="")
        for std in line:
            print(std)
        print("Total Male Students = {}\n".format(len(line)))

def show_y1table():
    with open('year1stdlst.txt', 'r') as dby1:
        line = dby1.read().splitlines()
        print("line male = ",line,end="")
        for std in line:
            print(std)
        print("Total Year 1st Students = {}\n".format(len(line)))

def show_y2table():
    with open('year2stdlst.txt', 'r') as dby2:
        line = dby2.read().splitlines()
        print("line 2nd = ",line,end="")
        for std in line:
            print(std)
        print("Total Year 2nd Students = {}\n".format(len(line)))

def show_y3table():
    with open('year3stdlst.txt', 'r') as dby3:
        line = dby3.read().splitlines()
        print("line 3rd = ",line,end="")
        for std in line:
            print(std)
        print("Total Year 3rd Students = {}\n".format(len(line)))

def show_y4table():
    with open('year4stdlst.txt', 'r') as dby4:
        line = dby4.read().splitlines()
        print("line 4th = ",line,end="")
        for std in line:
            print(std)
        print("Total Year 4th Students = {}\n".format(len(line)))

def show_yetctable():
    with open('yearetcstdlst.txt', 'r') as dbyetc:
        line = dbyetc.read().splitlines()
        print("line etc = ",line,end="")
        for std in line:
            print(std)
        print("Total Others year Students = {}\n".format(len(line)))


loadprogress()
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
    dbfemale.write("Total female students = {}".format(qtyfemale))
    dbmale.write("Total male students = {}".format(qtymale))
    dby1.write("Total Student = {}".format(qtyy1))
    dby2.write("Total Student = {}".format(qtyy2))
    dby3.write("Total Student = {}".format(qtyy3))
    dby4.write("Total Student = {}".format(qtyy4))
    dbyetc.write("Total Student = {}".format(qtyyetc))

    dbmale.close();dbfemale.close()
    dby1.close();dby2.close();dby3.close();dby4.close();dbyetc.close()

