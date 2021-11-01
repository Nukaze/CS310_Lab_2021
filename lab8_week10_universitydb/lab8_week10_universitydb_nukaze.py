# CS310 127G Week09 Lab7 Anupun Khumthong 1640705560
# university database Program  #nukaze-
import time
def loadprogress():
    input("> Press any key to analysis raw data to University database ")
    print("> [ Analysing Data.. ]")
    t = 5
    print("> [",end="")
    for i in range(t):
        time.sleep(0.5)
        loadprogress = "■"*i*5
        print("%s"%loadprogress,end="")
    print("]")
    time.sleep(1)
    print("> [ 100% Database Analysis Successfully. ]")

def genderCal():
    std.split()
    if data[-1].upper() == "F":
        dbfemale.write(std)
    elif data[-1].upper() == "M":
        dbmale.write(std)


def yearCal():
    cnt = 0
    data[4]

"""
dby1 = open('year1stdlst.txt','w+')
dby2 = open('year2stdlst.txt','w+')
dby3 = open('year3stdlst.txt','w+')
dby4 = open('year4stdlst.txt','w+')
dbyetc = open('yearetcstdlst.txt','w+')
"""
with open('stdlst.txt','r') as dbstd:
    dbmale = open('malestdlst.txt', 'w+')
    dbfemale = open('femalestdlst.txt', 'w+')
    dbrmale = open('malestdlst.txt', 'r')
    dbrfemale = open('femalestdlst.txt', 'r')
    line = dbstd.read().splitlines()
    print("line = ",line,end="\n")
    qtyfemale,qtymale = 0,0
    for std in line:
        data = std.split()
        std.split()
        if data[-1].upper() == "F":
            dbfemale.write(std+'\n')
            qtyfemale += 1
        elif data[-1].upper() == "M":
            dbmale.write(std+'\n')
            qtymale += 1
    dbfemale.write("Total female students = {}".format(qtyfemale))
    dbmale.write("Total male students = {}".format(qtymale))
    dbmale.close()
    dbfemale.close()


with open('femalestdlst.txt','r') as dbfemale:
    line = dbfemale.read().splitlines()
    print("\n\nline female = ",line,end="\n")
    for std in line:
        print(std)
    #print("Total Female Students = {}\n".format(len(line)))

with open('malestdlst.txt', 'r') as dbmale:
    line = dbmale.read().splitlines()
    print("line male = ",line,end="")
    for std in line:
        print(std)
    #print("Total Male Students = {}\n".format(len(line)))