# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 11:24:19 2023

@author: Tushar
"""
inputs = float(input("Enter the input :"))
weights = float(input("Enter the weight :"))
bias = float(input("Enter bias :"))
yin = bias + (inputs * weights)
if yin < 0:
  out = 0
elif yin > 1:
  out= 1
else:
    out = yin
print("Output is :",out)
