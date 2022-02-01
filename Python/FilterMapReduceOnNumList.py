# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 21:29:42 2022

@author: offic
"""
from functools import reduce


numList  = [1,2,3,4,5,6,7,8,9,10]

def isEven(number):
    if number%2==0:
        return True

def doubler(number):
      return number*2

def sumCalc(number1,number2):
      return number1+number2;


#Filter sends the elements to the function one by one
evens = list(filter(isEven, numList))

#map is used when we need to perform operation on all values apart from filtering
doubledEvens = list(map(doubler, evens))

#we use reduce to collect a values and generate one result
summingEvens=reduce(sumCalc, evens)

print("Evens :- "+str(evens))
print("Even Values Doubled :- "+str(doubledEvens))
print("Sum of Even Values  :- "+str(summingEvens))


print("\n operations done on Odds are using LAMBDA \n")


#Using lambda!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

odds = list(filter(lambda numbers : numbers%2!=0, numList))

doubledOdds = list(map(lambda number: number*2, odds))

summingOdds=reduce(lambda number1,number2: number1+number2, odds)

print("Odds :- "+str(odds))
print("Odd Values Doubled :- "+str(doubledOdds))
print("Sum of odd Values  :- "+str(summingOdds))
