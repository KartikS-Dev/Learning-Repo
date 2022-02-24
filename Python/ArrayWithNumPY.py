# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 13:09:26 2022

@author: kARTIK
"""
import numpy as np
"""

from numpy import *


myArray = array([1,2,3,4,5])


print(myArray.dtype)
print(myArray)



myArray = array([1,2,3,4,0.5])
#numpy implicitly converrt to float, all the values become float 
print(myArray.dtype)
print(myArray)




# start , End (included) , no. of parts
arr = linspace(0,16,10) #can give float as range is based on parts
print(arr)
arr = linspace(1,16,16)
print(arr)
arr = linspace(1,16,16) 
print(arr)
 

# start , end (not included) ,number added to the predecessor
arr=arange(1,11,2)
print(arr) #=>[1 3 5 7 9]


#array of all zeros lby default in float
arr=zeros(5)
print(arr)
#array of all zeros by in int
arr=zeros(5,int)
print(arr)

#llar to zeros
arr=ones(5)
print(arr)
arr=ones(5,int)
print(arr)




#operation on each elemet
arr=array([1,2,3,4,5,6])
print(arr+5)
    #adding 2 arrays
arr2=arr+5
print(arr+arr2)   
    #log, sin ,cos...
print(log(arr2))
print(sqrt(arr2))
    #copying array
arr3=arr2 # in memory there will be one array only
arr3=arr2.view() # two array in diff. memory ,this is shadow copying, 
                  #  change in arr2 will update in arr3
arr3=arr2.copy()#two different array , without any dependency on each other  
    


arr5= np.array([[3,4,5],[6,7,8],[9,10,11]])
print(arr5)
print(arr5[1:3 ])# because array has index from 0 and endpoint is not included
print(arr5[2:3 ,0]) # arr5([Rows,col])
print(arr5[2:3 ,0:3]) # arr5([Rows,col])
print(arr5[1:3 ,1]) # arr5([Rows,col])
print(arr5[1:3 ,1:2]) # arr5([Rows,col])
print(arr5[1:3 ,1:3]) # arr5([Rows,col])

"""


arr101= np.arange(0,10).reshape(2,5)

print(arr101)

print("\n\n")

splitarr101=np.hsplit(arr101,5)
print(splitarr101)
print("\n\n")

_splitarr101=np.vsplit(arr101,2)
print(_splitarr101)

