import csv

#teams to assign
yes_players=[]
no_players=[]

#open and file
with open('soccer_players.csv') as csvfile:
    playerreader=csv.DictReader(csvfile)
    rows=list(playerreader)

    for row in rows:        
        if row['Soccer Experience']== "YES":
            yes_players.append(tuple([row['Name'],row['Soccer Experience'],row["Guardian Name(s)"]]))
            
        else:
            no_players.append(tuple([row['Name'],row['Soccer Experience'],row["Guardian Name(s)"]]))
        
#add players to teams
size_needed= int(len(yes_players)/3)
no_size_needed = int(len(no_players)/3)

shark=yes_players[:size_needed] + no_players[:no_size_needed]
dragons=yes_players[size_needed: (size_needed * 2)] + no_players[no_size_needed: (no_size_needed * 2)]
raptors=yes_players[(size_needed * 2):] + no_players[(no_size_needed * 2):]

teams = {
        'sharks': shark,
        'raptors': dragons,
        'dragons': raptors
    }


def print_line(team):
    output = ""
    for player in team: 
        output += "Name: " + player[0] + ", " + "Soccer Experience: " + player[1] + ", " + "Parents: " + player[2] + "\n"
    return output


if __name__ == "__main__":
#write to team file
    with open("teams.txt", "w") as file:
        file.write("SHARKS *********\n")
        file.write(print_line(teams.get('sharks')))
        file.write("\nRAPTORS *********\n")
        file.write(print_line(teams.get('raptors')))
        file.write("\nDRAGONS *********\n")
        file.write(print_line(teams.get('dragons')))
        file.close()  
