import csv

#teams to assign
yes_players=[]
no_players=[]


#open and file
with open('soccer_players.csv') as csvfile:
    playerreader=csv.DictReader(csvfile)
    rows=list(playerreader)
    player=[]
    for row in rows:        
        if row['Soccer Experience']== "YES":
            yes_players.append(tuple([row['Name'],row['Soccer Experience'],row["Guardian Name(s)"]]))
            
        else:
            no_players.append(tuple([row['Name'],row['Soccer Experience'],row["Guardian Name(s)"]]))
        
#shark.append(player)


size_needed= int(len(yes_players)/3)
no_size_needed = int(len(no_players)/3)

print(yes_players)
shark=yes_players[:size_needed] + no_players[:no_size_needed]
dragons=yes_players[size_needed: (size_needed * 2)] + no_players[no_size_needed: (no_size_needed * 2)]
raptors=yes_players[(size_needed * 2):] + no_players[(no_size_needed * 2):]

def commas():
 print("*" * 25)

commas()
print("SHARKS:", shark)
commas()
print("DRAGONS:", dragons)
commas()
print("RAPTORS:", raptors)
commas()


teams = {
    'sharks': shark,
    'raptors': dragons,
    'dragons': raptors
}       


#right to file
with open("teams.txt", "a") as file:
    file.write("SHARKS *********\n")
    file.write(str(teams.get('sharks')))
    file.write("\nRAPTORS *********\n")
    file.write(str(teams.get('raptors')))
    file.write("\nDRAGONS *********\n")
    file.write(str(teams.get('dragons')))
   
    file.close()

 #row['Soccer Experience'],
              #row["Guardian Name(s)"],
              #row["Height (inches)"]

 #    file.write(str(dragons))
#    file.write(str(raptors))
