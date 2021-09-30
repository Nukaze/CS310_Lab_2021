#CS310 127G Anupun Khumthong 1640705560
#Week05_Lab04_Score_calculator #nukaze-
i,c = 1,1
sclist,scpass_list,sctray= [],[],[]
#header
print("==========================================")
print("    *** Welcome Anupun khumthong *** " )
print("     *** Computer Programming I ***       ")
print("------------------------------------------")
#loopScore
for i in range(10):
        try:
                score = float(input("[%d].Enter your score : " %c))
                sctray.append(score)
                c += 1
        except ValueError: print("Error invalid input! please try again")
sctray.sort(reverse=True)
for score in sctray:
        if score <= 100 and score >= 0:
                sclist.append(score)
for score in sctray:
        if score <= 100 and score >= 50:
                scpass_list.append(score)
#score_condition
#remove out range number

#collect pass std
#pass score list

avg_sclist = sum(sclist) / len(sclist)
avg_scpass = sum(scpass_list) / len(scpass_list)

#result
print("------------------------------------------")
print("            | *** Results *** |")
print("------------------------------------------")
print("Amount of scores :",len(sclist),"number")
print("Average Score : %.2f" %avg_sclist)
print("Highest Score : %.2f" %max(sclist))
print("Lowest Score  : %.2f" %min(sclist))
print("%s" %"="*35)
print("Total Passed Student :",len(scpass_list),"people")
print("Average Passed Score : %.2f" %avg_scpass)
print("%s" %"="*35)
print("Scores list :",sclist)