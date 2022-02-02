# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 14:00:17 2022

@author: kARTIK
"""

from numpy import *

arr = array([[1,2,3],
             [4,5,6]]) #ndarray ...n dimensional array

print(arr)
print(arr.ndim)# to get the total dimension 
print(arr.size)
print(arr.flatten())#muli to single dimension


arr = array([[1,2,3],
             [4,5,6]])
print(arr.reshape(3,2))#  multidimensionnal array using reshap based on specified Rows & cols


#MATRIX
arr = array([[1,2,3],
             [4,5,6]])

m = matrix(arr)
print(m)

        #another way to create matrix
m = matrix('1,2,3;4,5,6;7,8,9') # row seperated by ;
print(m)

    #operations on matrix
print(diagonal(m))# get diagonal elements of matrix
print(m.min())# min values in matrix

m2 = matrix('7,8,9;4,5,6;1,2,3')
print(m*m2)
print(m/m2)