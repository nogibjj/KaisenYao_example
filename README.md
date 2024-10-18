# KaisenYao_example
[![CI](https://github.com/nogibjj/KaisenYao_example/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/KaisenYao_example/actions/workflows/cicd.yml)

## File Structure
```
KaisenYao_example/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/cicd.yml
├── .gitignore
├── data/
│   └── US_births.csv
├── Dockerfile
├── LICENSE
├── main.py
├── Makefile
├── mylib/
│   ├── __init__.py
│   ├── extract.py
│   ├── query.py
│   └── transform_load.py
├── README.md
├── requirements.txt
├── setup.sh
├── test_main.py
└── setup.py
```

## Purpose of Project
The goal of this project is to create an ETL-Query pipeline utilizing Databricks and create an executable by packaging the project. This pipeline involves tasks such as extracting data from a URL, cleaning and transforming the data, then loading it into Databricks SQL Warehouse. Once the data is in place, we'll be able to run complex queries that may involve tasks like joining tables, aggregating data, and sorting results.

## Preparation
1. Open Codespaces or clone the repository locally
2. Wait for the container to be built and virtual environment to be activated with requirements.txt installed
3. Build the packaged project by running `make setup_package`
4. Extract: run `make extract`
5. Transform and load: run `make transform_load`
6. Query: run `make query` or alternatively write your own query using `python main.py query "<insert query>"`

## Complex Query
Here's the complex query used in this project:

```sql
WITH monthly_avg AS (
    SELECT 
        year,
        month,
        AVG(births) AS avg_births_per_month
    FROM 
        ids706_data_engineering.default.kaisenyao_example
    GROUP BY 
        year, month
)
SELECT 
    e.year,
    e.month,
    e.date_of_month,
    CASE 
        WHEN e.day_of_week = 1 THEN 'Sunday'
        WHEN e.day_of_week = 2 THEN 'Monday'
        WHEN e.day_of_week = 3 THEN 'Tuesday'
        WHEN e.day_of_week = 4 THEN 'Wednesday'
        WHEN e.day_of_week = 5 THEN 'Thursday'
        WHEN e.day_of_week = 6 THEN 'Friday'
        WHEN e.day_of_week = 7 THEN 'Saturday'
    END AS day_name,
    e.births,
    m.avg_births_per_month
FROM 
    ids706_data_engineering.default.kaisenyao_example e
JOIN
    monthly_avg m ON e.year = m.year AND e.month = m.month
ORDER BY 
    e.year DESC, e.month DESC, e.date_of_month DESC
LIMIT 20;
```

### Query Explanation:
- It uses a Common Table Expression (CTE) to calculate the average births per month.
- Joins the main table with the CTE to include the monthly average.
- Converts the numeric day of the week to a day name.
- Orders the results by year, month, and date in descending order.
- Limits the output to 20 rows.

This query demonstrates sorting, joining, and aggregation, providing insights into birth data trends.

### Sample Output:
Here's an example of the query output:

```
Row(year=2014, month=12, date_of_month=31, day_name='Tuesday', births=11990, avg_births_per_month=10958.90322580645)
Row(year=2014, month=12, date_of_month=30, day_name='Monday', births=13634, avg_births_per_month=10958.90322580645)
Row(year=2014, month=12, date_of_month=29, day_name='Sunday', births=12811, avg_births_per_month=10958.90322580645)
Row(year=2014, month=12, date_of_month=28, day_name='Saturday', births=7724, avg_births_per_month=10958.90322580645)
Row(year=2014, month=12, date_of_month=27, day_name='Friday', births=8656, avg_births_per_month=10958.90322580645)
...
```

## Check Format and Test Errors 
1. Format code: `make format`
2. Lint code: `make lint`
3. Test code: `make test`

## Simple Visualization of Process
![ETLQ](adflow.svg)

## Reflection Questions
1. What challenges did you face when extracting, transforming, and loading the data into Databricks? How did you overcome them?
2. What insights or new knowledge did you gain from querying the Databricks database?
3. How can Databricks and SQL help make data analysis more efficient? What are the limitations?
4. What AI assistant did you use and how did it compare to others you've tried? What are its strengths and weaknesses?
5. If you could enhance this lab, what would you add or change? What other data would be interesting to load and query?

## Challenge Exercises
- Add more transformations to the data before loading it into Databricks
- Write a query to find correlated fields in the data
- Create a second table in the Databricks database and write a join query
- Build a simple Flask web app that runs queries on demand
- Containerize the application using Docker

## References 
1. [Databricks SQL Documentation](https://docs.databricks.com/sql/index.html)
2. [Databricks SQL Connector for Python](https://docs.databricks.com/dev-tools/python-sql-connector.html)
3. [FiveThirtyEight Datasets](https://data.fivethirtyeight.com/)