
import os
import csv

def processboxfile(fname):
    #initialize variables
    team1=''
    score1=''
    team2=''
    score2=''
    refs=''
    gamedate=''
    #process file
    boxid = open(fname,'r')
    #boxid = open('box-boxscore.html','r')
    text = boxid.readlines()
    boxid.close()
    n = len(text)
    teamfound = 0
    i = 0
    players=[]
    while i < n:
        #look for teams, score, date, and refs
        # look for game date
        found = text[i].find('<dt>Date')
        if found !=-1:
            i = i+1
            found = text[i].find('<dd>')
            gamedate = text[i][found+4:found+12]
            #print(gamedate)
        # look for team and score
        found = text[i].find("section class="+'"panel"')
        if found != -1:
            l = len(text[i])
            team = text[i][47:l-6]
            score = text[i][l-5:l-3]
            if teamfound == 0:
                teamfound = -1
                team1 = team
                score1 = score
                #print(team1, score1)
            else:
                team2 = team
                score2 = score
                #print(team2, score2)
        # look for refs
        found = text[i].find('Referees')
        if found !=-1:
            i = i+1
            found1 = text[i].find('<dd>')
            found2 = text[i].find('</dd>')
            refs = text[i][found1+4:found2]
            #print(refs)
        # get player stats
        found = text[i].find('mobile-jersey-number')
        if found != -1:
            offset = found+len('mobile-jersey-number')+2
            l = 2
            # jersey number
            jnum=text[i][offset:offset+l]
            if jnum != 'TM':
                # player name
                # ignore link if there
                found1 = text[i].find('href')
                if found1 ==-1:
                    found1 = text[i].find('/span')
                    found2 = text[i].find('</td')
                    pname =text[i][found1+7:found2]
                else:
                    found1 = text[i].find("'boxscore_player_link'>")
                    found2 = text[i].find('</a')
                    pname = text[i][found1 + 23:found2]
                i=i+1
                found1 = text[i].find('down')
                found2 = text[i].find('</td')
                gs = text[i][found1+6:found2]
                i = i+1
                found1 = text[i].find('MIN')
                found2 = text[i].find('</td')
                min = text[i][found1+5:found2]
                i = i+1
                found1 = text[i].find('FG')
                found2 = text[i].find('</td')
                fg = text[i][found1+4:found2]
                i = i+1
                found1 = text[i].find('3PT')
                found2 = text[i].find('</td')
                pt3 = text[i][found1+5:found2]
                i = i+1
                found1 = text[i].find('FT')
                found2 = text[i].find('</td')
                ft = text[i][found1+4:found2]
                i = i+1
                found1 = text[i].find('DRB')
                found2 = text[i].find('</td')
                orbdrb = text[i][found1+5:found2]
                i = i+1
                found1 = text[i].find('REB')
                found2 = text[i].find('</td')
                reb = text[i][found1+5:found2]
                i = i+1
                found1 = text[i].find('PF')
                found2 = text[i].find('</td')
                pf = text[i][found1+4:found2]
                i = i+1
                found1 = text[i].find('A')
                found2 = text[i].find('</td')
                a = text[i][found1+3:found2]
                i = i+1
                found1 = text[i].find('TO')
                found2 = text[i].find('</td')
                to = text[i][found1+4:found2]
                i = i+1
                found1 = text[i].find('BLK')
                found2 = text[i].find('</td')
                blk = text[i][found1+5:found2]
                i = i+1
                found1 = text[i].find('STL')
                found2 = text[i].find('</td')
                stl = text[i][found1+5:found2]
                i = i+1
                found1 = text[i].find('PTS')
                found2 = text[i].find('</td')
                pts = text[i][found1+5:found2]
                #print(team,jnum, pname,gs,min,fg,pt3,ft,orbdrb,reb,pf,a,to,blk,stl,pts)
                player_info=[team,jnum, pname,gs,min,fg,pt3,ft,orbdrb,reb,pf,a,to,blk,stl,pts]
                players.append(player_info)
                        
        i = i+1
    #print(team1, score1, team2, score2, gamedate, refs)
    #print[players]
    return[i, players]

dir_list = os.listdir()
n = len(dir_list)
data_list=[]
all_playerstat=[]

for i in range(n):
    numchars = len(dir_list[i])
    ext = dir_list[i][numchars - 4:]
    prefix = dir_list[i][0:7]
    if prefix == 'fgcubox':
        i, data_list = processboxfile(dir_list[i])
        all_playerstat.append((i, data_list))  # Store 'i' along with player data

with open('player_stats.csv', 'a', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write the header row
    header = ["GameID", "Team", "Jersey Number", "Player Name", "GS", "MIN", "FG", "3PT", "FT", "ORB+DRB", "REB", "PF", "A", "TO", "BLK", "STL", "PTS"]
    csv_writer.writerow(header)

    # Write the player statistics along with their corresponding 'i' value
    for i, player_data in all_playerstat:
        for player_info in player_data:
            player_row = [str(i)] + player_info  # Convert 'i' to a string and concatenate it
            csv_writer.writerow(player_row)
"""
for i in range(n):
    numchars = len(dir_list[i])
    ext = dir_list[i][numchars-4:]
    prefix = dir_list[i][0:7]
    if prefix == 'fgcubox':
        #print(dir_list[i])
        i, data_list=processboxfile(dir_list[i])
        #print(data_list)
        #print("0 index",data_list[0]) #this works but multiple data_list[0] exist need another list
        all_playerstat.append((i,data_list))

with open('player_stats.csv', 'a', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write the header row
    header = ["GameID", "Team", "Jersey Number", "Player Name", "GS", "MIN", "FG", "3PT", "FT", "ORB+DRB", "REB", "PF", "A", "TO", "BLK", "STL", "PTS"]
    csv_writer.writerow(header)

    # Write the player statistics along with their corresponding 'i' value
    for i, player_data in all_playerstat:
        for player_info in player_data:
            player_row = [i] + player_info[1:]  # Concatenate 'i' with the player_info list, excluding the 'i' value
            csv_writer.writerow(player_row)
"""