# Week6 Lab5 Anupun Khumthong 1640705560
# CS310 127G #nukaze- # Grade calculator
# Try catch error like a other grade letter or space bar input
def main_subjectgpa():
    count = 1
    #loopsubject
    try:
        amountsj= int(input("Enter Subject Amount : "))
        print("You have %d Subject Amount" %amountsj)
        for run in range(amountsj):
            print("_" * 64)
            subject = input("Enter Subject [%d] : " % count)
            sjlist.append(subject),wsjlist.append(subject)
            credito = int(input("Enter Credit : "))
            crlist.append(credito),wcrlist.append(credito)
            stat = input("Enter Grade : ")
            stlist.append(stat),wstlist.append(stat)
            if stat.upper() == "W":
                sjlist.remove(subject)
                crlist.remove(credito)
                stlist.remove(stat)
            count += 1
    except ValueError:              # catch error n clear list data
        sjlist.clear(), crlist.clear(), stlist.clear()
        wsjlist.clear(), wcrlist.clear(), wstlist.clear()
        print("x"* 64,"")
        print(inpvalid.center(64))
        print("x"*64,"\n")
        main_subjectgpa()
    #end collect next to calculate
    stlen = len(stlist)             # var len list to int num for loop
    for run in range(stlen):
        try:
            if stlist[run].upper() == "F":
                rawgrade = crlist[run] * 0
                rawlst.append(rawgrade)
            elif stlist[run].upper() == "D":
                rawgrade = crlist[run] * 1.0
                rawlst.append(rawgrade)
            elif stlist[run].upper() == "D+":
                rawgrade = crlist[run] * 1.5
                rawlst.append(rawgrade)
            elif stlist[run].upper() == "C":
                rawgrade = crlist[run] * 2.0
                rawlst.append(rawgrade)
            elif stlist[run].upper() == "C+":
                rawgrade = crlist[run] * 2.5
                rawlst.append(rawgrade)
            elif stlist[run].upper() == "B":
                rawgrade = crlist[run] * 3.0
                rawlst.append(rawgrade)
            elif stlist[run].upper() == "B+":
                rawgrade = crlist[run] * 3.5
                rawlst.append(rawgrade)
            elif stlist[run].upper() == "A":
                rawgrade = crlist[run] * 4.0
                rawlst.append(rawgrade)
            elif stlist[run].upper() == " ":                # catch error spacebar input make trouble
                sjlist.clear(), crlist.clear(), stlist.clear()
                wsjlist.clear(), wcrlist.clear(), wstlist.clear()
                rawlst.clear()
                print("x" * 64, )
                print(wrongalpha.center(64))
                print("x" * 64, "\n")
                main_subjectgpa()
            else:                                           # catch other error
                sjlist.clear(), crlist.clear(), stlist.clear()
                wsjlist.clear(), wcrlist.clear(), wstlist.clear()
                rawlst.clear()
                print("x" * 64, )
                print(wrongalpha.center(64))
                print("x" * 64, "\n")
                main_subjectgpa()
        except ValueError:
            sjlist.clear(), crlist.clear(), stlist.clear()
            wsjlist.clear(), wcrlist.clear(), wstlist.clear()
            rawlst.clear()

def main_displayprofile(sid,fname,major):
    print("=" * 64)
    print(pgname.center(64))
    print("=" * 64)
    print("Student ID.",sid.capitalize())
    print("Name:", fname.capitalize())
    print("School:",major.capitalize())

def main_displaysubject():
    sjtable = "|            Subject           |    Credit(s)    |    Grade    |"
    print("=" * 64)
    print(sjtable.center(64))
    print("=" * 64)
    wsjlen = len(wsjlist)
    rcount = 1
    for run in range(wsjlen):
        dispwsj = str(wsjlist[run])
        dispwcr = str(wcrlist[run])
        dispwst = str(wstlist[run])
        print(dispwsj.ljust(32).capitalize(), dispwcr.center(16), dispwst.upper().center(16))
        rcount += 1

def main_gpadisplay():
    gpadisplay = ("\\\\\\\\\   GPA %.2f   /////" %gpax)
    print("=" * 64)
    print(gpadisplay.center(64))
    print("=" * 64)


#mainVariable
count = 1
sid,fname,major = (""),(""),("")                #displayprofile
gpax,rawgrade = float(),float()                 #vardef_gpa_calculate
sjlist,crlist,stlist,rawlst = [],[],[],[]       #listdef_gpa_alculate
wsjlist,wcrlist,wstlist = [],[],[]              #listdef_rDisplayTable
#varMessage
welcome = "++++  Welcome to Grade Calculator  ++++"
pgname = "||||  Grade Calculator  ||||"
wrongalpha = "Wrong Grade alphabet!! Please try again."
inpvalid = "Error Invalid input!! Please Enter try again."
#mainStatement
print("=" * 64)
print(welcome.center(64))
print("=" * 64)
sid = input("Enter student's ID: ")
fname = input("Enter student's name: ")
major = input("Enter student's faculty: ")
print("<>"*32)
main_subjectgpa()
gpax = sum(rawlst) / sum(crlist)
main_displayprofile(sid, fname, major)
main_displaysubject()
main_gpadisplay()
print("<>"*32)