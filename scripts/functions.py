#First the required libraries
import numpy as np
import pandas as pd
import time
import polars as pl
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def get_data(num_employees):
    np.random.seed(2019)
    num_employees = num_employees
    employee_ids = np.arange(1, num_employees + 1)
    employee_names = ['Employee' + str(i) for i in employee_ids]
    employee_salaries = np.random.randint(30000, 100000, num_employees)
    department_ids = np.random.randint(1, 6, num_employees)

    employees_df = pd.DataFrame({
        'EmployeeID': employee_ids,
        'EmployeeName': employee_names,
        'Salary': employee_salaries,
        'DepartmentID': department_ids
    })

    employees_df.to_csv('../data/employees.csv', index = False)
    
    return employees_df


# Define a function to measure CPU time for reading CSV
def measure_read_csv_time(package_name, csv_file_path):
        
    if package_name == 'Pandas':
        start_time = time.time()
        pd.read_csv(csv_file_path)
        end_time = time.time()
    elif package_name == 'Polars':
        start_time = time.time()
        pl.read_csv(csv_file_path)
        end_time = time.time()
    elif package_name == 'PySpark':
        spark = SparkSession.builder.appName('CSVReader').getOrCreate()
        start_time = time.time()
        spark.read.csv(csv_file_path, header=True, inferSchema=True)
        end_time = time.time()
        spark.stop()
    else:
        raise ValueError('Invalid package name')

    elapsed_time = end_time - start_time
    
    return package_name, elapsed_time

def measure_aggregation(package_name, csv_file_path):

    if package_name == 'Pandas':
        employees_df = pd.read_csv(csv_file_path)
        start_time = time.time()
        department_avg_salaries = employees_df.groupby('DepartmentID')['Salary'].mean().reset_index()
        end_time = time.time()
    elif package_name == 'Polars':
        employees_df = pl.read_csv(csv_file_path)
        start_time = time.time()
        department_avg_salaries = employees_df.groupby('DepartmentID').agg(pl.col('Salary').mean().alias('AvgSalary'))
        end_time = time.time()
    elif package_name == 'PySpark':
        spark = SparkSession.builder.appName('CSVReader').getOrCreate()
        employees_df = spark.read.csv(csv_file_path, header=True, inferSchema=True)
        start_time = time.time()
        department_avg_salaries = employees_df.groupBy('DepartmentID').agg({'Salary': 'avg'}).withColumnRenamed('avg(Salary)', 'AvgSalary')
        end_time = time.time()
        spark.stop()
    else:
        raise ValueError('Invalid package name')
    
    elapsed_time = end_time - start_time
    
    return package_name, elapsed_time

def measure_filtering(package_name, csv_file_path):

    if package_name == 'Pandas':
        employees_df = pd.read_csv(csv_file_path)
        start_time = time.time()
        average_salary = employees_df['Salary'].mean()
        filtered_df = employees_df[employees_df['Salary'] > average_salary]
        end_time = time.time()
    elif package_name == 'Polars':
        employees_df = pl.read_csv(csv_file_path)
        start_time = time.time()
        average_salary = employees_df['Salary'].mean()
        filtered_df = employees_df.filter(employees_df['Salary'] > average_salary)
        end_time = time.time()
    elif package_name == 'PySpark':
        spark = SparkSession.builder.appName('CSVReader').getOrCreate()
        employees_df = spark.read.csv(csv_file_path, header=True, inferSchema=True)
        start_time = time.time()
        average_salary = employees_df.agg({'Salary': 'avg'}).collect()[0][0]
        filtered_df = employees_df.filter(col('Salary') > average_salary)
        end_time = time.time()
        spark.stop()
    else:
        raise ValueError('Invalid package name')
    
    elapsed_time = end_time - start_time
    
    return package_name, elapsed_time


def measure_writing(package_name, csv_file_path):

    if package_name == 'Pandas':
        employees_df = pd.read_csv(csv_file_path)
        start_time = time.time()
        employees_df.to_csv('../data/pandas.csv')
        end_time = time.time()
    elif package_name == 'Polars':
        employees_df = pl.read_csv(csv_file_path)
        start_time = time.time()
        employees_df.write_csv('../data/polars.csv')
        end_time = time.time()
    elif package_name == 'PySpark':
        spark = SparkSession.builder.appName('CSVReader').getOrCreate()
        employees_df = spark.read.csv(csv_file_path, header=True, inferSchema=True)
        start_time = time.time()
        employees_df.write.format('csv').option('header', 'true').mode('overwrite').save('../data/pyspark.csv')
        end_time = time.time()
        spark.stop()
    else:
        raise ValueError('Invalid package name')
    
    elapsed_time = end_time - start_time
    
    return package_name, elapsed_time