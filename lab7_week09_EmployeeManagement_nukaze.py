# CS310 127G Week7 Lab6 Anupun Khumthong 1640705560
#Employee information management Program  #nukaze-
uidlst, namelst, snamelst, userlst, keylst = [], [], [], [], []
uid, reqname, fname, name, sname, keyword = "","","","","",""


def emp_main():
    print(("> " * 10 + "Welcome Employee System" + " <" * 10).center(64))
    print("[1] Register Employee")
    print("[2] Delete Employee")
    print("[3] Show Data Employee")
    print("[4] Exit Program")
    selectmenu = input("Please select menu [1-3]: ")
    if selectmenu == "1":
        emp_regis()
    elif selectmenu == "2":
        emp_del()
    elif selectmenu == "3":
        emp_data()
    elif selectmenu == "4":
        exit("Program closing..")
    else:
        print(("x "*32).center(64))
        print(("Sorry Please select menu again").center(64))
        print(("x " *32).center(64))
        emp_main()


def emp_regis():
    print("+"*64)
    print("+ + + REGISTER EMPLOYEE + + +".center(64))
    print("+"*64)
    reqname = input("Enter Name Surname: ")
    fname = reqname.split()
    if len(fname) > 1:                                    #catch
        name = fname[0];namelst.append(name)
        sname = fname[1];snamelst.append(sname)
        username = name+"."+sname[0]                      #genuser
        userlst.append(username)
        ukey = (reqname[1].lower())+(reqname[3].upper())+(reqname[2].upper())+str(len(reqname))+(reqname[4].lower())
        #genkey
        keylst.append(ukey)
        print(namelst)
        print(snamelst)
        print(ukey)
    else:
        print("Required name and surname!! Please try again.")
        emp_regis()
    uid = (input("Enter ID card [13 digits]: "))
    while len(uid) != 13:
        print("Invalid ID card ")
        uid = (input("Enter ID card [13 digits]: "))
    uidlst.append(uid)
    print(uid)
    print(uidlst)
    print("Register Complete.")

    emp_main()


def emp_del():
    print("-" * 64)
    print("- - - DELETE EMPLOYEE - - -".center(64))
    print("-" * 64)
    print(uid)
    print(namelst)
    print(snamelst)
    print(userlst)
    print(keylst)
    delname = input("Enter name employee to delete : ")
    if delname in namelst:
        delindex = namelst.index(delname)
        print("Del index = ",delindex)
        uidlst.pop(delindex)
        namelst.pop(delindex)
        snamelst.pop(delindex)
        userlst.pop(delindex)
        keylst.pop(delindex)
        print(delname+"has been deleted.")
    else:
        print("Invalid name!! Please try again.")
        emp_del()

    emp_main()


def emp_data():
    print("*" * 64)
    print("* * * SHOW DATA EMPLOYEE * * *".center(64))
    print("*" * 64)
    print("#".center(4) + "Name".ljust(12) + "Surname".ljust(12)
          + "Username".center(11) + "Password".center(11) + "ID Card".center(14))
    if uidlst:
        print("=" * 64)
        for run in range(len(uidlst)):
            cnt = str(run+1)
            print(cnt.center(4)+str(namelst[run]).ljust(12)+str(snamelst[run]).ljust(12)
                  +str(userlst[run]).center(11)+str(keylst[run]).center(11)+str(uidlst[run]).center(14))
        print("=" * 64)
    else:
        print("." * 64)
        print(" " * 64)
        print("No Data Found!".center(64))
        print("Please Register Data before Checking.".center(64))
        print(" " * 64)
        print("." * 64)
    emp_main()

emp_main()