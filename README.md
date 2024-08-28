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

2. Install the required dependencies:
   
   ```bash
   pip install -r requirements.txt
   
3. Run the Jupyter Notebooks in the `notebooks/` directory to train the models and evaluate their performance:

   ```bash
   jupyter notebook


4. To run the Streamlit web application, navigate to the `streamlit_app/` folder and run:

   ```bash
   streamlit run app.py


## Features
- **Exploratory Data Analysis (EDA):** A thorough analysis of the dataset, including distribution plots, correlation heatmaps, and feature engineering.

- **Model Training and Evaluation:** Various machine learning models (individual and ensemble) are trained on different data splits (80:20, 70:30, 60:40) and evaluated using the RMSE, MAE, and R-squared metrics.

- **Feature Engineering:** The dataset is enhanced by adding new features like house age and renovation status to improve model accuracy.

- **Streamlit Application:** A user-friendly web application where users can input the features of a house and predict its price using the best-performing machine learning model.

## Usage
- **Model Comparison:** Evaluate the performance of different machine learning models on predicting house prices.
- **Price Prediction Web App:** The Streamlit app allows users to input house features and get a price estimate using the trained model.

## Results
The analysis shows that **Linear Regression** and **XGBoost** models yielded the best results across various splits and metrics. The RMSE and MAE were lowest for these models, while the R-squared values were the highest, making them the most reliable for predicting house prices in King County, USA.

## Future Work
- **Expansion of feature sets** to include more detailed neighborhood and economic factors.
- **Use of advanced deep learning models** such as CNNs or RNNs for improved predictions.
- **Exploration of interpretability techniques** to better understand the importance of features influencing house prices.
