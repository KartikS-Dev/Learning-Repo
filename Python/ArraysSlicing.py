# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 19:14:41 2022

@author: kARTIK
"""

from array import *
import numpy as np


#Array Slicing :- array[startIndex:stopIndex(not included)]
# array[startIndex:] start from the index ,till end index
# array[:stopIndex(not included)] remove everthing starting from this index
#array[startIndex:stopIndex(not included):step]#slicing with skipping the values also
#arr[1, 1:4] 
myArray = np.arange(15).reshape(3,5) 
print(myArray) 

print("\n")
print(myArray[1::]) 

print("\n")
print(myArray[:2:]) 

print("\n")
print(myArray[::3]) 


print("\n")

print(myArray[:1:]) 

print(myArray[:,1:3]) 



arr=np.arange(60) # 0 to 59


print(arr)


print(arr[2])

print(arr[0:59:2])


arr2= arr.reshape(6,10)

print(arr2)

arr3= np.arange(0.0,5.0,0.2)
print(arr3)

arr4=arr.reshape(3,2,10) # array of 3 stacks with each stach having 2 rows and 10 cols
print(arr4)

print(arr4[1,1,3])# stack on index 1, row index 1 and column index 3