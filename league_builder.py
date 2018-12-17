
import csv


#open and file
with open('soccer_players.csv') as csvfile:
    playerreader=csv.DictReader(csvfile)
    rows=list(playerreader)
    for row in rows:
        print(row['Name'],row['Soccer Experience'])
       
       
        
       
#pull out file information

#loop through info and add to appropariate lists

#take new lists and input them to a new file in order of TD instructions 
#with open("teams.txt", "a") as file:
 #   file.write(LIST NAMES)


