# House Price Prediction Using Machine Learning Models

## Overview
This project focuses on **Comparing Ensemble Machine Learning Algorithms vs. Individual Machine Learning Algorithms for House Price Prediction** using the King County, USA housing dataset. The primary goal of the research is to evaluate how ensemble learning methods compare to individual machine learning models in predicting house prices and to assess the effective performance benefits through ensemble algorithms.

Several algorithms are implemented, including:
- **Linear Regression**
- **Support Vector Machine (SVM)**
- **Decision Tree Regressor**
- **Random Forest Regressor**
- **Gradient Boosting Regressor**
- **AdaBoost Regressor**
- **XGBoost Regressor**

The performance of these models is assessed using evaluation metrics such as:
- **Root Mean Squared Error (RMSE)**
- **Mean Absolute Error (MAE)**
- **R-squared (R²)**

## Project Structure
This repository contains the following key components:

- **data/**: Dataset files and any other relevant data used for analysis.
- **notebooks/**: Jupyter Notebooks containing the data analysis, modeling, and evaluation.
- **src/**: Python scripts for model building, training, and evaluation.
- **streamlit_app/**: Files related to the deployment of the Streamlit web application.
- **README.md**: Project description and instructions.

## Dataset
The dataset used in this research is the **House Sales in King County, USA** dataset, which contains features such as the number of bedrooms, bathrooms, living area size, etc. These features are used to predict the house price.

### Dataset Link
You can access the dataset [here](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction).

## Installation
To run this project locally, follow the instructions below:

1. Clone the repository:
   ```bash
   git clone https://github.com/username/house-price-prediction.git
   cd house-price-prediction
