print("%7.2f" %71544818181.1819)




order = int(input("Enter order: "))
if order >= 3000 and order <=5000:
    dis = 120
elif order >= 3000 and order <=5000:
    dis = 60
else:
    dis = 0
###############
des = input("Enter dest : ")
if des.upper() == "BK":
    w = float(input("Enter wei :"))
    print("\n%s" % ("-" * 60))
    print("|       Weight        |       BK        |       TH         |")
    print("%s" % ("-" * 60))
    print("|       1 - 5         |       80        |       140        |")
    print("|       6 - 10        |      150        |       200        |")
    print("|        10+          |      200        |       250        |")
    print("%s" % ("-" * 60))
    if w >= 1 and w <=5:
        shipping = 80
    elif w >= 6 and w <= 10:
        shipping =150
    elif w >= 6 and w <= 10:
        shipping =200
    else:shipping = 0


elif des.upper() == "TH":
    w = float(input("Enter wei :"))
    print("\n%s" % ("-" * 60))
    print("|       Weight        |       BK        |       TH         |")
    print("%s" % ("-" * 60))
    print("|       1 - 5         |       80        |       140        |")
    print("|       6 - 10        |      150        |       200        |")
    print("|        10+          |      200        |       250        |")
    print("%s" % ("-" * 60))
    if w >= 1 and w <=5:
        shipping = 120
    elif w >= 6 and w <= 10:
        shipping =200
    elif w >= 6 and w <= 10:
        shipping =300
    else:shipping = 0
net = order + shipping + dis
print("",net)
