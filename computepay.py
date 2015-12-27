# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 14:14:40 2015

@author: nerdylinius
"""

def computepay(h, r):
    h, r = float(h), float(r)
    return h*r if h<=40 else 40*r+(h-40)*r*1.5
    
def computepay1(h, r):
    h, r = float(h), float(r)
    if h <= 40:
        return h*r
    else:
        return 40*r+(h-40)*r*1.5
    
h = raw_input("Enter hours:")
r = raw_input("Enter rate:")
print computepay(h, r)
