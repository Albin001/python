# -*- coding: utf-8 -*-
"""
Created on Fri May 27 09:47:34 2022

@author: alber
"""

import matplotlib.pyplot as pt
l2=[]
l4=[1,2,3,4]
l5=[1,2,3,4]
c=0
l3=["PIC","AVR","ARDUINO","8051","ARM8","welcome"]
f1=open("C:/Users/alber/Desktop/p1.txt","r")
f2=f1.read()
f3=f2.split()
for i in f3:
    for i1 in l3:
        if(i==i1):
            c=c+1  
        else:
            continue
            print("Wrong Answer")  
f1
f1.close()
print(c)
l4.append(c)
l5.append(c)
pt.plot(l4,l5,linewidth="7")
pt.xlabel("Maximum Mark")
pt.ylabel("Total MArks")
pt.show()

