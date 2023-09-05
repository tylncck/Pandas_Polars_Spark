# Benchmarking Data Processing Frameworks: Pandas, Polars, and Spark

In today's data-driven world, efficient data processing is paramount for organizations to gain actionable insights and make informed decisions. To shed light on the capabilities of three prominent data processing frameworks, namely Pandas, Polars, and Spark, we embarked on a comprehensive benchmarking journey. This comparative study aimed to assess the speed and performance of these frameworks across essential data manipulation tasks, including data reading, filtering, writing, and performing aggregation calculations. By pitting these tools against each other, we aimed to provide valuable insights to data professionals and organizations seeking the most suitable data processing solution for their specific needs.

## Requirements

1. To run the code in this repository, you need to have Docker Desktop installed. Please follow these steps:

   - Install Docker Desktop from the [Docker website](https://www.docker.com/products/docker-desktop/).
   - Run the Docker Desktop app.
   - In your terminal, run the `docker compose up --build` command to start the container. This command will build the container and install all the packages listed in the `requirements.txt` file.
   - Once the container is built, you can proceed to the link provided in the terminal to start using the JupyterLab environment.

2. To store visualizations in [Plotly Chart Studio](https://chart-studio.plotly.com/feed/#/), an API key is required. Please visit the [Plotly documentation](https://plotly.com/python/getting-started-with-chart-studio/#:~:text=Your%20API%20key%20for%20account,your%20Chart%20Studio%20Enterprise%20server) for details on obtaining an API key. You can store your API key and other necessary information in a `config.ini` file in the root directory as follows:

```
[plotly]
user = your_username
api_key = your_api_key
api_token = your_api_token
```

If you do not wish to use Plotly Chart Studio, you can simply comment out the related code sections in the notebooks.

## Datasets

This dataset was designed to store different numbers of employee information. It includes the following columns:

- **EmployeeID:** Integer values incrementing by 1 for each employee, serving as the primary key for this dataset.

- **EmployeeName:** Theoretical employee names in the format "Employee_X," where X is an incrementally increasing integer suffix.

- **Salary:** Theoretical salary information assigned to employees, used for testing aggregation functions like sum and average.

- **DepartmentID:** Randomly assigned integer values representing department IDs, ranging from 1 to 5.

Please refer to the `scripts\functions.py` file for details on how synthetic data was generated.

## Functions

All tasks, including reading, writing, filtering, and aggregation, were performed using functions defined in the `scripts\functions.py` file. This approach was adopted to keep the notebooks clean and readable. You can refer to the mentioned file for further details.

## Performance Summary

**Reading .csv Files:**

- Pandas and Polars perform comparably for datasets up to 250,000 rows, with Polars surpassing Pandas for larger datasets.
- PySpark exhibits the slowest performance initially but outperforms Pandas for larger datasets.

**Filtering Task:**

- Pandas and Polars demonstrate consistent and robust performance regardless of dataset size.
- PySpark's performance deteriorates as the dataset size increases.

**Aggregation Task:**

- Pandas' performance steadily decreases with an increasing number of rows.
- Up to 250,000 rows, Pandas outperforms other packages in aggregation.
- Polars consistently offers the best aggregation performance.
- PySpark becomes faster than Pandas after 500,000 rows.

**Writing Task:**

- Polars excels in writing dataframes to .csv files, with consistent performance regardless of dataset size.
- Pandas is the second-best option but exhibits performance degradation with increasing row counts.
- PySpark lags behind, showing the slowest performance, particularly for larger datasets.

**Conclusion:**

In this comprehensive performance evaluation of Pandas, Polars, and PySpark across various data processing tasks, several key findings emerge:

- Polars is the preferred choice for handling large datasets across all tasks.
- Pandas remains suitable for smaller datasets but exhibits performance degradation with increasing rows.
- PySpark, while versatile, may not be the optimal choice for tasks involving substantial data volumes due to its performance limitations.
