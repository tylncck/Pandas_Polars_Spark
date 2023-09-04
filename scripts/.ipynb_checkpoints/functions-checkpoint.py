#First the required libraries
import numpy as np
import pandas as pd
import time
import polars as pl
from pyspark.sql import SparkSession

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

    departments_df = pd.DataFrame({
        'DepartmentID': np.arange(1, 6),
        'DepartmentName': ['HR', 'Finance', 'IT', 'Marketing', 'Operations']})

    employees_df.to_csv('../data/employees.csv', index = False)
    departments_df.to_csv('../data/departments.csv', index = False)
    
    return employees_df, departments_df


# Define a function to measure CPU time for reading CSV
def measure_read_csv_time(package_name, csv_file_path):
        
    if package_name == "Pandas":
        start_time = time.process_time()
        pd.read_csv(csv_file_path)
        end_time = time.process_time()
    elif package_name == "Polars":
        start_time = time.process_time()
        pl.read_csv(csv_file_path)
        end_time = time.process_time()
    elif package_name == "PySpark":
        spark = SparkSession.builder.appName("CSVReader").getOrCreate()
        start_time = time.process_time()
        spark.read.csv(csv_file_path, header=True, inferSchema=True)
        end_time = time.process_time()
        spark.stop()
    else:
        raise ValueError("Invalid package name")

    elapsed_time = end_time - start_time
    
    return package_name, elapsed_time