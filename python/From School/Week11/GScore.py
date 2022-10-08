'''
ScoreLister v1.42
Lee Zhi Wei
29/6/22
'''
player =['Hafu', 'Toast', 'Pokimane', 'Pewdiepie', 'Ninja','Markiplier'] #Namelist
results = [[98, 107, 87, 121],[88, 111],[79, 130, 99],[86, 100, 121, 66, 98],[108, 79, 92],[77, 126, 93, 100, 73, 89]] #resultlist
finallist = [] #Finallist var
for scores in results: #Score sorting
    plays = len(scores) #Plays calc using len
    wins = 0 #Reset win every loop
    tscore = 0 #Reset totalscore every loop
    for oscore in scores: #Individual score loop
        if oscore >= 100: #If score is more or equal to 100
            wins += 1 #Add one to wins
        tscore += oscore #Adds individual score to totalscore
    finallist.append([plays,wins,tscore]) #Appends results to list via sublist
if len(finallist) == len(player): #Sanity check for list
    print('{:<12}{:<2}{:<6}{:<6}'.format("Player","P","Wins","Total"))#Prints header
    for x in range(len(player)):#Loop to print each result
        print('{:<12}{:<2}{:<6}{:<6}'.format(player[x],finallist[x][0],finallist[x][1],finallist[x][2]))#Prints the results
else: #If length of player and scores dont match
    print("Check list, length not matched") #Print error
'''
#Player list
#for index in range(len(player)):
    #print(player[index])
#List of scores
#for list in results:
    #for score in list:
        #print(score)
#Header
print("{:12} {} {:^4} {:^5}".format("Player","P","Wins","Total"))
#Print player and score list
for index in range(len(player)): #Loop for player
    num_win = 0
    total_score = 0
    for score in results[index]: #Loop for score
        if score >=100: #Score more than equal to 100
            num_win += 1 #Add to number of wins
    total_score += score #Add total score
    #print(player[index],score,len(results[index]),num_wins,total_socre)
    print("{:12} {} {:^4} {:^5}".format(player[index],len(results[index]),num_win,total_score))
'''
