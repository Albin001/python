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
a="Hello"
b=upper_case(a)
print(b)
c=lower_case(a)
print(c)