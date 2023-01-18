# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 11:38:47 2023

@author: Tushar
"""
list1=[]
print("Enter 5 numbers")
for i in range(0,5):
    v=int(input())
    list1.append(v)
list2=[]
print("Enter 5 numbers")
for i in range(0,5):
    v=int(input())
    list2.append(v)
flag=0
for i in list1:
    if i in list2:
        flag=1
if(flag==1):
    print("The Lists Overlap")
else:
    print("The Lists do Not overlap")
list1=[]
c=int(input("Enter the number of elements that you want to insert in List 1:"))
for i  in range(0,c):
   ele = int(input("Enter the element :"))
   list1.append(ele)
a = int(input("enter the number that you want to find in List 1:"))
if a not in list1:
    print( "The list does not contain ", a )
else:
    print( "The list contains", a )
