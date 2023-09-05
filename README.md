# Benchmarking Data Processing Frameworks: Pandas, Polars, and Spark
In today's data-driven world, efficient data processing is paramount for organizations to gain actionable insights and make informed decisions. To shed light on the capabilities of three prominent data processing frameworks, namely Pandas, Polars, and Spark, we embark on a comprehensive benchmarking journey. This comparative study aims to assess the speed and performance of these frameworks across essential data manipulation tasks, including data reading, filtering, writing, and performing aggregation calculations. By pitting these tools against each other, we hope to provide valuable insights to data professionals and organizations seeking the most suitable data processing solution for their specific needs.

## Requirements
1. In the repository, I used a docker container specifically designed for PySpark to avoid environment configurations on my local computer. Therefore, before using this repository:
- Please install Docker Desktop app using [Docker Website](https://www.docker.com/products/docker-desktop/)
- Run the Docker Desktop app
- In your terminal run `docker compose up --build` command to start the container. While building the container, all the packages listed in `requirements.txt` file will be installed. 
- Once the container is built, proceed to the link (link also contains the token) shown in the terminal part to start using Jupyterlab environment. 

2. In order to store my visuals in [Plotly Chart Studio](https://chart-studio.plotly.com/feed/#/), I used the Plotly API. Please visit the [link](https://plotly.com/python/getting-started-with-chart-studio/#:~:text=Your%20API%20key%20for%20account,your%20Chart%20Studio%20Enterprise%20server.) for details. In order to use the tokens and API keys I used a config.ini file which is not included in this repository. If you do not want to use Plotly Chart Studio to save your visuals, just simply comment the related codes and use the notebooks without those codes. Otherwise, You need to create a config.ini file in the root directory like:

```
[plotly]

user = your_username
api_key = your_api_key
api_token = your_api_token
```
 
## Datasets
Employees Data: This dataset designed to store different number of employee information. The availabile columns are:
> **- EmployeeID:** Integers incrementing by 1 unit for each employee. This is the primary key for this dataset. 
> **- EmployeeName:** Theoretical name for employees starting with Employee_ and taking incrementally increasing integer suffixes. 
> **- Salary:** Assigned theoretical salary information for employees to test aggregation functions like sum, average, and etc.
> **- DepartmentID:** Randomly assigned integer values representing the id of departments. Ranging from 1 to 5. 

*Please refer to `scripts\functions.py` for the details of synthetic data generation. 

## Functions
All the tasks (reading, writing, filtering, writing) were performend with functions defined in `scripts\functions.py` file to keep notebook clean and readble. You can refer to the said file for further details. 