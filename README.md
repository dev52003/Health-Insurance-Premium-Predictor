# Health Insurance Premium Prediction

## 🚀 Project Overview

This project aims to predict health insurance premiums for individuals based on their demographic and health-related attributes. The goal is to build an accurate regression model by performing comprehensive data analysis, feature engineering, and evaluating multiple machine learning algorithms. The final, optimized model is deployed as an interactive web application using Streamlit.

---

## 📋 Table of Contents
- [Problem Statement](#problem-statement)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Key Insights & Results](#key-insights--results)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [How to Run This Project](#how-to-run-this-project)
- [Deployment](#deployment)

---

## 🎯 Problem Statement

The objective of this project is to develop a machine learning model that can accurately predict the annual medical insurance premium (`expenses`) an individual is likely to incur. By analyzing factors such as age, BMI, smoking habits, and number of children, the model can provide valuable insights for both insurance providers in risk assessment and for individuals in understanding their potential healthcare costs.

---

## 💾 Dataset

The dataset used for this project was sourced from Kaggle. It contains real-world data on individual insurance policyholders.

- **Source:** [Kaggle - Health Insurance Marketplace](https://www.kaggle.com/datasets/mirichoi0218/insurance)
- **Size:** 1,338 records, 7 features.
- **Features:**
    - `age`: Age of the primary beneficiary.
    - `sex`: Gender of the beneficiary (female, male).
    - `bmi`: Body Mass Index.
    - `children`: Number of children covered by health insurance.
    - `smoker`: Whether the person smokes (yes, no).
    - `region`: The beneficiary's residential area in the US (northeast, southeast, southwest, northwest).
    - `expenses`: Individual medical costs billed by health insurance (Target Variable).

---

## ⚙️ Methodology

The project follows a structured machine learning workflow:

1.  **Data Cleaning & Preprocessing:** The dataset was loaded, inspected for missing values, and duplicates were removed to ensure data quality.
2.  **Exploratory Data Analysis (EDA):** Univariate and bivariate analyses were conducted to understand feature distributions and their relationships with insurance expenses. Key drivers of cost were identified through visualizations like histograms, count plots, and a correlation heatmap.
3.  **Feature Engineering:** The dataset was split into training (80%) and testing (20%) sets. Categorical features (`sex`, `smoker`, `region`) were transformed into numerical format using One-Hot Encoding within a Scikit-learn `Pipeline`.
4.  **Model Building:** Five different regression models were trained to predict the `expenses` target variable:
    - Linear Regression (Baseline)
    - Decision Tree Regressor
    - Polynomial Regression
    - Random Forest Regressor
    - Gradient Boosting Regressor
5.  **Model Evaluation:** The performance of each model was systematically compared using R-squared (R²), Mean Absolute Error (MAE), and Mean Squared Error (MSE) on the test set.
6.  **Model Deployment:** The best-performing model was serialized using `pickle` and deployed as an interactive web application using **Streamlit**.

---

## 📈 Key Insights & Results

### EDA Insights:
- **Smoking is the strongest predictor of cost:** Premiums for smokers are, on average, **~380% higher** than for non-smokers.
- **Age is a significant factor:** There is a positive correlation of **+0.30** between age and insurance expenses.
- **BMI also influences cost:** A higher BMI is generally associated with higher premiums, showing a **+0.20** correlation with expenses.

### Model Performance:
The Gradient Boosting Regressor was the top-performing model, demonstrating high accuracy and a significant improvement over the baseline.

| Model | R² Score | MAE ($) |
| :--- | :--- | :--- |
| Linear Regression | 80.69% | 4,177 |
| Decision Tree | 80.19% | 2,755 |
| Polynomial Regression | 87.09% | 3,049 |
| Random Forest | 84.69% | 3,539 |
| **Gradient Boosting** | **90.05%** | **2,511** |

The final model achieved an **R² of 90.05%**, representing a **12% relative improvement** over the baseline model.

---

## 🛠️ Technologies Used

- **Programming:** Python 3
- **Libraries:**
    - **Data Manipulation:** Pandas, NumPy
    - **Data Visualization:** Matplotlib, Seaborn
    - **Machine Learning:** Scikit-learn
    - **Model Deployment:** Streamlit
    - **Serialization:** Pickle
- **Environment:** Jupyter Notebook

---

## 💻 How to Run This Project

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/dev52003/Health-Insurance-Premium-Predictor.git](https://github.com/dev52003/Health-Insurance-Premium-Predictor.git)
    cd health-insurance-prediction
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Explore the analysis in the Jupyter Notebook:**
    ```bash
    jupyter notebook Health_Insurance_Premium_Prediction.ipynb
    ```

5.  **Run the Streamlit web application:**
    ```bash
    streamlit run app.py
    ```
    Navigate to `http://localhost:8501` in your web browser.

---