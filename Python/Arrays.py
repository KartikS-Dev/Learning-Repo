# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 12:10:53 2022

@author: kARTIK
"""

from array import *


userArray = array('i',[])



class ArrayCreation:
    
    @staticmethod
    def getArraySize():
        arraySizeInput=int(input("how many numbers you want to enter :- "))
        ArrayCreation.createArray(arraySizeInput)

    @classmethod
    def createArray(self,arraySize):
        for i in range(arraySize):
            userInput=int(input("Enter number "+str(i)+" :- "))
            userArray.append(userInput)
            
            
    @staticmethod
    def searchArray():
            userInput=int(input("Enter number to search  :- "))
            for i in range(0,len(userArray)):
                if userInput == userArray[i]:
                    return str(i)
            else :
                return '!!!! not found'
                        



obj = ArrayCreation()
obj.getArraySize()
print(userArray)



print("found the number at index :- " + obj.searchArray())

