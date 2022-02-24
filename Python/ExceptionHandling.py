# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 21:07:02 2022

@author: kARTIK
"""

class oddNumberException(Exception):
          def _init_(self, a):
            self.value = str(a)
          def __str__(self):
            return("Odd number Entered :- "+str(a))
        
        
        



try:
    a=9
    b='c' # chnage b to an in , and you will see an user created exception ;)

    if a%b ==0:
        print("No Exception")
    else:    
       raise oddNumberException(a)
except oddNumberException as what_error:
        print("Exception Occured :- ",what_error)
  
except TypeError as what_error:
        print ("Exception Occured:- ",what_error)
finally:
    print("\n\n\tAll the best for future...")
        
    
    