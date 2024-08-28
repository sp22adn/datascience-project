Data Science FINAL PROJECT REPORT 

Project Title:  
Comparison of Ensemble Machine Learning Algorithms vs Individual Machine learning Algorithms for House price prediction     

my project is mailnly based on the comparision of predictive performances of the single and collective models of the machine learning frame work on the record from king county, USA. Several models such as linear Regression, support vector Machine (SVM), Decision Tree, Random forest, Gradient Boosting, AdaBoost, and XGBoost are used and their performances are compared on three different splits of data (80:20, 70:30, and 60:40), to predict the house prices based on the data.
Here the data is splitted into training and testing, then the results are assessed with essential measures such as Root Mean  Squared Error (RMSE), Mean Absolute Error (MAE) and R-squared (R²), the accuracy and reliability of the models.
 Comparing the errors and the R-squared values of all models, we can note that Linear Regression and XGBoost models have, as a rule, the lowest errors and the highest R-squared values that proves their effectiveness in identifying patterns in the data on housing. AdaBoost also fared badly, specifically in RMSE and R-squared meaning that it is not suitable for this specific dataset.
Creating a Machine Learning model to predict the house price based on the given data. We are going to use the dataset from Kaggle.com. We are also going to create a single page website which will provide the front end to access our model for predictions.

Below data science concepts are used in this project:

Data loading and cleaning
Outlier detection and removal
Feature engineering


Python:
Numpy and Pandas for data cleaning
Matplotlib for data visualization
Sklearn for model building
Google Colaboratory Notebook


 Data set:
 https://www.kaggle.com/datasets/harlfoxem/housesalesprediction
 csv file:"C:\Users\sp22adn\Downloads\kc_house_data.csv"
