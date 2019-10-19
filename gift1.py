# -*- coding: utf-8 -*-
"""
ID: prateek53
LANG: PYTHON3
TASK: gift1
"""

fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')
names={}
l=[]

for line in fin:
    l.append(line)
    
n_people = int(l[0])
for i in range(n_people):
    names[l[i+1]]=0
    
count=0
money_given=0
name_who_gives=""
friends_who_get=0

for i in l[(n_people+1):len(l)]:
    #if(i==l[len(l)-1]):
     #   names[i]=names[i]+(money_given//friends_who_get)
      #  continue
    if(count==0):
        name_who_gives=i
    if(count==1):
        money_given=int(i.split(" ")[0])
        friends_who_get=int(i.split(" ")[1])
        names[name_who_gives]-=money_given
    if(count!=0 and count!=1):
        names[i]=names[i]+(money_given//friends_who_get)
    if(count==friends_who_get+1):
        count=0
        if(friends_who_get==0):
            continue            
        names[name_who_gives]+=(money_given%friends_who_get)
        continue
    count+=1
    
for i in names:
    fout.write(i[0:-1])
    fout.write(" ")
    fout.write(str(names[i]))
    fout.write("\n")
        
fout.close()
