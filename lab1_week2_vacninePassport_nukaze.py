#################################################
##   CS310 127G Lab01 Week02                   ##
##   Anupun Khumthong 1640705560  nukaze-      ##
#################################################
#input_section
print("======================================")
print("||  Vaccine List                    ||")
print("======================================")
print("| - Astrazeneca                      |")
print("| - Pfizer                           |")
print("| - Moderna                          |")
print("|------------------------------------|")
nvac  = input("|  Enter Vaccine name  : ")
fname = input("|  Enter First name    : ")
lname = input("|  Enter Last name     : ")
yob   = int(input("|  Year of birth       : "))
height= float(input("|  Enter height(meters): "))
weight= float(input("|  Enter weight(kg)    : "))
datevac = input("|  Vaccine Date        : ")

#calculate_process
fullname = fname +" "+ lname   #combineName
age = (2021 - yob)  #yearofbirth
bmi = weight / ( height **2 )   #bmiCalculate

#output_records
print("======================================")
print("  COVID-19 Vaccination Record Card    ")
print("======================================")
print(" Name :",fullname)
print(" Age :",age)
print(" BMI : %.2f" %(bmi))
print(" Height :",height *100 ,"CM")
print(" Weight :",weight,"KG")
print("--------------------------------------")
print(" Vaccine  :",nvac)
print(" 1ST Dose :",datevac)
