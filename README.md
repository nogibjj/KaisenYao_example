[![CI](https://github.com/nogibjj/KaisenYao_example/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/KaisenYao_example/actions/workflows/cicd.yml)
## KaisenYao_example
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
The goal of this project is to create an ETL-Query pipeline utilizing databricks and create an executable by packaging the project. This pipeline involves tasks such as extracting data from a URL, cleaning and transforming the data, then loading it into databricks Warehouse. Once the data is in place, we'll be able to run complex queries that may involve tasks like joining tables, aggregating data, and sorting results.

## Preparation
1. Open Codespaces or clone the repository locally
2. Wait for the container to be built and virtual environment to be activated with requirements.txt installed
3. Build the packaged project by running `make setup_package`
4. Extract: run `make extract`
5. Transform and load: run `make transform_load`
6. Query: run `make query` or alternatively write your own query using `python main.py query "<insert query>"`

## Complex Query
Here's the complex query used in this project, limited to the first 10 results:

```sql
SELECT
    year,
    month,
    date_of_month,
    day_of_week,
    births
FROM ids706_data_engineering.default.kaisenyao_example
ORDER BY year DESC, month DESC, date_of_month DESC
LIMIT 10;
```

This query retrieves all columns from the `kaisenyao_example` table in the `ids706_data_engineering.default` schema. It orders the results by year, month, and date of month, all in descending order, and then limits the output to the first 10 rows.

### Query Explanation:
- `SELECT`: Specifies the columns we want to retrieve (in this case, all columns).
- `FROM`: Indicates the table we're querying from.
- `ORDER BY`: Sorts the results based on specified columns.
  - `year DESC`: Sorts by year in descending order (most recent years first).
  - `month DESC`: For each year, sorts by month in descending order.
  - `date_of_month DESC`: For each month, sorts by date in descending order.
- `LIMIT 10`: Restricts the output to only the first 10 rows of the result set.

This query is useful for quickly viewing the most recent birth data in the dataset. It provides a snapshot of the latest entries, which can be helpful for verifying data freshness or getting a quick overview of recent trends.

### Sample Output:
Here's an example of what the output might look like:

| year | month | date_of_month | day_of_week | births |
|------|-------|---------------|-------------|--------|
| 2014 | 12    | 31            | 3           | 11990  |
| 2014 | 12    | 30            | 2           | 13634  |
| 2014 | 12    | 29            | 1           | 12811  |
| 2014 | 12    | 28            | 7           | 7724   |
| 2014 | 12    | 27            | 6           | 8656   |
| 2014 | 12    | 26            | 5           | 10386  |
| 2014 | 12    | 25            | 4           | 6749   |
| 2014 | 12    | 24            | 3           | 9308   |
| 2014 | 12    | 23            | 2           | 12604  |
| 2014 | 12    | 22            | 1           | 12799  |


## Check Format and Test Errors 
1. Format code: `make format`
2. Lint code: `make lint`
3. Test code: `make test`

## Simple Visualization of Process
![ETLQ](adflow.svg)

## Reflection Questions
1. What challenges did you face when extracting, transforming, and loading the data? How did you overcome them?
2. What insights or new knowledge did you gain from querying the Databricks database?
3. How can databricks and SQL help make data analysis more efficient? What are the limitations?
4. What AI assistant did you use and how did it compare to others you've tried? What are its strengths and weaknesses?
5. If you could enhance this lab, what would you add or change? What other data would be interesting to load and query?

## Challenge Exercises
- Add more transformations to the data before loading it into databricks.
- Write a query to find correlated fields in the data
- Create a second table in the databricks database and write a join query
- Build a simple Flask web app that runs queries on demand
- Containerize the application using Docker

## References 
1. [SQLite Documentation](https://www.sqlite.org/docs.html)
2. [Python SQLite3 Module](https://docs.python.org/3/library/sqlite3.html)
3. [FiveThirtyEight Datasets](https://data.fivethirtyeight.com/)