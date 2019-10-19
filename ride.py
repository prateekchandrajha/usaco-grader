# -*- coding: utf-8 -*-
"""
ID: prateek53
LANG: PYTHON3
TASK: gift1
"""
fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')
l=[]


#x=input("enter number")
#y=input("enter another number")

def asciiprod(st):
    prod1=1
    for i in st:
        prod=1
        prod1=prod1*(ord(i)-64)
        
    return(prod1)

for line in fin:
    xin = asciiprod(line)%47
    l.append(xin)
    
if l[0]==l[1]: 
    fout.write ("GO\n")
    #print("GO")
else:
    fout.write ("STAY\n")

#if ((asciiprod(x))%47 == (asciiprod(y))%47):
   # fout.write ("GO")
    #print("GO")
#else:
 #   fout.write ("STAY")
    #print("STAY")
fout.close()



