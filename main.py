#made by u/icantnotbreathe
#feel free to copy!
#imports
from math import trunc

#inputs
playerRank=int(input("Your current rank:"))
goalRank=int(input("Your target rank:"))
avgXP=int(input("Your average xp per match:"))

totalXPneeded=0

#calculation
for i in range(goalRank-playerRank):
    i=playerRank
    totalXPneeded=totalXPneeded+((i+1)*1000)
    i=+1
matchestgt=totalXPneeded/avgXP
timetgt=matchestgt*900
int(timetgt)

days=timetgt//86400
hours=(timetgt-(days*86400))//3600
minutes=(timetgt-(days*86400)-(hours*3600))//60

days=trunc(days)
hours=trunc(hours)
minutes=trunc(minutes)

#output
if minutes==0:
    print(f"{days} days and {hours} hours of continuous grinding")
elif hours==0:
    print(f"{days} days and {minutes} minutes of continuous grinding")
elif minutes==0 and hours==0:
    print(f"{days} days of continuous grinding")
else:
    print(f"{days} days, {hours} hours and {minutes} minutes of continuous grinding")