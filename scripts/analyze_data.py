#Import necessary libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load datasets

fulfillment_data = pd.read_csv('datasets/fulfillment.csv')
inventory_data = pd.read_csv('datasets/inventory.csv')
orders_and_shipments_data = pd.read_csv('datasets/orders_and_shipments.csv')

fulfillment_df = pd.read_csv('datasets/fulfillment.csv')
inventory_df = pd.read_csv('datasets/inventory.csv')
orders_shipments_df = pd.read_csv('datasets/orders_and_shipments.csv')

# Join datasets based on common columns
merged_data = pd.merge(orders_and_shipments_data, fulfillment_data, on='Product Name', how='inner')
merged_data = pd.merge(merged_data, inventory_data, on='Product Name', how='inner')

merged_df = pd.merge(orders_shipments_df, fulfillment_df, on='Product Name')

#Explore the structure of each dataset

print("Fulfillment Data:")
print(fulfillment_data.info())
print("\nInventory Data:")
print(inventory_data.info())
print("\nOrders and Shipments Data:")
print(orders_and_shipments_data.info())

# Basic statistical summary

print("\nFulfillment Data Summary:")
print(fulfillment_data.describe())
print("\nInventory Data Summary:")
print(inventory_data.describe())
print("\nOrders and Shipments Data Summary:")
print(orders_and_shipments_data.describe())

# What are the top-selling products in terms of gross sales?

top_selling_products = orders_shipments_df.groupby('Product Name')[' Gross Sales '].sum().nlargest(10)
print("Top-selling products:")
print(top_selling_products)

# Can you provide a breakdown of gross sales by product department?

gross_sales_by_department = orders_shipments_df.groupby('Product Department')[' Gross Sales '].sum()
print("\nGross sales breakdown by product department:")
print(gross_sales_by_department)

# How does the order fulfillment time vary across different warehouses?

fulfillment_time_by_warehouse = merged_df.groupby('Warehouse Country')[' Warehouse Order Fulfillment (days) '].mean()
print("\nAverage order fulfillment time by warehouse:")
print(fulfillment_time_by_warehouse)

# Plotting the average order fulfillment time by warehouse

sns.barplot(x=fulfillment_time_by_warehouse.index, y=fulfillment_time_by_warehouse.values)
plt.title('Average Order Fulfillment Time by Warehouse')
plt.xlabel('Warehouse Country')
plt.ylabel('Average Fulfillment Time (days)')
plt.show()

# What is the average discount percentage for orders in each product category?

# Convert 'Discount %' column to numeric
orders_shipments_df[' Discount % '] = pd.to_numeric(orders_shipments_df[' Discount % '], errors='coerce')

avg_discount_by_category = orders_shipments_df.groupby('Product Category')[' Discount % '].mean()
print("\nAverage discount percentage by product category:")
print(avg_discount_by_category)

# Plotting the average discount percentage by product category

# Increase the figure size to make more room for x-axis labels
plt.figure(figsize=(12, 6))

avg_discount_by_category.plot(kind='bar', color='skyblue', width=0.8)

plt.title('Average Discount Percentage by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Average Discount Percentage')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Which warehouse has the highest and lowest inventory levels?

highest_inventory_warehouse = inventory_df.loc[inventory_df[' Warehouse Inventory '].idxmax()]['Product Name']
lowest_inventory_warehouse = inventory_df.loc[inventory_df[' Warehouse Inventory '].idxmin()]['Product Name']
print(f"\nWarehouse with the highest inventory: {highest_inventory_warehouse}")
print(f"Warehouse with the lowest inventory: {lowest_inventory_warehouse}")

# What is the average profit margin for each product category?

avg_profit_margin_by_category = orders_shipments_df.groupby('Product Category')[' Profit '].mean()
print("\nAverage profit margin by product category:")
print(avg_profit_margin_by_category)

# Plotting the average profit margin by product category

# Increase the figure size to make more room for x-axis labels
plt.figure(figsize=(12, 6))

avg_profit_margin_by_category.plot(kind='bar', color='lightgreen', width=0.8)

plt.title('Average Profit Margin by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Average Profit Margin')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Can you identify any seasonal trends in order quantities or gross sales?

seasonal_trends = orders_shipments_df.groupby([' Order Year ', ' Order Month '])[['Order Quantity', ' Gross Sales ']].mean()
print("\nSeasonal Trends in Order Quantities and Gross Sales:")
print(seasonal_trends)

# Plot Seasonal Trends in Order Quantities and Gross Sales

seasonal_trends.plot(kind='line', marker='o')
plt.title('Seasonal Trends in Order Quantities and Gross Sales')
plt.xlabel('Year and Month')
plt.ylabel('Average Quantity / Gross Sales')
plt.xticks(rotation=45)
plt.show()

# What is the average shipment duration for each shipment mode?

avg_shipment_duration_by_mode = orders_shipments_df.groupby('Shipment Mode')[' Shipment Days - Scheduled '].mean()
print("\nAverage Shipment Duration by Shipment Mode:")
print(avg_shipment_duration_by_mode)

# Plot Average Shipment Duration by Shipment Mode

avg_shipment_duration_by_mode.plot(kind='bar', color='lightblue')
plt.title('Average Shipment Duration by Shipment Mode')
plt.xlabel('Shipment Mode')
plt.ylabel('Average Shipment Duration (Days)')
plt.show()

# Are there any products with consistently high or low discount percentages?

discount_percentages = orders_shipments_df.groupby('Product Name')[' Discount % '].mean()
high_discount_products = discount_percentages[discount_percentages > 0.2].index
low_discount_products = discount_percentages[discount_percentages < 0.05].index
print("\nProducts with Consistently High Discount Percentages:")
print(high_discount_products)
print("\nProducts with Consistently Low Discount Percentages:")
print(low_discount_products)

# What are the most and least profitable product categories?

profitable_categories = avg_profit_margin_by_category.idxmax(), avg_profit_margin_by_category.idxmin()
print("\nMost Profitable Product Category:", profitable_categories[0])
print("Least Profitable Product Category:", profitable_categories[1])

# Can you provide a geographical breakdown of customer markets and their corresponding gross sales?

geographical_breakdown = orders_shipments_df.groupby(['Customer Market', 'Customer Region', 'Customer Country'])[' Gross Sales '].sum()
print("\nGeographical Breakdown of Customer Markets and Gross Sales:")
print(geographical_breakdown)

# What is the overall trend in gross sales over the years?

overall_gross_sales_trend = orders_shipments_df.groupby(' Order Year ')[' Gross Sales '].sum()
print("\nOverall Trend in Gross Sales Over the Years:")
print(overall_gross_sales_trend)

# Are there any products that have experienced a significant increase or decrease in sales over time?

product_sales_over_time = orders_shipments_df.groupby(['Product Name', ' Order Year '])['Order Quantity'].sum().unstack()
product_sales_change = (product_sales_over_time.iloc[:, -1] - product_sales_over_time.iloc[:, 0]) / product_sales_over_time.iloc[:, 0]
significant_sales_change = product_sales_change[product_sales_change.abs() > 0.5].index
print("\nProducts with Significant Increase or Decrease in Sales Over Time:")
print(significant_sales_change)

# What is the average order quantity for different product categories?

avg_order_quantity_by_category = orders_shipments_df.groupby('Product Category')['Order Quantity'].mean()
print("\nAverage Order Quantity for Different Product Categories:")
print(avg_order_quantity_by_category)

# What are the most common shipment modes used?

most_common_shipment_modes = orders_shipments_df['Shipment Mode'].value_counts().idxmax()
print("\nMost Common Shipment Modes:")
print(most_common_shipment_modes)

# Plot Most Common Shipment Modes

plt.bar(x=most_common_shipment_modes, height=orders_shipments_df['Shipment Mode'].value_counts()[most_common_shipment_modes], color='lightcoral')
plt.title('Most Common Shipment Modes')
plt.xlabel('Shipment Mode')
plt.ylabel('Frequency')
plt.show()