# SalesCognos

### Project Definition
-----
Purpose	of	the	project is to	present	factual	data	in	a	form	that	end	user	can	easily understand	the	trends	in	the	data	and	can	take	important	business-oriented	decisions.

### Data Warehouse
-----
Data Warehouse is a collection of data from multiple data source which is then processed through ETL Process.
![alt text](/images/warehouse.png)

### Understanding Dataset
-----
The given dataset was fetched from url: https://www.kaggle.com/kyanyoga/sample-sales-data. 
After understanding the dataset, it could be concluded that:
*	Given dataset consist of 25 columns and 2823 data rows.
*	Dataset has information related to order details, product description and the customer contact information.
*	Provided data has been recorded between year 2003 – 2005.
*	Each row consists of “Order Line” details.
*	It has information such as order number, quantity, price, date, status, product line, product code, customer name, contact, address and contact name.

### Cleaning Dataset
-----
The given data could be cleaned before inserting into data warehouse schema. It was found that the format of date was not similar and was not in the standard format. By using python script, the date format was changed to dd-mm-yyyy and removed the hours and minutes from the data. As result the final cleaned data was of smaller size as compared to raw data because the unwanted noise was deleted. The advantages of clean data is to remove noise, maintain consistent data format, to correct major and minor errors, and to increase the efficiency of the reporting and analysis done from the data warehouse tools.

### The Schema
-----
The dataset provided for the case study shows sales data of a company. Fact table includes facts and measures of the business so, it was decided to choose sales as a fact table which can be analyzed to identify the business trends. The data can be used to find the areas where the company need to improvise, which product lines are going in loss. The dimension table provides information about single area of business line and includes multiple data perspectives for analysis. Also, some of the fields in the dataset are included in the dimension table. Five dimensions was identified for the business - location dimension, customer dimension, order dimension, product dimension, and time dimension.

The star schema was chosen due to it's various advantages which is shown below:
![alt text](/images/schema.png)

### Cognos BI
-----
Cognos BI was implemented for the reporting and analysis of dataset. There are various categories of filtration available for reporting of the data. For every small or big business organization the analysis of the product or sales report is very required to construct the near future strategies. Hence data warehouse techniques would be very useful in this case scenario.

#### Sales Report according to Product Names
![alt text](/images/product_name.png)

#### Sales report on basis of Customer Name
![alt text](/images/customer_name.png)

#### Sales report on basis of year and Status of product
![alt text](/images/year.png)

### References
“ETL and its Application in Data Warehouses”. Available: https://www.seguetech.com/etl-application-data-warehouses/
