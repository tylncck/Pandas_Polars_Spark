# Benchmarking Data Processing Frameworks: Pandas, Polars, and Spark
In today's data-driven world, efficient data processing is paramount for organizations to gain actionable insights and make informed decisions. To shed light on the capabilities of three prominent data processing frameworks, namely Pandas, Polars, and Spark, we embark on a comprehensive benchmarking journey. This comparative study aims to assess the speed and performance of these frameworks across essential data manipulation tasks, including data reading, merging, joining, writing, and performing aggregation calculations. By pitting these tools against each other, we hope to provide valuable insights to data professionals and organizations seeking the most suitable data processing solution for their specific needs.

## Datasets
There are two different datasets synthetically generated to test data processing frameworks:

1. Employees Data: This dataset designed to store 1 millions of employee information. The availabile columns are:
> **- EmployeeID:** Integers incrementing by 1 unit for each employee. This is the primary key for this dataset. 
> **- EmployeeName:** Theoretical name for employees starting with Employee_ and taking incrementally increasing integer suffixes. 
> **- Salary:** Assigned theoretical salary information for employees to test aggregation functions like sum, average, and etc.
> **- DepartmentID:** Randomly assigned integer values representing the id of departments. Ranging from 1 to 5. This field is generated to join two tables. 

2. Departments Data: This dataset designed to store the deparment information from 1 to 5 representing 'HR', 'Finance', 'IT', 'Marketing' and 'Operations'. The available columns are:
> **- DepartmentID:** Department ID ranging from 1 to 5. Primary Key of this table and unique to each department. 
> **- DepartmentName:** Name of the department from the list of ['HR', 'Finance', 'IT', 'Marketing', 'Operations']. 

