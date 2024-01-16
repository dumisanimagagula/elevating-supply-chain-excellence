# ProVisionary Insights: Elevating Supply Chain Excellence

Welcome to the ProVisionary Insights repository, your gateway to unraveling the intricate dynamics of Just In Time's supply chain operations through our advanced Power BI analytics. ProVisionary Insights is a sophisticated project designed to provide comprehensive insights, interactive visualizations, and strategic data analysis for optimizing supply chain performance.

# Elevating Supply Chain Excellence Dashboard

![Elevating Supply Chain Excellence](screenshots/Elevating%20Supply%20Chain%20Excellence.jpg
)

## Dashboard Features

- **Interactive Visualizations:** Explore dynamic charts, graphs, and maps offering a holistic view of the supply chain, allowing in-depth analysis of key performance metrics and trends.

- **Inventory Intelligence:** Analyze inventory data (datasets/inventory.csv) to gain insights into levels, stockouts, and turnover, facilitating optimal inventory management.

- **Order Fulfillment Insights:** Dive into orders and shipments data (datasets/orders_and_shipments.csv) to understand processing, delivery times, and accuracy.

- **Fulfillment Efficiency:** Assess efficiency with data from (datasets/fulfillment.csv), identifying potential bottlenecks in the supply chain.

## Files in this Repository

**datasets/fulfillment.csv:**

- Product Name
- Warehouse Order Fulfillment(days)

**datasets/inventory.csv:**

- Product Name
- Warehouse Inventory
- Inventory Cost Per Unit
- Year Month
- Year
- Month

**datasets/orders_and_shipments.csv:**

- Order Id
- Order Item Id
- Order YearMonth
- Order Year
- Order Month
- Order day
- Order Time
- Order Quantity
- Product Department
- Product Category
- Product Name
- Customer Id
- Customer Market
- Customer Region
- Customer Country
- Warehouse Country
- Shipment Year
- Shipment Month
- Shipment Day
- Shipment Mode
- Shipment Days - Scheduled
- Gross Sales
- Discount %
- Profit

**dashboard/Elevating Supply Chain Excellence.pbix:** Power BI file serving as the foundation for the ProVisionary Insights Dashboard, containing data models, queries, and visualizations.

## Relationship Between Datasets

- ``fulfillment.csv``, ``inventory.csv``, and ``orders_and_shipments.csv`` are utilized within the Power BI Dashboard, ``Elevating Supply Chain Excellence.pbix``. The relationships between datasets are established based on the following columns:

    - **Relationship 1:** ``fulfillment.csv`` and ``orders_and_shipments.csv`` are related by the Product Name column.

    - **Relationship 2:** ``inventory.csv`` and ``orders_and_shipments.csv`` are related by the Product Name column.

    - **Relationship 3:** ``fulfillment.csv`` and ``inventory.csv`` are related by the Product Name column.

## Overview of the dashboard charts

### Score Cards

Get an at-a-glance view of key performance indicators with our Score Cards.

![Score Cards](screenshots/Score%20Cards.jpg
)

### Sales and Profit by Order Year

Dive into the financial landscape with insights into Sales and Profit trends across different order years.

![Sales and Profit by Order Year](screenshots/Sales%20and%20Profit%20by%20Order%20Year.jpg
)

### Sales and Profit by Product Name

Explore detailed profitability analysis by examining Sales and Profit metrics for each product.

![Sales and Profit by Product Name](screenshots/Sales%20and%20Profit%20by%20Product%20Name.jpg
)

### Ordered Quantities by Product Name

Gain a deeper understanding of product demand with a breakdown of ordered quantities by product name.

![Ordered Quantities by Product Name](screenshots/Ordered%20Quantities%20by%20Product%20Name.jpg
)

### Sales and Demand by Product Department

Visualize the relationship between Sales and Demand across different product departments.

![Sales and Demand by Product Department](screenshots/Sales%20and%20Demand%20by%20Product%20Department.jpg
)

## Getting Started

**1.Install Power BI:** Download and install Power BI Desktop from the official Microsoft website if not already installed.

**2.Clone or Download the Repository:** Clone this repository to your local machine or download it as a ZIP file.

**3.Open the Power BI Dashboard:** Launch Power BI Desktop and open the Supply Chain Analytics.pbix file in the "dashboard" folder within the repository.

**4.Refresh Data:** Optionally, refresh the data in the Power BI file for the latest information.

**5.Interact with the Dashboard:** Explore the interactive visualizations, interact with the data, and gain valuable insights into Just In Time's supply chain operations.

Feel free to reach out if you have any questions or need assistance in navigating the ProVisionary Insights Dashboard. Thank you for exploring the pinnacle of supply chain analytics!