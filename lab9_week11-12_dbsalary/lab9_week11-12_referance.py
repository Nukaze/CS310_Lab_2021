id,name,surname,work,salary,sale,income = [],[],[],[],[],[],[]

def getdata ():
    with open("profile.txt","r") as file:
        while True :
            data = file.readline().split()
            print(data)
            if data == []:
                break
            id.append(data[0])
            name.append(data[1])
            surname.append(data[2])
            work.append(data[3])
            salary.append(int(data[4]))
            sale.append(int(data[5]))
            income.append(int(data[4])+(int(data[5])*10/100))
        print(id,"\n",name,"\n",surname,"\n",work,"\n",salary,"\n",sale,"\n",income,"\n")
def writedatafile ():
    outf1 = open("parttime.txt","w")
    outf2 = open("fulltime.txt","w")
    part = 0
    full = 0
    head = " NAME SURNAME SALARY SALE INCOME\n ==== ====== ====== ==== ======\n"
    outf1.write(" - SHOW INCOME EMPLOYEE PARTTIME -\n %s"%head)
    outf2.write(" - SHOW INCOME EMPLOYEE FULLTIME -\n %s"%head)
    for i in range(len(name)):
        if work[i] == "P" :
            part = part + income[i]
            print(part)
            outf1.write("%-10s %-13s %7d %7d %7d\n"
            %(name[i],surname[i],salary[i],sale[i],income[i]))
            outf1.write("================================================\nTotal Income = %d\n"
                        % part)
        else :
            full = full + income[i]
            print(full)
            outf2.write("%-10s %-13s %7d %7d %7d\n"
            %(name[i],surname[i],salary[i],sale[i],income[i]))
            outf2.write("=========================-======================\nTotal Income = %d\n"
            %full)
    outf1.close()
    outf2.close()

getdata()
writedatafile()
print("Getdata Complete....")