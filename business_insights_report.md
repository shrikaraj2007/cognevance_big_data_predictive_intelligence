# Business Insights Report – Big Data Analytics & Predictive Intelligence

## 1. Project Overview

This project develops an E-commerce Customer Analytics and Predictive Intelligence system. It combines data preprocessing, SQL analytics, machine learning, and data visualization to understand customer behavior and predict customer churn.

## 2. Dataset Details

* Domain: E-commerce
* Total Records: 1,000 customers
* Original Features: 10
* Processed Features: 12
* Target Variable: Churn

## 3. Data Preprocessing

The dataset was processed using Python and Pandas.

Steps performed:

1. Loaded the customer dataset.
2. Checked for missing values.
3. Removed duplicate records.
4. Filled missing numerical values using median values.
5. Created new features for predictive analysis.

### Feature Engineering

Two additional features were created:

* Total Spending = Total Purchases × Average Order Value
* Income Per Purchase = Annual Income ÷ Total Purchases

## 4. SQL Analytics

SQLite was used to perform customer-level business analysis.

| Gender | Customers | Average Spending | Average Satisfaction |
| ------ | --------: | ---------------: | -------------------: |
| Female |       474 |          6543.76 |                 2.96 |
| Male   |       526 |          6835.21 |                 2.94 |

The SQL analysis demonstrates how customer groups can be analyzed using database queries.

## 5. Predictive Analytics

A Random Forest Classifier was implemented to predict customer churn.

The model used:

* Age
* Annual Income
* Total Purchases
* Average Order Value
* Website Visits
* Customer Satisfaction
* Previous Returns
* Total Spending
* Income Per Purchase

The model achieved 100% accuracy on the test split.

Note: The dataset is synthetically generated and the churn target was created using predefined rules. Therefore, the 100% accuracy should not be interpreted as expected real-world performance.

## 6. Customer Behavior Insights

* Customer spending can be analyzed together with annual income.
* Website visits provide a useful customer engagement measure.
* Customer satisfaction can be used as a behavioral feature.
* Previous returns can help identify customer patterns.
* Churn prediction can support customer retention planning.

## 7. Visualizations

The project contains four visualizations:

1. Customer Churn Distribution
2. Annual Income vs Total Spending
3. Customer Satisfaction Distribution
4. Website Visits vs Total Spending

These charts help identify customer behavior patterns and relationships between important business variables.

## 8. Business Recommendations

* Monitor customers with low engagement.
* Analyze customer satisfaction regularly.
* Identify customers with repeated returns.
* Use churn predictions to support retention strategies.
* Update the model with real customer data for more reliable predictions.
* Track important KPIs through dashboards.

## 9. Project Architecture

```text
Raw Customer Dataset
        ↓
Data Preprocessing
        ↓
Feature Engineering
        ↓
SQLite Database
        ↓
SQL Analytics
        ↓
Machine Learning Model
        ↓
Churn Prediction
        ↓
Data Visualizations
        ↓
Business Insights & Recommendations
```

## 10. Technologies Used

* Python
* Pandas
* NumPy
* SQLite
* SQL
* Scikit-learn
* Matplotlib
* Machine Learning
* Random Forest Classifier

## 11. Conclusion

The Big Data Analytics & Predictive Intelligence project demonstrates a complete analytics workflow from raw customer data to business insights. Python and SQL were used for data processing and analysis, while Random Forest was used for predictive analytics. The visualizations provide a clear view of customer behavior and business KPIs.

The project can be further improved by using larger real-world datasets, advanced time-series models, cloud-based big data technologies, and interactive Power BI or Tableau dashboards.
