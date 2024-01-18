-- Create or use the database
IF NOT EXISTS (SELECT 1 FROM sys.databases WHERE name = 'SalesDatabase')
BEGIN
    CREATE DATABASE SalesDatabase;
END

USE SalesDatabase;

-- Create fulfillment table
IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'fulfillment')
BEGIN
    CREATE TABLE fulfillment (
        ProductName NVARCHAR(MAX),
        WarehouseOrderFulfillmentDays INT
    );
END

-- Create inventory table
IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'inventory')
BEGIN
    CREATE TABLE inventory (
        ProductName NVARCHAR(MAX),
        WarehouseInventory INT,
        InventoryCostPerUnit FLOAT,
        YearMonth NVARCHAR(7),
        Year INT,
        Month INT
    );
END

-- Create orders_and_shipments table
IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'orders_and_shipments')
BEGIN
    CREATE TABLE orders_and_shipments (
        OrderId INT,
        OrderItemId INT,
        OrderYearMonth NVARCHAR(7),
        OrderYear INT,
        OrderMonth INT,
        OrderDay INT,
        OrderTime TIME,
        OrderQuantity INT,
        ProductDepartment NVARCHAR(MAX),
        ProductCategory NVARCHAR(MAX),
        ProductName NVARCHAR(MAX),
        CustomerId INT,
        CustomerMarket NVARCHAR(MAX),
        CustomerRegion NVARCHAR(MAX),
        CustomerCountry NVARCHAR(MAX),
        WarehouseCountry NVARCHAR(MAX),
        ShipmentYear INT,
        ShipmentMonth INT,
        ShipmentDay INT,
        ShipmentMode NVARCHAR(MAX),
        ShipmentDaysScheduled INT,
        GrossSales FLOAT,
        DiscountPercentage FLOAT,
        Profit FLOAT
    );
END
