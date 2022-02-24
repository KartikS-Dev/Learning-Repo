# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 16:41:16 2022

@author: kARTIK
"""

"""
1 Create a function to import this XML file. 
Your function should include appropriate exception handling clauses and should return the XML data.
"""

import xml.etree.ElementTree as ET

xmlFilePAth = "C://Users//offic//OneDrive//Documents//NationalCollegeOfIreland//College Notes//SEM1_Subjects//DataBaseAndAnalyticsProgramming//CA1_SEM1//theoDataset.xml"

def getXMLFile(filePath):
    try:
        xmlData= open(filePath,'r')
        xmlTree=ET.fromstring(xmlData.read())
        return xmlTree
    except FileNotFoundError :
        print(">>>> File Not Found at the path provided")
    finally:
        xmlData.close()


importedXMLTree=getXMLFile(xmlFilePAth)



"""
b) Use the print function to display the ‘id’, ‘weight’ and ‘conc’ of the second, fourth, 
    sixth, eight and tenth records in the XML dataset. 
    (Hint: you may use the range() function).
"""

#printing Complete xml 
import xml.dom.minidom
dom = xml.dom.minidom.parse(xmlFilePAth) # or xml.dom.minidom.parseString(xml_string)
pretty_xml_as_string = dom.toprettyxml()
#print (pretty_xml_as_string)


for i in range (1,10,2):
    try:
        id = importedXMLTree[i].find('id').text
        weight=importedXMLTree[i].find('weight').text
        conc=importedXMLTree[i].find('conc').text
        print("id :{}\t weight :{}\t conc :{}\t".format(id, weight,conc))
    except AttributeError : 
        print (">>>> Attribute does not exist ")
        break
    

"""
c)Extract all the XML data and write it to a CSV file. 
    Your file should also contain the column names.
"""    
#create a CSV file 
csvFilePath = "C://Users//offic//OneDrive//Documents//NationalCollegeOfIreland//College Notes//SEM1_Subjects//DataBaseAndAnalyticsProgramming//CA1_SEM1//theoDataset.csv"

def fileCreator(filePath):
    try:
        csvFile=open(filePath,'r')
    except FileNotFoundError:
        try:
            csvFile=open(filePath,'w')
            print('\nfile Createed successfully')
        except PermissionError:
            print("it seems either you don't have permission or file is already open")
    except PermissionError:
        print("it seems either you don't have permission , or file is already open")
    else:
        print('\nFile Already Exists')
    finally:
        csvFile.close()


fileCreator(csvFilePath)

#Writing the XML Data to CSV file
import csv

def writingCSVFile(filePath):
   try: 
        xmlFile=open(xmlFilePAth,'r')
        csvFile=open(filePath,'w')
        csvWriter=csv.writer(csvFile)
        #adding col names in CSV file , loop should only run once 
        temp=0
        for subject in importedXMLTree.findall('subject'):
            row=[]
            head=[]
            if temp ==0:
                for j in range (0, len(list(subject))):
                    print(subject[j].tag)
                    head.append(subject[j].tag)
                    temp = 1
                csvWriter.writerow(head)
            
        
            for i in range(0,len(list(subject))):
                #print(subject[i].text)
                row.append(subject[i].text)
            csvWriter.writerow(row)
        csvFile.close()
   except PermissionError:
        print("it seems either you don't have permission , or file is already open")
    
   finally:   
       xmlFile.close()
writingCSVFile(csvFilePath)          


"""
d)Create a NumPy array filled with 3000 numbers starting with 1,000. 
    Ensure that your array has 300 rows and 10 columns.
""" 
import numpy as np

myArray = np.arange(1000,4000).reshape(300,10)
print(myArray)  
print("\n\n")

"""
e)Using slicing, split this array into 5 separate arrays. 
    The number of rows in each array should be equal, 
    and there should still be 5 columns.
"""
my_array_one = myArray[0:60,:]
my_array_two = myArray[60:120,:]
my_array_three = myArray[120:180,:]
my_array_four = myArray[180:240,:]
my_array_five = myArray[240:300,:]

print(my_array_one)

print("\n\n")
print(my_array_five)
print("\n\n")

"""
f)Reshape these 3 of these arrays into any dimensions of your choice. 
    They should all have different dimensions.
"""
reShapedOne = my_array_one.ravel() #Return a contiguous flattened array
reShapedfive= my_array_five.reshape(200,3)
reShapedThree= my_array_three.reshape(100,3,2)
print(reShapedThree)
print("\n\n")

"""
g) Split 2 of these reshaped arrays column-wise. means :- Hsplit
"""
splitThree=np.hsplit(reShapedThree,3)
print(splitThree)


"""
h) Create a new array whose shape is **broadcast compatible** with your 
    original ndarray. It should contain values starting at 500.
    Multiply this new array by your original array.
    
Rules os Braod Cast Compatibility 
 > Either Row or column should match with other array respectively
 > if a=(2,3) and b = (,3) , since b is shorter array , we prepend 1 in it
     now b=(1,3) , hence compatible to a as cols match .
    
"""

print("\n\nBroadcasting\n\n")
newArray=np.arange(500,800).reshape(300,1)
print(newArray)
print("\n\n Multiplying 2 arrays \n\n")
print(myArray*newArray)


"""
I) Given the following string:

All I want is a proper cup of coffee
Made in a proper copper coffee pot
I may be off my dot
But I want a cup of coffee
From a proper coffee pot
Tin coffee pots and iron coffee pots
They’re no use to me
If I can’t have a proper cup of coffee
In a proper copper coffee pot
I’ll have a cup of tea

Write a single function that uses regular expressions to highlight the words “tea”,“dot” or “pot” if they appear at the end of a line.

Your answer should look like this:

All I want is a proper cup of coffee
Made in a proper copper coffee {pot}
I may be off my {dot}
But I want a cup of coffee
From a proper coffee {pot}
Tin coffee pots and iron coffee pots
They’re no use to me
If I can’t have a proper cup of coffee
In a proper copper coffee {pot}
I’ll have a cup of {tea}

"""
import re

testString = "All I want is a proper cup of coffee\nMade in a proper copper coffee pot\nI may be off my dot\nBut I want a cup of coffee\nFrom a proper coffee pot\nTin coffee pots and iron coffee pots\nThey’re no use to me\nIf I can’t have a proper cup of coffee\nIn a proper copper coffee pot\nI’ll have a cup of tea"
data=["pot",'tea','dot']
testarr=[]

def stringSplitter(str):
    testarr = testString.split("\n")
    return (testarr)

def stringCreator(testarr):
    finalString=""
    for i in range (0 , len(testarr)):
        finalString = finalString+testarr[i]+"\n"
    return finalString    

def stringCreatorV2(testarr):
    finalString=""
    for i in range (0 , len(testarr)):
        finalString = finalString+testarr[i]+" "
    return finalString    

def highlighter(str):
    testarr = stringSplitter(str)
    regex="\\b{}\\b$"
    
    for i in data:
        for x in testarr:
            if re.search(regex.format(i), x)!=None:
                tempStartIndex = x.index(i)
                tempEndIndex = tempStartIndex+2
                tempString=x[tempStartIndex:tempEndIndex+1]
                #print(tempString)
                tempString = "{"+tempString+"}"
                updatedX = x[0:tempStartIndex] + tempString
                #print(updatedX)
                indexInTestArr = testarr.index(x)
                testarr[indexInTestArr] = updatedX
                
    
    return stringCreator(testarr)

    
    
print(highlighter(testString))

"""
J)Using regular expressions, write code to highlight all words that begin with the characters po or co.

Your answer should look like this:

All I want is a proper cup of {coffee}
Made in a proper {copper} {coffee} {pot}
I may be off my dot
But I want a cup of {coffee}
From a proper {coffee} {pot}
Tin {coffee} {pots} and iron {coffee} {pots}
They’re no use to me
If I can’t have a proper cup of {coffee}
In a proper {copper} {coffee} {pot}
I’ll have a cup of tea
"""

dataV2=['po','co']
def highlighterV2(str):
    testarr = stringSplitter(str)
    regex="{}"
  
    for i in dataV2:
        for x in testarr:
            if re.search(regex.format(i), x)!=None:
                innerArr = testarr[testarr.index(x)].split(" ")
                for y in innerArr:
                    if re.search(regex.format(i), y)!=None:
                        tempInnerString = "{"+y+"}"
                        innerArr[innerArr.index(y)]=tempInnerString
                testarr[testarr.index(x)]= stringCreatorV2(innerArr)
               
    return stringCreator(testarr)

    
    
print(highlighterV2(testString))

"""
The End...
"""