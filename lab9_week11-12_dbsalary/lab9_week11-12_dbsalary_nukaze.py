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
                print("- Out of data Profile Database -")
                break
                #quit("Exiting")
            else:
                wid.append(dbprofile[0])
                name.append(dbprofile[1])
                sname.append(dbprofile[2])
                tier.append(dbprofile[3])
                salary.append(float(dbprofile[4]))
                sale.append(float(dbprofile[5]))
                income.append(float(dbprofile[4])+float(dbprofile[5])*0.1)
        print(wid,"\n", name,"\n",sname,"\n",tier,"\n", salary, "\n", sale, "\n", income)



def writedatafile():
    dbptime = open('parttime.txt','w+')
    dbftime = open('fulltime.txt','w+')
    netftotal,netptotal = 0,0
    headrow = "NAME SURNAME SALARY SALE INCOME\n ==== ====== ====== ==== ======\n"
    for run in range(len(wid)):
        dbftime.write("[ Show income employee full-time ]".center(64)+("\n%s") %headrow)
        dbptime.write("[ Show income employee part-time ]".center(64)+("\n%s") %headrow)
        if tier[run] == "F":
            print(tier[run])
            netftotal += income[run]
            #print("%6s %6s %6s %7.2f %7.2f %7.2f"%(wid[run],name[run],sname[run], salary[run],sale[run],income[run]))
            dbftime.write("%6s %6s %6s %7.2f %7.2f %7.2f"%(wid[run], name[run], sname[run],salary[run], sale[run], income[run]))
        elif tier[run] == "P":
            print(tier[run])
            netptotal += income[run]
            #print("%6s %6s %6s %7.2f %7.2f %7.2f"%(wid[run], name[run], sname[run],salary[run], sale[run], income[run]))
            dbftime.write("%6s %6s %6s %7.2f %7.2f %7.2f"%(wid[run], name[run], sname[run],salary[run], sale[run], income[run]))
    print("Total Fulltime networth = %7.2f" %netftotal)
    print("Total Parttime networth = %7.2f" %netptotal)
    dbptime.close()
    dbftime.close()


getdata()
input("Getdata complete. Press any key to show table.")
uicls()
writedatafile()