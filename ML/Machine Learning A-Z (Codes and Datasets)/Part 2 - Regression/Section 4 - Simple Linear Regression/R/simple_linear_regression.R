setwd('C:/Users/Nihaal/OneDrive/Desktop/DSML/ML/Machine Learning A-Z (Codes and Datasets)/Part 2 - Regression/Section 4 - Simple Linear Regression/R/')
dataset <- read.csv('Salary_Data.csv')

library(caTools)
set.seed(456)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Fitting Simple Linear Regression to the Training set
regressor = lm(formula = Salary ~ YearsExperience, data = training_set)

# Predicting the Test set results
y_pred = predict(regressor, newdata = test_set)

# Visualizing the Training Set results
# install.packages('ggplot2')

library(ggplot2)
ggplot() + 
  geom_point(aes(x = training_set$YearsExperience , y = training_set$Salary),
             colour = 'red') + 
  geom_line(aes(x = training_set$YearsExperience , y = predict(regressor, newdata = training_set)), 
            colour = 'blue') +
  ggtitle('Salary vs Experience(Training Set)') + 
  xlab('Years of Experience') +
  ylab('Salary')

# Visualizing the Test Set results
# install.packages('ggplot2')

library(ggplot2)
ggplot() + 
  geom_point(aes(x = test_set$YearsExperience , y = test_set$Salary),
             colour = 'red') + 
  geom_line(aes(x = training_set$YearsExperience , y = predict(regressor, newdata = training_set)), 
            colour = 'blue') +
  ggtitle('Salary vs Experience(Test Set)') + 
  xlab('Years of Experience') +
  ylab('Salary')