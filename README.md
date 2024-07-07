# ARIMA Electricity Forecast

This repository contains tools and scripts for forecasting electricity demand using ARIMA models. The project consists of the following components:

- `arima_processing.ipynb`: Jupyter notebook for ARIMA model training and forecasting.
- `eda.ipynb`: Jupyter notebook for exploratory data analysis of electricity demand data.
- `get_data.py`: Python script to fetch and preprocess electricity demand data.
- `utils.py`: Utility functions used across the project.

## Files

### arima_processing.ipynb

This notebook demonstrates the process of training and evaluating ARIMA models for electricity demand forecasting. It includes:

- Data loading and preprocessing.
- ARIMA model fitting and tuning.
- Forecasting future electricity demand.
- Evaluation metrics for model performance.

### eda.ipynb

The exploratory data analysis notebook explores the characteristics and patterns in electricity demand data. It covers:

- Data visualization for understanding trends, seasonality, and anomalies.
- Statistical analysis of electricity demand distribution.
- Correlation analysis with external factors affecting electricity consumption.

### get_data.py

This script is used to automate the retrieval and preprocessing of electricity demand data. Key functionalities include:

- Data fetching from sources (e.g., CSV files, APIs).
- Data cleaning and transformation into a suitable format for modeling.
- Handling missing data and outliers to ensure data quality.

### utils.py

The utility functions module contains reusable code snippets and helper functions used throughout the project. It includes:

- Functions for data loading and saving.
- Mathematical and statistical functions relevant to ARIMA modeling.
- Utility functions for plotting, metrics calculation, and general data manipulation.
