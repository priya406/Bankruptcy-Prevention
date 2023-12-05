# Bankruptcy-Prevention
 

!['Bankruptcy_cover'](https://www.meatpoultry.com/ext/resources/2023/04/28/Bankruptcy_adobe.png?height=667&t=1682699472&width=1080)

## Overview

This repository contains the code and resources for a bankruptcy prediction project. The goal of the project is to model the probability that a business goes bankrupt based on various features. The dataset includes information from 250 companies, with 7 features and a binary target variable indicating bankruptcy or non-bankruptcy.

## Dataset

The dataset consists of the following variables:

1. **industrial_risk:** Risk level in the industrial sector (0=low risk, 0.5=medium risk, 1=high risk).
2. **management_risk:** Risk associated with management (0=low risk, 0.5=medium risk, 1=high risk).
3. **financial_flexibility:** Financial flexibility of the company (0=low flexibility, 0.5=medium flexibility, 1=high flexibility).
4. **credibility:** Credibility level of the company (0=low credibility, 0.5=medium credibility, 1=high credibility).
5. **competitiveness:** Competitiveness of the company (0=low competitiveness, 0.5=medium competitiveness, 1=high competitiveness).
6. **operating_risk:** Operating risk of the company (0=low risk, 0.5=medium risk, 1=high risk).
7. **class:** Target variable indicating bankruptcy or non-bankruptcy.

## Project Structure

- **`data/`:** Directory containing the dataset.
- **`notebooks/`:** Jupyter notebooks for data exploration, preprocessing, and model development.
- **`src/`:** Source code for the classification model.
- **`requirements.txt`:** List of required dependencies for the project.
- **`README.md`:** Documentation providing an overview of the project, dataset, and instructions for running the code.

## Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/Ablu876/bankruptcy-prevention.git
   cd bankruptcy-prevention

2. Install the required dependencies: `pip install -r requirements.txt`
3. Explore the Jupyter notebooks in the notebooks/ directory for data analysis and model
development.
4. Execute the classification model using the code in the src/ directory.

