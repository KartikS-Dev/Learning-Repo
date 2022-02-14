#TidyVerse
data("ToothGrowth")
view(ToothGrowth)



#We need to filter and Sort Data for Analysis
#Without pipes, we could do this 
  #either by nesting commands or by creating a sequence of data frames. 

install.packages("dplyr")

#Filtering Using filter()
filtered_tg<-filter(ToothGrowth,dose==0.5)
View(filtered_tg)

#Sorting using arange()
arrange(filtered_tg,len)


#Sorting And Filtering Using Nested Function
arrange(filter(ToothGrowth,dose==0.5),len)


#Using Pipes

filtered_toothGrowth<-ToothGrowth %>%
  filter(dose==0.5)%>%
  arrange(len)

View(filtered_toothGrowth)

# Using Group By
#Need to compute the avg Tooth Length for each of the two supplements 
  #used in the study: orange juice or OJ and ascorbic acid or VC. 
    #We'll replace the arrange function with the group by function
filtered_toothGrowth2<-ToothGrowth %>%
  filter(dose==0.5)%>%
  group_by(supp)%>%
  summarise(mean_len=mean(len,na.rm=T))

View(filtered_toothGrowth2)

d<-"April 10, 2019"
dmultinom()
