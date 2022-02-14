#Anscombe's quartet

view(quartet)

quartet%>%
  group_by(set)%>%
  summarise(mean_X=mean(x),
            sd_X=sd(x),
            mean_Y=mean(y),
            sd_Y=sd(y),
            corr_X_y=cor(x,y))


