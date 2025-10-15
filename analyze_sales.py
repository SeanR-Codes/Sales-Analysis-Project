#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 07:30:15 2025

@author: SeanR-Codes
"""

import pandas as pd
import os
import matplotlib.pyplot as plt

# Get a list of all files in directory
files = [file for file in os.listdir('./Sales_Data')]

# Create an empty DF to store data
all_months_data = pd.DataFrame()

# Loop through files, read them, and append to main DF
for file in files:
    df = pd.read_csv("./Sales_Data/" + file)
    all_months_data = pd.concat([all_months_data, df])

# Save data to new CSV
all_months_data.to_csv("all_data.csv", index=False)

print("\n --- All files have been merged! ---")

# --- Data Cleanup ---

# Read in DF
df = pd.read_csv("all_data.csv")

# Find NaN values and display
nan_df = df[df.isna().any(axis=1)]
print("\n --- Found the following empty rows: ---")
print(nan_df.head())

# Drop NaN to clean data
df = df.dropna(how='all')
print("Empty rows have been removed.")

# Find rows containing "Or" and remove them
df = df[df['Order Date'].str[0:2] != 'Or']
print("Removed rows with bad date entries.")

# Convert "Order Date" column to proper datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%y %H:%M')
print("Converted 'Order Date' column to datetime format.")

# Convert columns to correct numeric type for calculations
df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'])
df['Price Each'] = pd.to_numeric(df['Price Each'])
print("Converted 'Quantity Ordered' and 'Price Each' to numeric.")

# Create 'Sales' column
df['Sales'] = df['Quantity Ordered'] * df['Price Each']
print("Created 'Sales' column.")

# Display first five rows
print("\nDataFrame with new 'Sales' column:")
print(df.head())

# Create 'Month' column
df['Month'] = df['Order Date'].dt.month
print("Created 'Month' column.")

print("\nFinal DF with all new columns:")
print(df.head())

# --- Answer the following questions ---

# Question 1: What was the best month for sales? How much was earned?
monthly_sales = df.groupby('Month')['Sales'].sum()

print("\n--- Question 1: What was the best month for sales? ---")
print(monthly_sales.apply(lambda x: f'${x:,.2f}'))

# Divide sales by 1,000,000 to make chart cleaner
sales_in_millions = monthly_sales / 1_000_000

# Create bar chart of monthly sales data
months = range(1, 13)
plt.bar(months, sales_in_millions)

# Add labels and title for clarity
plt.xticks(months)
plt.ylabel('Sales in USD ($)')
plt.xlabel('Month Number')
plt.title('Monthly Sales Performance')

# Display chart
plt.show()

# Question 2: What city had the highest number of sales?

# Pull city from address


def get_city(address):
    return address.split(',')[1].strip()

# Pull state from address


def get_state(address):
    return address.split(',')[2].split(' ')[1]


def format_city_state(address):
    city = get_city(address)
    state = get_state(address)
    return f"{city} ({state})"


# Create 'City' column
df['City'] = df['Purchase Address'].apply(format_city_state)

print("Created 'City' column.")
print("\nDataFrame with new 'City' column:")
print(df.head())

city_sales = df.groupby('City')['Sales'].sum()
print("\n--- Question 2: What city had the highest number of sales? ---")
print(city_sales.apply(lambda x: f'${x:,.2f}'))

# Order cities in same order as sales data
cities = [city for city, df in df.groupby('City')]

# Divide by 1,000,000 to make chart cleaner
city_sales_in_millions = city_sales / 1_000_000

plt.bar(cities, city_sales_in_millions)
plt.xticks(cities, rotation='vertical', size=8)
plt.ylabel("Sales in millions of USD ($)")
plt.xlabel('City Name')
plt.title('Sales Performance by City')

# Ensure everything fits without overlap
plt.tight_layout()
plt.show()
