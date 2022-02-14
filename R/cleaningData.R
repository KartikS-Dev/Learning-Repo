head(penguins)

penguin_By_Len<-penguins%>%
  arrange(bill_length_mm)
head(penguin_By_Len)

#to sort in descending order AND GETTING ONLY MALES
penguin_By_Len_desc<-penguins%>%
  filter(sex=="male")%>%
  arrange(-bill_length_mm)

head(penguin_By_Len_desc) # this is showing on console , 
                            #to view as data frame use view()


penguin_By_Len_desc_specific_cols<-penguin_By_Len_desc%>%
  select(species,island,bill_length_mm,sex)

View(penguin_By_Len_desc_specific_cols)



#Using group by to get average height of males according to species
avg_height_of_males_in_species<-penguin_By_Len_desc_specific_cols%>%
   group_by(species)%>%
   drop_na()%>% # this will remove the rows with missing values
   summarise(avg_height=mean(bill_length_mm))
   

view(avg_height_of_males_in_species)

#max bill length per specie
max_bil_length_males_per_specie<-penguins%>%
  group_by(species)%>%
  drop_na()%>%
  summarise(max_Height=max(bill_length_mm))
  
view(max_bil_length_males_per_specie)

# bill lengths of males per specie and island
bill_length_males_per_specie_and_island<-penguins%>%
  group_by(species,island)%>%
  drop_na()%>%
  filter(sex=="male")%>%
  summarise(max_Height=max(bill_length_mm),
            avg_Height=mean(bill_length_mm),
            min_Height=min(bill_length_mm))

view(bill_length_males_per_specie_and_island)

