#creating function
  function_name<- function(){
  print('this is a function')
  }
  
  function_with_args<- function(name){
    print(name)
  }
  #notice this function and it's call  
  function_with_args_default<- function(name='sharma'){
    print(name)
  }
  
  function_return<- function(name){
    return(name)
  }
  
  function_calling_function<- function(name){
    response<-last_name()
    return(paste(name,response))
  }
      last_name<-function(){return('Sharma')}
      
  nested_function<-function(name){
    inner_function<-function(){
      return('sharma')
    }
    return(paste(name,inner_function()))
    
  }
  
  add_function<-function(num1){
    calculate<-function(num2){
      return(num1+num2)
    }
    return(calculate)
  }
  
  
  
#calling function
  function_name()
  function_with_args('kartik')
  function_with_args_default()
  function_with_args_default('KS')
  print(function_return('Kartik Sharma'))
  print(function_calling_function('kartik'))
  print(nested_function('Kartik'))
  adder<-add_function(5) # here adder is also a function 
  print(adder(3)) #value assigned to adder is passed to inner function because add_function returned the function itself 
  