# CS310 127G Week7 Lab6 Anupun Khumthong 1640705560
#Employee information management Program  #nukaze-
uidlst, allnamelst, userlst, keylst = [], [], [], []
uid, name, fname, keyword = "","","",""
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
    print("+ + + REGISTER EMLOYEE + + +".center(64))
    print("+"*64)
    fname = input("Enter Name Surname: ")
    uid = (input("Enter ID card [13 digits]: "))
    while len(uid) != 13:
        print("Invalid ID card ")
        uid = (input("Enter ID card [13 digits]: "))
        print(len(uid))
    uidlst.append(uid)
    allnamelst.append(fname)
    #fname =
    #username = nam
    #ukey =
    #userlst.append()
    #keylst.append()
    print(uid)
    print(uidlst)
    print("Register Complete.")
    emp_main()


def emp_del():
    print("-" * 64)
    print("- - - DELETE EMLOYEE - - -".center(64))
    print("-" * 64)

    emp_main()


def emp_data():
    print("*" * 64)
    print("* * * SHOW DATA EMLOYEE * * *".center(64))
    print("*" * 64)
    if uidlst:
        for run in range(len(uidlst)):
            print("No.".center())
            print([run] + allnamelst[run] + uidlst[run])
    else:
        print("." * 64)
        print(" " * 64)
        print("No Data Found!".center(64))
        print("Please Register Data before Checking.".center(64))
        print(" " * 64)
        print("." * 64)



    emp_main()


emp_main()