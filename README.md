# Exploratory Sales Data Analysis

## Project Overview

This project is an exploratory data analysis of sales data for an electronics store. The goal is to clean a raw dataset, analyze it to answer key business questions, and visualize the findings. This demonstrates a complete data analysis workflow, from data wrangling and cleaning to generating actionable insights.

## Skills Demonstrated

-   **Data Cleaning & Preparation:** Merged 12 separate CSV files, handled missing values (`NaN`), and corrected data types for accurate analysis.
-   **Feature Engineering:** Created new columns (Month, City, Sales) from existing data to enable deeper analysis.
-   **Data Analysis with Pandas:** Used `groupby()` and other Pandas functions to answer business questions like:
    -   What was the best month for sales?
    -   What city had the highest number of sales?
-   **Data Visualization with Matplotlib:** Created clear and professional bar charts to present the findings, including custom formatting for readability.

## How to Run This Project

1.  **Prerequisites:** You will need Python with the Pandas and Matplotlib libraries installed.
2.  **Data:** The `all_data.csv` file is the cleaned and merged dataset used by the script. The original raw data (12 separate monthly files) is not included in this repository.
3.  **Execute the Script:** Run the `analyze_sales.py` script from your terminal. The script will perform the analysis and display two bar charts summarizing the findings for monthly and city-wide sales.
