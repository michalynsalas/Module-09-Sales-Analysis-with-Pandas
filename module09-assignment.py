# Module 9 Assignment: Introduction to Data Analysis with Pandas
# GlobalTech Sales Analysis

# Import required libraries
import pandas as pd
import numpy as np

# Welcome message
print("=" * 60)
print("GLOBALTECH QUARTERLY SALES ANALYSIS")
print("=" * 60)

# TODO 1: Load and Explore the Dataset
# The sales_data.csv file contains data with the following structure:
# - Date: Date of sale (YYYY-MM-DD format)
# - Region: Sales region (North America, Europe, Asia, Latin America)
# - Store: Store identifier
# - Category: Product category (Smartphones, Computers, Audio, Accessories, Wearables)
# - Product: Specific product name
# - Units: Number of units sold
# - Unit_Price: Price per unit in USD
# - Total_Sales: Total sales amount in USD
# - Promotion: Whether the product was on promotion (Yes/No)
# Some entries contain missing values marked as NaN

# REQUIRED VARIABLE NAMES FOR AUTOGRADING:
# - sales_df: Main DataFrame loaded from CSV
# - total_units: Total units sold across all records
# - total_revenue: Total sales amount across all records
# - avg_unit_price: Average unit price across all products
# - na_sales: DataFrame containing only North America sales
# - high_volume_sales: DataFrame with sales where Units > 20
# - phonex_promo: DataFrame with PhoneX products on promotion
# - feb_sales: DataFrame containing February 2024 sales
# - best_product: Product name with highest total sales
# - sales_by_region: Series with total sales by region (sorted descending)
# - avg_units_by_category: Series with average units sold per category
# - promo_comparison: Dictionary with promotion effectiveness metrics
# - missing_counts: Series with count of missing values per column
# - missing_percentages: Series with percentage of missing values per column

# ----- USE THE FOLLOWING CODE TO SIMULATE A CSV FILE (DO NOT MODIFY) -----
from io import StringIO

# Simulated CSV content
csv_content = """Date,Region,Store,Category,Product,Units,Unit_Price,Total_Sales,Promotion
2024-01-15,North America,NA001,Smartphones,PhoneX,12,899.99,10799.88,No
2024-01-18,Europe,EU002,Computers,LaptopPro,8,1299.99,10399.92,Yes
2024-01-20,Asia,AS001,Audio,WirelessEarbuds,25,149.99,3749.75,No
2024-01-22,North America,NA002,Wearables,SmartWatch,15,249.99,3749.85,No
2024-01-25,Latin America,LA001,Smartphones,PhoneX,7,899.99,6299.93,Yes
2024-01-27,Europe,EU001,Accessories,PhoneCase,35,24.99,874.65,No
2024-01-30,Asia,AS002,Smartphones,PhoneSE,18,499.99,8999.82,No
2024-02-02,North America,NA001,Computers,LaptopPro,6,1299.99,7799.94,No
2024-02-05,Europe,EU002,Wearables,SmartWatch,20,249.99,4999.80,Yes
2024-02-08,North America,NA003,Audio,WirelessEarbuds,30,149.99,4499.70,Yes
2024-02-10,Asia,AS001,Accessories,ChargingCable,45,19.99,899.55,No
2024-02-12,Latin America,LA001,Computers,TabletBasic,12,399.99,4799.88,No
2024-02-15,North America,NA002,Smartphones,PhoneSE,14,499.99,6999.86,No
2024-02-18,Europe,EU001,Audio,BlueSpeaker,22,79.99,1759.78,Yes
2024-02-20,Asia,AS002,Wearables,FitnessTracker,28,129.99,3639.72,No
2024-02-22,North America,NA001,Accessories,PhoneCase,50,24.99,1249.50,Yes
2024-02-25,Latin America,LA002,Smartphones,PhoneX,9,,8099.91,No
2024-02-28,Europe,EU002,Computers,LaptopBasic,10,899.99,8999.90,No
2024-03-02,North America,NA003,Wearables,FitnessTracker,,129.99,2599.80,Yes
2024-03-05,Asia,AS001,Smartphones,PhoneSE,15,499.99,7499.85,No
2024-03-08,Europe,EU001,Accessories,ChargingCable,60,19.99,1199.40,Yes
2024-03-10,North America,NA002,Computers,TabletPro,7,599.99,4199.93,No
2024-03-12,Latin America,LA001,Audio,WirelessEarbuds,18,149.99,2699.82,No
2024-03-15,North America,NA001,Wearables,SmartWatch,12,249.99,2999.88,No
2024-03-18,Europe,EU002,Smartphones,PhoneX,11,899.99,9899.89,Yes
2024-03-20,Asia,AS002,Computers,LaptopPro,6,1299.99,7799.94,No
2024-03-22,North America,NA001,Audio,BlueSpeaker,25,79.99,1999.75,No
2024-03-25,Latin America,LA002,Accessories,PhoneCase,40,,999.60,No
"""

# Create a StringIO object (simulates a file)
sales_data_csv = StringIO(csv_content)

# Now you can load this as if it was a CSV file:
# sales_df = pd.read_csv(sales_data_csv)
# ----- END OF SIMULATION CODE -----

# 1.1 Load the dataset and store it in a DataFrame called 'sales_df'
# REQUIRED: Variable name must be 'sales_df'
sales_df = pd.read_csv(sales_data_csv)

# 1.2 Display the first 5 rows of the dataset
print("\nFirst 5 rows:")
print(sales_df.head())

# 1.3 Display basic information about the DataFrame (info() method)
print("\nDataFrame Info:")
sales_df.info()

# 1.4 Get the dimensions of the DataFrame (number of rows and columns)
print("\nDataFrame Dimensions:")
print(f"Rows: {sales_df.shape[0]}, Columns: {sales_df.shape[1]}")

# 1.5 Display summary statistics for numerical columns using describe()
print("\nSummary Statistics:")
print(sales_df.describe())

# TODO 2: Column Selection and Basic Analysis
# 2.1 Select and display only the 'Product', 'Units', and 'Total_Sales' columns
print("\nSelected Columns (Product, Units, Total_Sales):")
print(sales_df[['Product', 'Units', 'Total_Sales']])

# 2.2 Calculate the total units sold across all records
# REQUIRED: Store result in variable 'total_units'
total_units = sales_df['Units'].sum()

# 2.3 Calculate the total sales amount across all records
# REQUIRED: Store result in variable 'total_revenue'
total_revenue = sales_df['Total_Sales'].sum()

# 2.4 Calculate the average unit price per product
# REQUIRED: Store result in variable 'avg_unit_price'
avg_unit_price = sales_df['Unit_Price'].mean()

# TODO 3: Row Selection and Filtering
# 3.1 Select sales from North America region only
# REQUIRED: Store result in variable 'na_sales'
na_sales = sales_df[sales_df['Region'] == 'North America']

# 3.2 Select sales where Units sold is greater than 20
# REQUIRED: Store result in variable 'high_volume_sales'
high_volume_sales = sales_df[sales_df['Units'] > 20]

# 3.3 Select sales of the 'PhoneX' product that were on promotion
# REQUIRED: Store result in variable 'phonex_promo'
phonex_promo = sales_df[(sales_df['Product'] == 'PhoneX') & (sales_df['Promotion'] == 'Yes')]

# 3.4 Select sales from February 2024 (hint: use string methods with the Date column)
# REQUIRED: Store result in variable 'feb_sales'
feb_sales = sales_df[sales_df['Date'].str.startswith('2024-02')]

# TODO 4: Advanced Filtering and Analysis
# 4.1 Find the product with the highest total sales
# REQUIRED: Store product name in variable 'best_product'
best_product = sales_df.groupby('Product')['Total_Sales'].sum().idxmax()

# 4.2 Calculate total sales by region and sort in descending order
# REQUIRED: Store result in variable 'sales_by_region' (pandas Series)
sales_by_region = sales_df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)

# 4.3 Calculate average units sold per category
# REQUIRED: Store result in variable 'avg_units_by_category' (pandas Series)
avg_units_by_category = sales_df.groupby('Category')['Units'].mean()

# 4.4 Compare sales performance of items on promotion vs. not on promotion
# REQUIRED: Store result in dictionary 'promo_comparison' with keys:
# - 'promo_avg_sales': average sale amount for promoted items
# - 'no_promo_avg_sales': average sale amount for non-promoted items
# - 'promo_total_revenue': total revenue from promoted items
# - 'no_promo_total_revenue': total revenue from non-promoted items
promo_sales = sales_df[sales_df['Promotion'] == 'Yes']['Total_Sales']
no_promo_sales = sales_df[sales_df['Promotion'] == 'No']['Total_Sales']

promo_comparison = {
    'promo_avg_sales': promo_sales.mean(),
    'no_promo_avg_sales': no_promo_sales.mean(),
    'promo_total_revenue': promo_sales.sum(),
    'no_promo_total_revenue': no_promo_sales.sum()
}

# TODO 5: Missing Value Detection and Reporting
# 5.1 Identify columns with missing values and count them
# REQUIRED: Store result in variable 'missing_counts' (pandas Series)
missing_counts = sales_df.isnull().sum()

# 5.2 Calculate what percentage of the data is missing in each column
# REQUIRED: Store result in variable 'missing_percentages' (pandas Series)
missing_percentages = (sales_df.isnull().sum() / len(sales_df)) * 100

# TODO 6: Insights and Business Analysis
# 6.1 Create a summary of the top-performing category in each region
# REQUIRED: Store result in variable 'top_categories_by_region' (pandas Series or dict)
category_sales_by_region = sales_df.groupby(['Region', 'Category'])['Total_Sales'].sum()
top_categories_by_region = category_sales_by_region.groupby(level=0).idxmax().apply(lambda x: x[1])

# 6.2 Calculate the average unit price for each product category
# REQUIRED: Store result in variable 'avg_price_by_category' (pandas Series)
avg_price_by_category = sales_df.groupby('Category')['Unit_Price'].mean()

# 6.3 For each product, calculate the total revenue and percentage of overall sales
# REQUIRED: Store result in variable 'product_revenue_analysis' (DataFrame with columns: 'total_revenue', 'percentage')
product_revenue_analysis = sales_df.groupby('Product')['Total_Sales'].sum().to_frame(name='total_revenue')
product_revenue_analysis['percentage'] = (product_revenue_analysis['total_revenue'] / total_revenue) * 100

# TODO 7: Generate Analysis Report
print("\n" + "=" * 60)
print("GLOBALTECH Q1 2024 SALES ANALYSIS REPORT")
print("=" * 60)

# 7.1 Display overall sales performance
# REQUIRED OUTPUT FORMAT:
# Overall Performance:
# - Total Revenue: $XXX,XXX.XX
# - Total Units Sold: XXX
# - Average Sale Value: $XXX.XX
print("\nOverall Performance:")
print(f"- Total Revenue: ${total_revenue:,.2f}")
print(f"- Total Units Sold: {int(total_units)}")
print(f"- Average Sale Value: ${sales_df['Total_Sales'].mean():,.2f}")

# 7.2 Display regional performance summary
# REQUIRED OUTPUT FORMAT:
# Regional Performance:
# [Region]: $XXX,XXX.XX
# ...
print("\nRegional Performance:")
for region, revenue in sales_by_region.items():
    print(f"{region}: ${revenue:,.2f}")

# 7.3 Display product category performance
# REQUIRED OUTPUT FORMAT:
# Category Performance:
# [Category]: Avg Units: XX.X, Avg Price: $XXX.XX
# ...
print("\nCategory Performance:")
for category in avg_units_by_category.index:
    print(f"{category}: Avg Units: {avg_units_by_category[category]:.1f}, Avg Price: ${avg_price_by_category[category]:,.2f}")

# 7.4 Display promotion effectiveness
# REQUIRED OUTPUT FORMAT:
# Promotion Effectiveness:
# - Promoted Items Avg Sale: $XXX.XX
# - Non-Promoted Items Avg Sale: $XXX.XX
# - Revenue from Promotions: $XXX,XXX.XX
# Your code here
print("\nPromotion Effectiveness:")
print(f"- Promoted Items Avg Sale: ${promo_comparison['promo_avg_sales']:,.2f}")
print(f"- Non-Promoted Items Avg Sale: ${promo_comparison['no_promo_avg_sales']:,.2f}")
print(f"- Revenue from Promotions: ${promo_comparison['promo_total_revenue']:,.2f}")
print(f"- Revenue without Promotions: ${promo_comparison['no_promo_total_revenue']:,.2f}")

# 7.5 Report on data quality issues
# REQUIRED OUTPUT FORMAT:
# Data Quality Report:
# - Missing Values Found: [list columns]
# - Total Missing Entries: XXX
missing_columns = missing_counts[missing_counts > 0].index.tolist()

print("\nData Quality Report:")
print(f"- Missing Values Found: {missing_columns}")
print(f"- Total Missing Entries: {int(missing_counts.sum())}")

# 7.6 Provide three key business recommendations based on your analysis
print("\nKEY BUSINESS RECOMMENDATIONS:")

# Recommendation 1
top_region = sales_by_region.idxmax()
print(f"1. Focus inventory and marketing investment in {top_region}, which generated the highest revenue at ${sales_by_region.max():,.2f}.")

# Recommendation 2
top_product_revenue = product_revenue_analysis['total_revenue'].idxmax()
top_product_share = product_revenue_analysis.loc[top_product_revenue, 'percentage']
print(f"2. Prioritize {top_product_revenue} in sales strategy because it is the top revenue-generating product, contributing {top_product_share:.2f}% of total sales.")

# Recommendation 3
if promo_comparison['promo_avg_sales'] < promo_comparison['no_promo_avg_sales']:
    print("3. Reevaluate promotion strategy because promoted items have a lower average sale value than non-promoted items; promotions may be better used for volume-building or specific product categories.")
else:
    print("3. Expand selective promotions because promoted items are producing stronger average sale performance than non-promoted items.")

# Optional: Additional insight displays
print("\nTop Category by Region:")
for region, category in top_categories_by_region.items():
    print(f"- {region}: {category}")

print("\nProduct Revenue Analysis:")
print(product_revenue_analysis.sort_values(by='total_revenue', ascending=False))