# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 22:28:23 2022

@author: offic
"""

#In python functions are treated s objects ,we can call a function inside a function 
# using decorators.

#This can be used there is need to add new functionality to an existing function without 
#updating the existing functions



def div(a,b):
    print (a/b)
    

def smart_div(fxn):
    #function inside function calling another function
    def divide(a,b):
        if a<b:
            a,b=b,a
        return fxn(a,b)
    return divide
    
    
divisionResult = smart_div(div)    


divisionResult(6,4)