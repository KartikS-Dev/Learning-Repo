# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 20:37:21 2022

@author: kARTIK
"""

import re as reg


test_string="qwerty 31 kartik 7 shar19 ma97 "



def reg_findAll_function():
    
    # finding all the occurence of values given in the square bracs.
    print(reg.findall("[317]", test_string))
    
    # finding specific data
    print(reg.findall("31", test_string))
    
    #\d is decimal digit
    print(reg.findall("\d", test_string))

    #\D - not a digit 
    print(reg.findall("\D", test_string))



reg_findAll_function()