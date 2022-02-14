#DataFrames
#Diamonds DataSet
# data("diamonds") to load dataset
# library(ggplot2) to load specific pacakage

View(diamonds)

#to view on some rows , use head() , it will give first 6 rows
#Quick preview
head(diamonds)

#structure of data frame
str(diamonds)

#get only col_names
colnames(diamonds)


# mutate() of dplyr pacakge can be used to make changes in data frame
mutate(diamonds , carat_X100= carat*100)
