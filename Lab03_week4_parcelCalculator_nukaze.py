# CS310_127G_Anupun_Khumthong_1640705560
# Week_04_Lab03 #nukaze-
# function
def desti_display():
    # destination
    print("%s" % ("-" * 60))
    print("| Destination:%s|" % (" " * 45))
    print("|    [BK] The Bangkok Metropolitan Region%s|" % (" " * 18))
    print("|    [TH] For areas in other provinces%s|" % (" " * 21))
    print("%s" % "-" * 60)

def desti_table():
    # table
    print("\n%s" % ("-" * 60))
    print("|       Weight        |       BK        |       TH         |")
    print("%s" % ("-" * 60))
    print("|       1 - 5         |       80        |       140        |")
    print("|       6 - 10        |      150        |       200        |")
    print("|        10+          |      200        |       250        |")
    print("%s" % ("-" * 60))

def parcel_calculate():
    # condition loop
    desti = input("Enter destination          : ")
    # BKK-Ship
    if desti.upper() == "BK":
        weight = float(input("Enter total weight [KG]    : "))
        if (type(weight)) == float:
            print("%.2f" % float(weight))
            if weight > 10:
                ship = 200
                desti_table()
                total_display(orderTotal,discount,ship)
            elif float(weight) >= 6 and weight <=10:
                ship = 150
                desti_table()
                total_display(orderTotal,discount,ship)
            elif float(weight) >= 1 and weight <= 5:
                ship = 80
                desti_table()
                total_display(orderTotal,discount,ship)
        else:
            print("Invalid weight input")
    # TH-Ship
    elif desti.upper() == "TH":
        try:
            weight = float(input("Enter total weight [KG]    : "))
            if (type(weight)) == float:
                if weight > 10:
                    ship = 250
                    desti_table()
                    total_display(orderTotal,discount,ship)
                elif float(weight) >= 6 and weight <= 10:
                    ship = 200
                    desti_table()
                    total_display(orderTotal,discount,ship)
                elif float(weight) >= 1 and weight <= 5:
                    ship = 140
                    desti_table()
                    total_display(orderTotal,discount,ship)
            else:
                print("Weight Can not be negative number")
        except ValueError: print("Invalid weight input! Please try again.")
    else:
        print("invalid Destination Code! Please try again.")

def total_display(orderTotal,discount,ship):
    # displayTotal
    print("Order Total  :   %7.2f" % orderTotal)
    print("Shipping     :   %7.2f" % ship)
    print("Discount     :  -%7.2f" % discount)
    print("%s" %("-" * 40))
    print("Total        :   %7.2f"%(orderTotal + ship - discount))
    print("%s" %("-" * 40))

# Header Program
print("%s" %("="*60))
print("|%s*** Order Summary ***%s|"%(" "*18," "*19))
print("%s" %("="*60))
# Main condition
try:
    orderTotal = float(input("Enter Order total : "))
    ship = 0
    if float(orderTotal) >= 5000:
        discount = 120
        desti_display()
        parcel_calculate()
    elif float(orderTotal) >= 3000 and orderTotal <= 5000:
        discount = 60
        desti_display()
        parcel_calculate()
    elif float(orderTotal) < 3000 and orderTotal >= 0:
        discount = 0
        desti_display()
        parcel_calculate()
    elif float(orderTotal) < 0:
        print("Invalid Order total can not be negative! Please try again.")
except ValueError: print("Invalid Order total input! Please try again.")
