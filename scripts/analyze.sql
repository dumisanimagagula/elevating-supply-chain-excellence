--What are the top-selling products in terms of gross sales?
SELECT 
    ProductName,
    SUM(GrossSales) AS TotalGrossSales
FROM 
    orders_and_shipments
GROUP BY 
    ProductName
ORDER BY 
    TotalGrossSales DESC;

--Can you provide a breakdown of gross sales by product department?
SELECT 
    ProductDepartment,
    SUM(GrossSales) AS TotalGrossSales
FROM 
    orders_and_shipments
GROUP BY 
    ProductDepartment;

--How does the order fulfillment time vary across different warehouses?
SELECT 
    o.WarehouseCountry,
    AVG(f.WarehouseOrderFulfillmentDays) AS AvgFulfillmentTime
FROM 
    fulfillment f
JOIN 
    orders_and_shipments o ON f.ProductName = o.ProductName
GROUP BY 
    o.WarehouseCountry;

--What is the average discount percentage for orders in each product category?
SELECT 
    ProductCategory,
    AVG(DiscountPercentage) AS AvgDiscountPercentage
FROM 
    orders_and_shipments
GROUP BY 
    ProductCategory;

--Which warehouse has the highest and lowest inventory levels?
SELECT 
    o.WarehouseCountry,
    MAX(i.WarehouseInventory) AS HighestInventory,
    MIN(i.WarehouseInventory) AS LowestInventory
FROM 
    orders_and_shipments o
JOIN 
    inventory i ON o.ProductName = i.ProductName
GROUP BY 
    o.WarehouseCountry;

--What is the average profit margin for each product category?
SELECT 
    ProductCategory,
    AVG(Profit / GrossSales) AS AvgProfitMargin
FROM 
    orders_and_shipments
GROUP BY 
    ProductCategory;

--Can you identify any seasonal trends in order quantities or gross sales?
SELECT 
    YEAR(OrderYearMonth) AS SalesYear,
    MONTH(OrderYearMonth) AS SalesMonth,
    SUM(OrderQuantity) AS TotalOrderQuantity,
    SUM(GrossSales) AS TotalGrossSales
FROM 
    orders_and_shipments
GROUP BY 
    YEAR(OrderYearMonth), MONTH(OrderYearMonth)
ORDER BY 
    SalesYear, SalesMonth;

--What is the average shipment duration for each shipment mode?
SELECT 
    ShipmentMode,
    AVG(ShipmentDaysScheduled) AS AvgShipmentDuration
FROM 
    orders_and_shipments
GROUP BY 
    ShipmentMode;

--Are there any products with consistently high or low discount percentages?
SELECT 
    ProductName,
    AVG(DiscountPercentage) AS AvgDiscountPercentage
FROM 
    orders_and_shipments
GROUP BY 
    ProductName
ORDER BY 
    AvgDiscountPercentage DESC;

--How does the inventory cost per unit correlate with the profit margin?
SELECT 
    i.ProductName,
    AVG(i.InventoryCostPerUnit) AS AvgInventoryCostPerUnit,
    AVG(o.Profit / o.GrossSales) AS AvgProfitMargin
FROM 
    inventory i
JOIN 
    orders_and_shipments o ON i.ProductName = o.ProductName
GROUP BY 
    i.ProductName;

--What are the most and least profitable product categories?
SELECT 
    ProductCategory,
    SUM(Profit) AS TotalProfit
FROM 
    orders_and_shipments
GROUP BY 
    ProductCategory
ORDER BY 
    TotalProfit DESC;

--Can you provide a geographical breakdown of customer markets and their corresponding gross sales?
SELECT 
    CustomerMarket,
    SUM(GrossSales) AS TotalGrossSales
FROM 
    orders_and_shipments
GROUP BY 
    CustomerMarket;

--Is there a correlation between warehouse inventory levels and order fulfillment time?
SELECT 
    o.WarehouseCountry,
    AVG(f.WarehouseOrderFulfillmentDays) AS AvgFulfillmentTime,
    AVG(i.WarehouseInventory) AS AvgInventoryLevel
FROM 
    orders_and_shipments o
JOIN 
    fulfillment f ON o.ProductName = f.ProductName
JOIN 
    inventory i ON o.ProductName = i.ProductName
GROUP BY 
    o.WarehouseCountry;

--What is the overall trend in gross sales over the years?
SELECT 
    YEAR(OrderYearMonth) AS SalesYear,
    SUM(GrossSales) AS TotalGrossSales
FROM 
    orders_and_shipments
GROUP BY 
    YEAR(OrderYearMonth)
ORDER BY 
    SalesYear;

--Are there any products that have experienced a significant increase or decrease in sales over time?
SELECT 
    ProductName,
    MIN(OrderYearMonth) AS FirstSale,
    MAX(OrderYearMonth) AS LastSale,
    SUM(GrossSales) AS TotalGrossSales
FROM 
    orders_and_shipments
GROUP BY 
    ProductName
HAVING 
    COUNT(DISTINCT OrderYearMonth) > 1
ORDER BY 
    TotalGrossSales DESC;

--How does the discount percentage impact the overall profit for each product category?
SELECT 
    ProductCategory,
    AVG(DiscountPercentage) AS AvgDiscountPercentage,
    AVG(Profit) AS AvgProfit
FROM 
    orders_and_shipments
GROUP BY 
    ProductCategory;

--What is the average order quantity for different product categories?
SELECT 
    ProductCategory,
    AVG(OrderQuantity) AS AvgOrderQuantity
FROM 
    orders_and_shipments
GROUP BY 
    ProductCategory;

--Are there any notable trends in shipment days compared to scheduled shipment days?
SELECT 
    ShipmentYear,
    ShipmentMonth,
    AVG(ShipmentDaysScheduled - ShipmentDaysScheduled) AS AvgShipmentDelay
FROM 
    orders_and_shipments
GROUP BY 
    ShipmentYear, ShipmentMonth;

--How does the warehouse country impact order quantities and gross sales?
SELECT 
    WarehouseCountry,
    SUM(OrderQuantity) AS TotalOrderQuantity,
    SUM(GrossSales) AS TotalGrossSales
FROM 
    orders_and_shipments
GROUP BY 
    WarehouseCountry;