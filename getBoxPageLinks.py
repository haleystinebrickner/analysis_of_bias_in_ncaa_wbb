
boxid = open('famuschedule-2018-19.html', 'r')
text = boxid.readlines()
boxid.close()
n = len(text)
teamfound = 0
i = 0
tempid = open('temp.txt', 'w')
while i < n:
        # look for teams, score, date, and refs
        # look for game date
        found = text[i].find('/boxscore/')
        if found != -1:
                found1 = text[i].find('href')
                found2 = text[i].find('aria')
                pre = '"'+"https://famuathletics.com"
                #pre = ''
                wsite = pre+text[i][found1+6:found2-1]+','
                tempid.write(wsite+'\n')
                print(wsite)
        i = i + 1

tempid.close()
                                                                                            
