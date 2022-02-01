# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 14:12:01 2022

@author: kARTIK
"""



class primeFinder :
    @staticmethod
    def findPrime(num):
        for i in range (2 ,num):
            if num%i==0:
                print (str(num)+" is not a prime number")
                break
        
        else:    
                print (str(num)+" is a prime number")
               
               

obj=primeFinder()
again = True

while again==True :
    a = int(input("Enter the number :- "))
    obj.findPrime(a)
    checkAgain=input("check another number yes(y) or no(n) :- ")
    if 'Y'==checkAgain.upper() or 'yes'==checkAgain.lower():
        again=True
    else :
        again=False
        print("ThankYou.........")