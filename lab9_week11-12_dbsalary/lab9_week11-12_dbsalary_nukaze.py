# CS310 127G Week11-12 Lab8 Anupun Khumthong 1640705560
# university database Program  #nukaze-
import os
wid,name,sname,tier,salary,sale,income = [],[],[],[],[],[],[]
uicls = lambda: os.system('cls')
def getdata():
    with open('profile.txt','r') as profiletxt:
        while True:
            dbprofile = profiletxt.readline().split()
            if dbprofile == []:
                break
            else:
                wid.append(dbprofile[0])
                name.append(dbprofile[1])
                sname.append(dbprofile[2])
                tier.append(dbprofile[3])
                salary.append(float(dbprofile[4]))
                sale.append(float(dbprofile[5]))
                income.append(float(dbprofile[4])+float(dbprofile[5])*0.1)
        #print(wid,"\n", name,"\n",sname,"\n",tier,"\n", salary, "\n", sale, "\n", income)

def writedatafile():
    dbptime = open('parttime.txt','w+')
    dbftime = open('fulltime.txt','w+')
    netftotal,netptotal = 0,0
    headrow = ("ID".center(4)+"NAME".center(14)+"SURNAME".center(12)+"SALARY".rjust(18)+"SALE".rjust(13)+"INCOME".rjust(13))
    headline = "="*80
    dbftime.write("%s\n"%headline+"[ Show income employee full-time ]".center(78) + ("\n\n%s\n%s\n") %(headrow,headline))
    dbptime.write("%s\n"%headline+"[ Show income employee part-time ]".center(78) + ("\n\n%s\n%s\n") %(headrow,headline))
    for run in range(len(wid)):
        if tier[run] == "F":
            netftotal += income[run]
            dbftime.write("%-8s %-10s %-15s %12.2f %12.2f %12.2f\n"
                          %(wid[run], name[run], sname[run],salary[run], sale[run], income[run]))
        elif tier[run] == "P":
            netptotal += income[run]
            dbptime.write("%-8s %-10s %-15s %12.2f %12.2f %12.2f\n"
                          %(wid[run], name[run], sname[run],salary[run], sale[run], income[run]))
        else: print("Out of work tier.")
    dbftime.write(headline+"\n# Total Full-time networth = %12.2f\n" %netftotal)
    dbptime.write(headline+"\n# Total Part-time networth = %12.2f\n" %netptotal)
    dbptime.close()
    dbftime.close()
    print(" < Getdata complete. >")

def show_menuincome():
    m = input(" < Select the menu below >\n[A] Show all table\n[F] Full-time income\n[P] Part-time income\n[x] exit\n> ")
    menu = m.upper()
    uicls()
    if menu == "A":
        uicls()
        show_ftimeincome()
        show_ptimeincome()
        navigate()
    elif menu == "F":
        show_ftimeincome()
        navigate()
    elif menu == "P":
        show_ptimeincome()
        navigate()
    elif menu == "X":
        quit("exiting..")
    else: print("[%s] Invalid menu "%menu);show_menuincome()

def show_ftimeincome():
    with open('fulltime.txt','r') as dbftime:
        data = dbftime.read()
        print(data)

def show_ptimeincome():
    with open('parttime.txt','r') as dbptime:
        data = dbptime.read()
        print(data)

def navigate():
    nav = input("Prees any key to back the menu or Select [x] to exit\n> ")
    if nav.upper() == "X":
        quit("exiting..")
    else: uicls();show_menuincome()

getdata()
writedatafile()
show_menuincome()