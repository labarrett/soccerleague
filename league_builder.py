
import csv

#teams to assign
yes_players=[]

shark=[]
dragons=[]
raptors=[]

#open and file
with open('soccer_players.csv') as csvfile:
    playerreader=csv.DictReader(csvfile)
    rows=list(playerreader)
    player=[]
    for row in rows:        
        if row['Soccer Experience']== "YES":
            yes_players.append(row['Name'])
#shark.append(player)
print(yes_players)
       
#pull out file information

#loop through info and add to appropariate lists

#take new lists and input them to a new file in order of TD instructions 
#with open("teams.txt", "a") as file:
 #   file.write(LIST NAMES)

 #row['Soccer Experience'],
              #row["Guardian Name(s)"],
              #row["Height (inches)"]
