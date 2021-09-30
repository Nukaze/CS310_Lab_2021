# CS310 127G Week7 Lab6 Anupun Khumthong 1640705560
# BU Restaurant Program #nukaze-
#uiprint
uidot = "."*64;uibures = "BU Restaurant".center(64);uiheadmenu = "Menu"
uimenuid = "Menu ID".center(16);uimenuprice = "Price".center(16)
#listvar
menuidlst = ["F01","F02","F03","F04","D01","D02"]
foodlst = ["F01","F02","F03","F04"]
menunamelst = ["Pan Fried Egg","Grilled Sandwich","Spagheti Olio","Caesar Salad","Coffee","Soft Drink"]
menupricelst = [125.00,145.00,169.00,139.00,120.00,90.00]
inidnamelst = [];inquanlst = [];inpricelst = [];inmnlst = []
qtyidlst = [0 for wid in menuidlst]         #pointer list
yesnolst = ["Y","N"]                        #Yes and No

def main_uiheader():
    print(uidot)
    print(uibures)
    print(uiheadmenu.center(64))
    print(uidot)
    print(uimenuid+uiheadmenu.center(32)+uimenuprice)
    for run in range(len(menuidlst)):
        print(menuidlst[run].center(16),"".center(6),menunamelst[run].ljust(26),("%5.0f").center(10) %menupricelst[run])
    print(uidot)

#inputLoop
def main_whilerun():
    wrun, c = 1, 1
    wquit = ""
    while wquit != "Y":
        try:
            print("#",c)
            wid = input("Enter Menu ID: ").upper()
            while not wid in menuidlst:             # check wid in menuidlst
                print("x" * 64)
                print("Invalid menu id!!, Please Try again.")
                print("x" * 64)
                print("#",c)
                wid = input("Enter Menu ID: ").upper()
            qty = int(input("Enter Quantity: "))
            widprice = menuidlst.index(wid)                 #wid index price in lst
            qtyidlst[widprice] = qtyidlst[widprice] + qty   #append qty in pointer id
            wquit = input("Quit? (Y/N): ").upper()
            while not wquit in yesnolst:                    #Catch Y and N only
                wquit = input("Quit? (Y/N): ").upper()
        except ValueError:
                print("x"*64)
                print("Invalid input, Please Try again.".center(64))
                print("x"*64)
                wrun, c = 1, 1
                inidnamelst.clear();inquanlst.clear()
                main_uiheader()
        c += 1
    bumember = input("BU Member Card (Y/N): ").upper()
    while not yesnolst:
        bumember = input("BU Member Card (Y/N): ").upper()
    sumfprice,sumdprice = 0,0
    run = 0
    print(uidot)
    print(uibures)
    print(uiheadmenu.center(64))
    print(uidot)
    print(uiheadmenu.center(26) + "QTY".center(20) + uimenuprice)
    while run < len(qtyidlst):
        if qtyidlst[run] > 0:
            qprice = qtyidlst[run] * menupricelst[run]      # qty price per menu
            print(str(menunamelst[run]).ljust(26)+str(qtyidlst[run]).center(20)+"%d".center(16)%qprice)
            if menuidlst[run] in foodlst:
                sumfprice += qprice         #find food price
            else:
                sumdprice += qprice         #find drink price
        run += 1
    print(uidot)
    memdiscount = 0
    if bumember == "Y":
        memdiscount = sumfprice * 0.10      #member food discount only
    fndcost = sumfprice + sumdprice         #summation of food and price
    tax = fndcost * 0.07
    allnet = fndcost + tax - memdiscount
    print("Price".ljust(48)+"%7.2f".rjust(10) %fndcost)
    print("Tax (7%)".ljust(48)+"%7.2f".rjust(10) %tax)
    print("Discount (onlyfood)".ljust(48)+"%7.2f".rjust(10) %memdiscount)
    print(uidot)
    print("Total".ljust(48) + "%7.2f".rjust(10) %allnet)
    print("*"*64)


main_uiheader()
main_whilerun()
print("Have a nice day, Good bye ~~".center(64)+"\n"+"*"*64)
