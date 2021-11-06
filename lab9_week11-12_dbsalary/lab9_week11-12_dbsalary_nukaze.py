# CS310 127G Week11-12 Lab8 Anupun Khumthong 1640705560
# university database Program  #nukaze-
wid,name,sname,tier,salary,sale,income = [],[],[],[],[],[],[]

def getdata():
    with open('profile.txt','r') as profiletxt:
        while True:
            dbprofile = profiletxt.readline().split()
            print()
            if dbprofile == []:
                print("- No data available in Profile Database -\n\n\n\n")
                input("Press any key to exit.. ")
                quit("Exiting")
            else:

                wid.append(dbprofile[0])
                name.append(dbprofile[1])
                sname.append(dbprofile[2])
                tier.append(dbprofile[3])
                salary.append(float(dbprofile[4]))
                sale.append(float(dbprofile[5]))
                income.append(float(dbprofile[4])+float(dbprofile[5])*0.1)
                print(wid,"\n", name,"\n",sname,"\n",tier,"\n", salary, "\n", sale, "\n", income, "\n")

                print("getdata complete")


def writedatafile():
    dbptime = open('parttime.txt','w')
    dbftime = open('fulltime.txt','w')
    netw = 0
    for run in range(len(wid)):
        if tier[run] == "F":

            netw += income[run]




    dbptime.close()
    dbftime.close()


getdata()
writedatafile()