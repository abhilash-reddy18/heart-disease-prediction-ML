# Heart Disease Prediction using Machine Learning

## Project Overview
This project predicts the presence of heart disease using a Logistic Regression model. The aim is to analyze clinical features and determine whether a patient is likely to have heart disease.

## Dataset
The dataset contains patient medical attributes including:

- Age
- Sex
- Chest Pain Type (cp)
- Resting Blood Pressure (trestbps)
- Cholesterol (chol)
- Fasting Blood Sugar (fbs)
- Resting ECG (restecg)
- Maximum Heart Rate Achieved (thalach)
- Exercise Induced Angina (exang)
- ST Depression (oldpeak)
- Slope of ST segment (slope)
- Number of Major Vessels (ca)
- Thalassemia (thal)

## Machine Learning Workflow

1. Data Loading
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Correlation Analysis
5. Feature Scaling using StandardScaler
6. Train-Test Split (80-20)
7. Logistic Regression Model Training
8. Model Evaluation

## Model Evaluation

Accuracy: **91.6%**

Confusion Matrix:

```
[[32, 0],
 [5, 23]]
```

ROC-AUC Score: **0.95**

## Key Insights

- Number of major vessels (ca) strongly influences heart disease prediction.
- Exercise induced angina (exang) is an important risk factor.
- Chest pain type and ST depression (oldpeak) also contribute significantly.

## Technologies Used
      
- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## Author

**Abhilash Reddy Donthireddy**  
Machine Learning Enthusiast | Aspiring Data Scientist
