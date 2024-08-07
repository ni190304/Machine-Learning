# Regression Template

# Importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
# library(caTools)
# set.seed(123)
# split = sample.split(dataset$Salary, SplitRatio = 0.8)
# training_set = subset(dataset, split == TRUE)
# test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)

# Fitting poly reg
# Create regressor

# Predicting a new result with L.R

y_pred = predict(lin_reg , data.frame(Level = 6.5))

# Visualizing Lin Reg.

library(ggplot2)
ggplot()+
  geom_point(aes(x= dataset$Level, y = dataset$Salary), colour = 'red')+
  geom_line(aes(x= dataset$Level, y = predict(regressor, newdata = dataset)), colour = 'blue')+
  ggtitle('Truth of Bluff(Regression Model)')+
  xlab('Level')+
  ylab('Salary')

# Visualizing Poly Reg.

library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
ggplot()+
  geom_point(aes(x= dataset$Level, y = dataset$Salary), colour = 'red')+
  geom_line(aes(x= dataset$Level, y = predict(poly_reg, newdata = data.frame(Level = x_grid))), colour = 'blue')+
  ggtitle('Truth of Bluff(Poly_R)')+
  xlab('Level')+
  ylab('Salary')

