#creating a data frame

id<- c(1:6)

name<-c("Kartik sharma","Rahul Dubey","Ranjit Singh","Ram Charan","Amit Sharma","Raghav ali")

job_title<-c("developer","developer","support","security","managment","" )

employee<-data.frame(id,name,job_title)


print(employee)


#dividing name col in to 2 new cols
emp_seprated_name<-separate(employee,name, into = c('first_name','last_name'),sep=' ')
print(emp_seprated_name)

#uniting first name and last name col into one 
emp_united_names<-unite(emp_seprated_name,'name',first_name,last_name)
print(emp_united_names)

#uniting first name and last name col into one using sep
emp_united_names_with_sep<-unite(emp_seprated_name,'name',first_name,last_name,sep = " ")
print(emp_united_names_with_sep)


