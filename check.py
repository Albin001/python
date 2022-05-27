# -*- coding: utf-8 -*-
"""
Created on Mon May 16 11:16:24 2022

@author: alber
"""
import pandas as pd
import matplotlib.pyplot as pt
l2=[]
l3=[]
l4=[]
s=0
def upper_case(a1):
     b=a1.upper()
     c=0
     for i in a1:
         if(i.isupper()==True):
             c=c+1
         else:
             continue;
     return c
def lower_case(a1):
     c1=0
     for i in a1:
         if(i.islower()==True):
             c1=c1+1
         else:
             continue;
     return c1
def space_case(a1):
    c2=0
    for i in a1:
        if(i.isspace()==True):
            c2=c2+1
        else:
             continue;
    return c2
def special_case(a1):
    c3=0
    c4=0
    c5=0
    for i in a1:
        if(i.isalnum()==True):
            if(i.isdigit()==True):
                c3=c3+1
            else:
                c4=c4+1
        else:
            c5=c5+1
    print("No of digits :",c3)
    print("No of Characters :",c4)
    print("No of  Special Characters :",c5)
f1=open("C:/Users/alber/Desktop/p1.txt","r")
f2=f1.read()
l1=f2.split()
for i in l1:
    print("Checking the Character is {}".format(i))
    a=upper_case(i)
    l2.append(a)
    print("The No of Upper Case :{}".format(a))
    c=lower_case(i)
    l3.append(c)
    print("No of Lower Case :",c)
    d=space_case(i)
    print("No of Spaces :",d)
    special_case(i)
f1.close()
a1={"uppercase":l2,"Lowercase":l3}
d1=pd.DataFrame(a1)
print(d1)
for i in l1:
    s=s+1
    l4.append(s)
pt.subplot(1,2,1)
pt.plot(l4,l2,marker='o',color="red")
pt.xlabel("No Of Characters For Test")
pt.ylabel("Upper Case")
pt.title("Data Analysis Of Characters")
pt.grid()
pt.subplot(1,2,2)
pt.plot(l4,l3,marker='o',color="blue")
pt.xlabel("No Of Characters For Test")
pt.ylabel("Lower  Case")
pt.title("Data Analysis Of Characters")
pt.grid()
pt.show()
    

