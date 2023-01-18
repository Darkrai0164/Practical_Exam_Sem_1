# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 11:40:26 2023

@author: Tushar
"""
details =[]
name=input("Enter your name : ")
details.append(name)
age=float(input("Enter your exact age : "))
details.append(age)
roll_no=int(input("Enter your roll no : "))
details.append(roll_no)
 
for i in details:
    print(i)
    print("Int = ",type(i) is int)
    print("Float = ",type(i) is float)
    print("String = ",type(i) is str)
    print()
details =[]
name=input("Enter your name : ")
details.append(name)
age=float(input("Enter your exact age : "))
details.append(age)
roll_no=int(input("Enter your roll no : "))
details.append(roll_no)
print() 
for i in details:
    print(i)
    print("Not Int = ",type(i) is not int)
    print("Not Float = ",type(i) is not float)
    print("Not String = ",type(i) is not str)
    print()
