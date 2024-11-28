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
    pname=''
    jnum=''
    team=''
    gs=''
    totmin1=''
    #process file
    boxid = open(fname,'r')
    #boxid = open('box-boxscore.html','r')
    text = boxid.readlines()
    boxid.close()
    n = len(text)
    teamfound = 0
    i = 0
    while i < n:
        #look for teams, score, date, and refs
        # look for game date
        found = text[i].find('<dt>Date')
        if found !=-1:
            i = i+1
            found = text[i].find('<dd>')
            gamedate = text[i][found+4:found+12]
            print(gamedate)
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
            print(refs)
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
                #print(team, jnum, pname, gs, min, fg, pt3, ft, orbdrb, reb, pf, a, to, blk, stl, pts)
        # look for the totals line
        found = text[i].find('<td>Totals')
        if found != -1:
            pname='Totals'
            i = i + 2
            if totmin1=='':
                found1 = text[i].find('MIN')
                found2 = text[i].find('</td')
                totmin1 = text[i][found1 + 5:found2]
                i = i + 1
                found1 = text[i].find('FG')
                found2 = text[i].find('</td')
                totfg1 = text[i][found1 + 4:found2]
                i = i + 1
                found1 = text[i].find('3PT')
                found2 = text[i].find('</td')
                totpt31 = text[i][found1 + 5:found2]
                i = i + 1
                found1 = text[i].find('FT')
                found2 = text[i].find('</td')
                totft1 = text[i][found1 + 4:found2]
                i = i + 1
                found1 = text[i].find('DRB')
                found2 = text[i].find('</td')
                totorbdrb1 = text[i][found1 + 5:found2]
                i = i + 1
                found1 = text[i].find('REB')
                found2 = text[i].find('</td')
                totreb1 = text[i][found1 + 5:found2]
                i = i + 1
                found1 = text[i].find('PF')
                found2 = text[i].find('</td')
                totpf1 = text[i][found1 + 4:found2]
                i = i + 1
                found1 = text[i].find('A')
                found2 = text[i].find('</td')
                tota1 = text[i][found1 + 3:found2]
                i = i + 1
                found1 = text[i].find('TO')
                found2 = text[i].find('</td')
                totto1 = text[i][found1 + 4:found2]
                i = i + 1
                found1 = text[i].find('BLK')
                found2 = text[i].find('</td')
                totblk1 = text[i][found1 + 5:found2]
                i = i + 1
                found1 = text[i].find('STL')
                found2 = text[i].find('</td')
                totstl1 = text[i][found1 + 5:found2]
                i = i + 1
                found1 = text[i].find('PTS')
                found2 = text[i].find('</td')
                totpts1 = text[i][found1 + 5:found2]
                print(team,jnum, pname,gs,totmin1,totfg1,totpt31,totft1,totorbdrb1,totreb1,totpf1,tota1,totto1,totblk1,totstl1,totpts1)
            else: 
                found1 = text[i].find('MIN')
                found2 = text[i].find('</td')
                totmin2 = text[i][found1 + 5:found2]
                i = i + 1
                found1 = text[i].find('FG')
                found2 = text[i].find('</td')
                totfg2 = text[i][found1 + 4:found2]
                i = i + 1
                found1 = text[i].find('3PT')
                found2 = text[i].find('</td')
                totpt32 = text[i][found1 + 5:found2]
                i = i + 1
                found1 = text[i].find('FT')
                found2 = text[i].find('</td')
                totft2 = text[i][found1 + 4:found2]
                i = i + 1
                found1 = text[i].find('DRB')
                found2 = text[i].find('</td')
                totorbdrb2 = text[i][found1 + 5:found2]
                i = i + 1
                found1 = text[i].find('REB')
                found2 = text[i].find('</td')
                totreb2 = text[i][found1 + 5:found2]
                i = i + 1
                found1 = text[i].find('PF')
                found2 = text[i].find('</td')
                totpf2 = text[i][found1 + 4:found2]
                i = i + 1
                found1 = text[i].find('A')
                found2 = text[i].find('</td')
                tota2 = text[i][found1 + 3:found2]
                i = i + 1
                found1 = text[i].find('TO')
                found2 = text[i].find('</td')
                totto2 = text[i][found1 + 4:found2]
                i = i + 1
                found1 = text[i].find('BLK')
                found2 = text[i].find('</td')
                totblk2 = text[i][found1 + 5:found2]
                i = i + 1
                found1 = text[i].find('STL')
                found2 = text[i].find('</td')
                totstl2 = text[i][found1 + 5:found2]
                i = i + 1
                found1 = text[i].find('PTS')
                found2 = text[i].find('</td')
                totpts2 = text[i][found1 + 5:found2]
                print(team,jnum, pname,gs,totmin2,totfg2,totpt32,totft2,totorbdrb2,totreb2,totpf2,tota2,totto2,totblk2,totstl2,totpts2)
            
        i = i+1
    print(team1, score1, team2, score2, gamedate, refs)
    
    x= int(score1)
    y= int(score2)
    
    winscore= max(x,y)
    if winscore==x:
        winner= team1
    elif winscore==y:
        winner=team2
    
        
    
    return[i, team1, score1, team2, score2, gamedate, refs, winner, totmin1, totmin2, totfg1, totfg2, totpt31, totpt32, totft1, totft2, totorbdrb1, totorbdrb2, totreb1, totreb2, totpf1, totpf2, tota1, tota2, totto1, totto2, totblk1, totblk2, totstl1, totstl2, totpts1, totpts2]

dir_list = os.listdir()
n = len(dir_list)
data_list=[]


for i in range(n):
    numchars = len(dir_list[i])
    ext = dir_list[i][numchars-4:]
    prefix = dir_list[i][0:7]
    #change 5 to num of characters in prefix ie.subox is 5
    #fgcu, njit
    #su, bu, ju, qu
    #ksu, lip, uca, una, unf, jax, eku, aup
    if prefix == 'fgcubox':
        #print(dir_list[i])
        data=processboxfile(dir_list[i])
        data_list.append(data) #print i counter for gameid
        

#print(data_list)        
with open('gamedata24fla.csv', mode='a', newline='') as csv_file:
        writer= csv.writer(csv_file)
        #writer.writerow(["GameID","AwayTeam", "AScore", "HomeTeam", "HScore", "Gamedate", "Refs", "WinTeam", "AMin", "HMin","AFg", "HFg", "A3pt", "H3pt", "AFt", "HFt", "AOD", "HOD", "AReb", "HReb", "HPf", "APf","AAst", "HAst", "ATo", "HTo", "ABlk", "HBlk", "AStl", "HStl", "APts", "HPts"])
        for data in data_list:
             writer.writerow(data)
