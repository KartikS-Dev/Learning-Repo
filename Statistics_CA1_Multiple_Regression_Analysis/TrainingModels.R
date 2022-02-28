#Training Models based on the Selected Features

x_train_path = "C://Users//offic//OneDrive//Documents//NationalCollegeOfIreland//GitRepo//Learning-Repo//Python//Statistics-CA1-Multiple Regression Analysis//X_train.csv"
x_train<- read.csv(x_train_path)

x_test_path = "C://Users//offic//OneDrive//Documents//NationalCollegeOfIreland//GitRepo//Learning-Repo//Python//Statistics-CA1-Multiple Regression Analysis//X_test.csv"
x_test<- read.csv(x_test_path)

model1=lm(income~creddebt+othdebt+carvalue+edcat+yrsempl+jobsat+homeown,data = x_train)

summary(model1)
abline(Mod2,col('green'))
plot(model1)
fitted_model1=fitted.values(model1)
head(fitted_model1)

View(x_train)


prediction<-predict(model1,x_test)

library(tidyverse)

# package to compute
# cross - validation methods
library(caret)

data.frame( R2 = R2(prediction, x_test$income ),
            RMSE = RMSE(prediction, x_test$income),
            MAE = MAE(prediction, x_test$income))


train_control <- trainControl(method = "LOOCV")

# training the model by assigning sales column
# as target variable and rest other column
# as independent variable
model <- train(income ~creddebt+othdebt+carvalue+edcat+yrsempl+jobsat+homeown, data = x_train,
               method = "lm",
               trControl = train_control)

# printing model performance metrics
# along with other details
print(model)
