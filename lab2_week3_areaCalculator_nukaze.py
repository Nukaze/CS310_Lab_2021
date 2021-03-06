#===========================================#
#  LAB02_Week3_Anupun_Khumthong_1640705560  #
#===========================================#
#Area Calculator Program #nukaze-
#frontarea
print("#=================================================#")
print("#             Area Calculator Program             #")
print("#=================================================#")
print("#  Shape code list :                              #")
print("#    [R] Rectangle                                #")
print("#    [T] Trapezoid                                #")
print("#    [P] Parallelogram                            #")
print("#    [C] Circle                                   #")
print("#=================================================#")
anglecode = input("Select Code [R, T, P, C]: ")
#Rectangle
if anglecode.upper() == "R":
  print("You Select [R] Rectangle")
  print("===================================================")
  print("                Area of Rectangle")
  print("===================================================")
  print("Inputs width and height in cm. or m.")
  unitcode = input("Select a unit code 1[cm.] or 2[m.] : ")
  if unitcode == "1":
    width = float(input("Enter width [cm.]: "))
    height = float(input("Enter height [cm.]: "))
    rectarea  =  width * height
    print("===================================================")
    print("             Rectacgle Area = %.2f cm2" %(rectarea))
    print("===================================================")
  elif unitcode == "2":
    width = float(input("Enter width  [m.]: "))
    height = float(input("Enter height [m.]: "))
    rectarea  =  width * height
    print("===================================================")
    print("             Rectacgle Area = %.2f m2" %(rectarea))
    print("===================================================")
  else: print("Wrong unit code! please try again.")

#Trapezoid
elif anglecode.upper() == "T":
  print("You Select [T] Trapezoid")
  print("===================================================")
  print("                 Area of Trapezoid")
  print("===================================================")
  print("Inputs parallel sides and height in cm. or m.")
  unitcode = input("Select a unit code 1[cm.] or 2[m.] : ")
  if unitcode == "1":
    prlA = float(input("Enter parallel side A [cm.]: "))
    prlB = float(input("Enter parallel side B [cm.]: "))
    height = float(input("Enter height [cm.]: "))
    trapzarea  =  (prlA + prlB) * 0.5 * height
    print("===================================================")
    print("             Trapezoid Area = %.2f cm2" %(trapzarea))
    print("===================================================")
  elif unitcode == "2":
    prlA = float(input("Enter parallel side A [m.]: "))
    prlB = float(input("Enter parallel side B [m.]: "))
    height = float(input("Enter height [m.]: "))
    trapzarea  =  (prlA + prlB) * 0.5 * height
    print("===================================================")
    print("             Trapezoid Area = %.2f m2" %(trapzarea))
    print("===================================================")
  else: print("Wrong unit code! please try again.")

#Parallelogram
elif anglecode.upper() == "P":
  print("You Select [P] Parallelogram")
  print("===================================================")
  print("               Area of Parallelogram")
  print("===================================================")
  print("Inputs base and height in cm. or m.")
  unitcode = input("Select a unit code 1[cm.] or 2[m.] : ")
  if unitcode == "1":
    base = float(input("Enter base [cm.]: "))
    height = float(input("Enter height [cm.]: "))
    prlarea  =  base * height
    print("===================================================")
    print("            Parallelogram Area = %.2f cm2" %(prlarea))
    print("===================================================")
  elif unitcode == "2":
    base = float(input("Enter base [m.]: "))
    height = float(input("Enter height [m.]: "))
    prlarea  =  base * height
    print("===================================================")
    print("            Parallelogram Area = %.2f m2" %(prlarea))
    print("===================================================")
  else: print("Wrong unit code! please try again.")

#Circle
elif anglecode.upper() == "C":
  print("You Select [C] Circle")
  print("===================================================")
  print("                  Area of Circle")
  print("===================================================")
  print("Inputs radius in cm. or m.")
  unitcode = input("Select a unit code 1[cm.] or 2[m.] : ")
  if unitcode == "1":
    radius = float(input("Enter base [cm.]: "))
    cirarea  =  22/7 * radius ** 2
    print("===================================================")
    print("             Circle Area = %.2f cm2" %(cirarea))
    print("===================================================")
  elif unitcode == "2":
    radius = float(input("Enter radius [m.]: "))
    cirarea  =  22/7 * radius ** 2
    print("===================================================")
    print("             Circle Area = %.2f m2" %(cirarea))
    print("===================================================")
  else: print("Wrong unit code! please try again.")
#out
else: print("You select [%s] is Invalid shape code\nPlease try again." %(anglecode.upper()))
