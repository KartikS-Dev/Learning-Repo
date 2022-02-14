# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 21:10:19 2022

@author: kARTIK
"""

import urllib.request
import urllib.error

from socket import gaierror


def wrong_url(): 

    try:
        response = urllib.request.urlopen('http://pythonnn.org/')
        try:
            html = response.read()
            html = str(html)
            print("Success \n")
        except gaierror: #What is Gaierror?It means that your given host name ' ' is invalid (gai stands for getaddrinfo() ).
            print("exception - gaierror")
    
    except urllib.error.URLError:
        print("exceptio - URLError")
        
        
def correct_url(): 

    try:
        response = urllib.request.urlopen('http://python.org/')
        try:
            html = response.read()
            html = str(html)
            print("Success \n")
        except gaierror: #What is Gaierror?It means that your given host name ' ' is invalid (gai stands for getaddrinfo() ).
            print("exception - gaierror")
    
    except urllib.error.URLError:
        print("exception - URLError")
        



#Calling Correct URL
print("Calling Correct URL")
correct_url() 


#Calling wrong URL
print("Calling wrong URL")
wrong_url()   