#Basics Of R

#type conversion

x<-10.5
y<-as.integer(x) #value after the decimal is neglected
z<-as.complex(x)
print(y)
print(z)

  #To check the type of variable
  print(class(x))
  print(class(y))
  print(class(z))
  

#STRINGS , can work with either " " or ' '  
test_string<-"qwerty,
asdf,
zxc"

print(test_string)
  #to remove spaces use cat()
    cat(test_string)
  
  #concatenation
    s1<-'kar'
    s2<-'tik'
    s3<-paste(s1,s2)
    print(s3)
  #number of chars in a string 
    nchar(s3) 
  #to find in a string
    grep('tiik',s3) # returns 1 for True & vice versa

#OPERATORS,
    #imp to note for modulus operator - returns remainder
      x<-5.8
      y<-2
      print(x%%y)
      print(x%/%y) # returns the quotient to the nearest roundUp towards back.`
#
#        Assignment Operator (<-) can also be -> & <<- ,i.e functionality 
#        remains same right value gets assigned to left value 
#
      #logical operators (!=,||,==,&&)
        #logical not 
          a=1
          b=1
          print(!(a==b)) #flips the result
  
#IF()..else

#>>> next , works similar to continue in java , 
#directly moves to next iteration , 
#skipping everything below   
#>>> break , breaks the loop

#For loop
      
          for (x in 1:5){ # start and end (1:5) are included
              print(x)
              }
