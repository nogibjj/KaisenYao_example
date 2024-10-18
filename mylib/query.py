"""Query the database"""

import os
from dotenv import load_dotenv
from databricks import sql

complex_query = """SELECT
    year,
    month,
    date_of_month,
    day_of_week,
    births
FROM ids706_data_engineering.default.kaisenyao_example
ORDER BY year DESC, month DESC, date_of_month DESC
LIMIT 10;
"""


def query():
    """Query the database for the top 10 rows of the table"""
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

            cursor.close()
            connection.close()

    return "query successful"


if __name__ == "__main__":
    query()
