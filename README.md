# Big Data Analytics & Predictive Intelligence

## Project Overview

This project develops an E-commerce Customer Analytics and Predictive Intelligence system using Python, SQL, machine learning, and data visualization.

The project analyzes customer behavior, performs SQL-based business analytics, predicts customer churn, and generates business insights.

## Objectives

* Analyze customer behavior
* Perform data preprocessing and feature engineering
* Use SQL for business analytics
* Build a machine learning prediction model
* Create business visualizations
* Analyze customer KPIs
* Generate business recommendations

## Dataset

* Domain: E-commerce
* Records: 1,000 customers
* Original Features: 10
* Processed Features: 12
* Target: Customer Churn

## Technologies Used

* Python
* Pandas
* NumPy
* SQL
* SQLite
* Scikit-learn
* Matplotlib
* Random Forest

## Project Workflow

1. Create and load customer dataset
2. Clean and preprocess data
3. Perform feature engineering
4. Store data in SQLite
5. Perform SQL analytics
6. Train Random Forest model
7. Predict customer churn
8. Create business visualizations
9. Generate business insights

## Feature Engineering

Two new features were created:

* **Total Spending** = Total Purchases × Average Order Value
* **Income Per Purchase** = Annual Income ÷ Total Purchases

## SQL Analytics

SQL was used to analyze customer groups based on gender, spending, and satisfaction.

| Gender | Customers | Average Spending | Average Satisfaction |
| ------ | --------: | ---------------: | -------------------: |
| Female |       474 |          6543.76 |                 2.96 |
| Male   |       526 |          6835.21 |                 2.94 |

## Machine Learning

A Random Forest Classifier was used for customer churn prediction.

### Model Result

**Test Accuracy: 100%**

Note: The dataset and churn target are synthetically generated. Therefore, this accuracy should not be treated as real-world model performance.

## Visualizations

The project includes four charts:

1. Customer Churn Distribution
2. Annual Income vs Total Spending
3. Customer Satisfaction Distribution
4. Website Visits vs Total Spending

## Business Insights

* Customer spending can be analyzed with income and purchasing behavior.
* Website visits provide an indication of customer engagement.
* Customer satisfaction is an important behavioral feature.
* Previous returns can help identify customer patterns.
* Churn prediction can support customer retention strategies.

## Project Architecture

```text
Customer Dataset
       ↓
Data Preprocessing
       ↓
Feature Engineering
       ↓
SQLite Database
       ↓
SQL Analytics
       ↓
Machine Learning
       ↓
Churn Prediction
       ↓
Data Visualization
       ↓
Business Insights
```

## Project Files

* `create_dataset.py` – Creates the customer dataset
* `ecommerce_customer_data.csv` – Original dataset
* `preprocessing.py` – Data preprocessing and feature engineering
* `processed_customer_data.csv` – Processed dataset
* `sql_analysis.py` – SQL analytics
* `customer_analytics.db` – SQLite database
* `predictive_model.py` – Random Forest churn prediction model
* `dashboard.py` – Visualization generation
* `churn_distribution.png` – Churn chart
* `income_vs_spending.png` – Income vs spending chart
* `customer_satisfaction.png` – Satisfaction chart
* `visits_vs_spending.png` – Website visits vs spending chart
* `business_insights_report.md` – Business insights report
* `README.md` – Project documentation

## Future Improvements

* Use larger real-world datasets
* Add Power BI or Tableau interactive dashboards
* Use advanced machine learning models
* Deploy the prediction system as a web application
* Use cloud-based big data technologies

## Conclusion

This project demonstrates a complete data analytics and predictive intelligence pipeline using Python, SQL, machine learning, and visualization. It provides practical experience in customer analytics, predictive modeling, and business intelligence.
