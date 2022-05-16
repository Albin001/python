# -*- coding: utf-8 -*-
"""
Created on Mon May 16 11:16:24 2022

@author: alber
"""

def upper_case(a1):
     b=a1.upper()
     c=0
     for i in a1:
         for j in b:
             if(i==j):
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
a="Hello123  "
b=upper_case(a)
print("No Of Upper Case :",b)
c=lower_case(a)
print("No of Lower Case :",c)
d=space_case(a)
print("No of Spaces :",d)
special_case(a)