# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 20:10:00 2022

@author: KartikS
"""

print("\n Result Calculator")

a="Enter practical assessments marks "
i=1
inputMarks=float(0)
sumOfMarks=float(0)

while i<=5:
    try:
       inputMarks= float(input(a+" for P "+ str(i)+ " :- "))*0.1
    except ValueError:
        print("!!!! please enter only numeric values !!!! \n")
        i=i-1
    sumOfMarks += inputMarks
    i=i+1

print ("-->> Total Marks in practical assessments (%age) :"+str(sumOfMarks))


inputMarks = float(input("Enter project marks :- "))*0.5
print ("-->> Total Marks in project (%age) :"+str(inputMarks))
sumOfMarks+=inputMarks


if sumOfMarks<40 : 
    print("\n !!! Failed with "+str(sumOfMarks)+ " (%age) marks")
else:
    print("\n Passed with "+str(sumOfMarks)+ " (%age) marks")    

    