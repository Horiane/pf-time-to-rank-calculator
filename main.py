#made by u/icantnotbreathe, suggestions by u/drift7rs
#feel free to copy!
#imports
from math import trunc
from sys import exit

#inputs
playerRank=int(input("Your current rank: "))
goalRank=int(input("Your target rank: "))
avgXP=int(input("Your average xp per match: ")) #average xp earned per game
avgHours=int(input("Your average hours per day: ")) #time played each day

if avgHours>24:
    print("How did you play phantom forces more than 24 hours a day?")
    exit()

totalXPneeded=0 #declare varible to avoid complier issues
i=playerRank #Setting the starting rank to calculate

#calculation
for i in range(goalRank-playerRank): #loop to calc the xp needed by going from player rank - goal rank
    totalXPneeded=totalXPneeded+((i+1)*1000) #a "equation"
    i=+1
matchesNeeded=totalXPneeded/avgXP #matches needed
timeNeeded=matchesNeeded*930 #15 minutes=900 seconds + 30 seconds intermission

realtime=(timeNeeded/3600)/avgHours #calc days needed to realisticly get to targeted rank

#making seconds into days hours minutes
days=timeNeeded//86400
hours=(timeNeeded-(days*86400))//3600
minutes=(timeNeeded-(days*86400)-(hours*3600))//60

#"rounding" the numbers
days=trunc(days)
hours=trunc(hours)
minutes=trunc(minutes)

#output
print(f"{realtime} days of grinding")

#i hate this if if if mess, its basicly just displaying required parameters
if minutes==0:
    print(f"{days} days and {hours} hours of continuous grinding")
elif hours==0:
    print(f"{days} days and {minutes} minutes of continuous grinding")
elif minutes==0 and hours==0:
    print(f"{days} days of continuous grinding")
else:
    print(f"{days} days, {hours} hours and {minutes} minutes of continuous grinding")
