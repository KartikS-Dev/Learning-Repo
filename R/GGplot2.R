#plot to show body msss and fliper length in 3 penguin species
#resultant plot shows positive relation ship , 
    #means larger the penguine large is the flipper
ggplot(data = penguins)+ 
  # this code initializes the plot with 0,0
  #+ sign is used to add layers to plot
  # geom_point tell the function to plot using points
  # AES is property that tell the position , color ,size or shape
  # mapping tells R what aesthetics to use for the plot 
  # x and y are the axes
  geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g))


#ploting with segregation of species using color
ggplot(data = penguins)+
  geom_point(mapping = aes(x= flipper_length_mm,y=body_mass_g,color=species))



#ploting with segregation of species using shape
ggplot(data = penguins)+
  geom_point(mapping = aes(x= flipper_length_mm,y=body_mass_g,shape=species))



#ploting with segregation of species using shape and color
ggplot(data = penguins)+
  geom_point(mapping = aes(x= flipper_length_mm,y=body_mass_g,color=species,
                           shape=species))

#ploting with segregation of species using shape ,color and size
ggplot(data = penguins)+
  geom_point(mapping = aes(x= flipper_length_mm,y=body_mass_g,color=species,
                           shape=species,size=species))

#ploting with segregation of species using alpha(transperency)
ggplot(data = penguins)+
  geom_point(mapping = aes(x= flipper_length_mm,y=body_mass_g,color=species,
                           shape=species,alpha=species))


#changing appearance of overall plot
ggplot(data = penguins)+
  geom_point(mapping = aes(x= flipper_length_mm,y=body_mass_g,shape=species,
                           alpha=species),color="green")

#geom smooth
ggplot(data = penguins)+
  geom_smooth(mapping = aes(x= flipper_length_mm,y=body_mass_g),color="yellow")+
  geom_point(mapping = aes(x= flipper_length_mm,y=body_mass_g,color=species,
                           shape=species))


#geom smooth with linetype
ggplot(data = penguins)+
  geom_smooth(mapping = aes(x= flipper_length_mm,y=body_mass_g,linetype=species)
              ,color="green")


#geom jitter
ggplot(data = penguins)+
  geom_jitter(mapping = aes(x= flipper_length_mm,y=body_mass_g,color=species,
                           shape=species))


#using Bar Graphs 
#bar only take one axis and gives the count on other axis
#color only gives outline to bar
#fill ,fills the bars
ggplot(data=diamonds)+
  geom_bar(mapping =aes(x=cut ,fill=cut) , color="red" )

#using clarity col in data set to get scatter bar 
ggplot(data=diamonds)+
  geom_bar(mapping =aes(x=cut ,fill=clarity) , color="red" )

#faceting
#facet_wrap
ggplot(data = penguins)+
  geom_jitter(mapping = aes(x= flipper_length_mm,y=body_mass_g,
                            color=species,shape=species))+
  facet_wrap(~sex)

ggplot(data=diamonds)+
  geom_bar(mapping = aes(x=cut,fill=clarity))+
  facet_wrap(~clarity)

#Annotate and Label
# adding title , subtitle , caption ,annotation and many more to plot
ggplot(data=diamonds)+
  geom_bar(mapping =aes(x=cut ,fill=cut) , color="red" )+
  labs(title="Diamonds : diamond cuts mostly sold",
       subtitle = "Sample of Diamond Sales", 
       caption="data collected from 2019-2021")+
  annotate("text",x=2,y=15000,label="Ideal Cut is top seller",
           color="purple",fontface="bold",size=4,angle=45)
#to save use export option or ggsave will save the most recent one
ggsave("demoPlot.png")

