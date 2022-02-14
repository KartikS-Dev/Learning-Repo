skim_without_charts(penguins)
glimpse(penguins)
head(penguins)

#only need to select species column
getSpecies_Island<-penguins %>%
  select(species)

head(getSpecies_Island)

#Everything Except species column
#put - in front of that column
getExceptSpecies_Island<-penguins %>%
  select(-species)

head(getExceptSpecies_Island)


#change column name 
penguins %>%
  rename(island_Habitat=island)


#upddate all colNames
rename_with(penguins,toupper)

#set by defaut col names to lower case as it the standard
clean_names(penguins)


