"""Query the database"""

import os
from dotenv import load_dotenv
from databricks import sql

complex_query = """
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
"""


def query():
    """Query the database for birth statistics"""
    load_dotenv()
    with sql.connect(
        server_hostname=os.getenv("SERVER_HOSTNAME"),
        http_path=os.getenv("HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_KEY"),
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(complex_query)
            result = cursor.fetchall()
            for row in result:
                print(row)
    return "query successful"


if __name__ == "__main__":
    query()
