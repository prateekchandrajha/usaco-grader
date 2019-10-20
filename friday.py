# -*- coding: utf-8 -*-
"""
ID: prateek53
LANG: PYTHON3
TASK: friday
"""

fin = open ('friday.in', 'r')
fout = open ('friday.out', 'w')

N = int(fin.read())

start_y = 1900

days_of_week =  {0:0,1:0,2:0,3:0,4:0,5:0,6:0} # Saturday to Friday Week, so days_of_week[0] represents Saturday and [6] represents Friday

days_30_mon = [4,6,9,11]
days_31_mon = [1,3,5,7,8,10,12]
mon_28_29 = [2]

counter = 0 # start_counter that starts on Monday i.e. pointing at the first key of days_of_week 1900 1st January
days_elapsed = 0
#days_of_week[counter]+=1

for curr_year in range(N):
    if((1900+curr_year)%4==0 and (1900+curr_year)%100!=0):
        for j in range(12):
            if j+1 in days_30_mon:
                days_elapsed+=12
                counter=(days_elapsed % 7)
                days_of_week[counter]+=1
                days_elapsed+=18
                counter=0
            if j+1 in days_31_mon:
                days_elapsed+=12
                counter=(days_elapsed % 7)
                days_of_week[counter]+=1
                days_elapsed+=19
                counter=0
            if j+1 in mon_28_29:
                days_elapsed+=12
                counter=(days_elapsed % 7)
                days_of_week[counter]+=1
                days_elapsed+=17
                counter=0
        continue
    
    if((1900+curr_year)%400==0):
        for j in range(12):
            if j+1 in days_30_mon:
                days_elapsed+=12
                counter=(days_elapsed % 7)
                days_of_week[counter]+=1
                days_elapsed+=18
                counter=0
            if j+1 in days_31_mon:
                days_elapsed+=12
                counter=(days_elapsed % 7)
                days_of_week[counter]+=1
                days_elapsed+=19
                counter=0
            if j+1 in mon_28_29:
                days_elapsed+=12
                counter=(days_elapsed % 7)
                days_of_week[counter]+=1
                days_elapsed+=17
                counter=0
        continue
    
    for j in range(12):
            if j+1 in days_30_mon:
                days_elapsed+=12
                counter=(days_elapsed % 7)
                days_of_week[counter]+=1
                days_elapsed+=18
                counter=0
            if j+1 in days_31_mon:
                days_elapsed+=12
                counter=(days_elapsed % 7)
                days_of_week[counter]+=1
                days_elapsed+=19
                counter=0
            if j+1 in mon_28_29:
                days_elapsed+=12
                counter=(days_elapsed % 7)
                days_of_week[counter]+=1
                days_elapsed+=16
                counter=0
                
       
        
numbers = [5,6,0,1,2,3,4]
for i in numbers:
    fout.write(str(days_of_week[i]))
    if i==4:
        fout.write("\n")
    else:
        fout.write(" ")

        
fout.close()
