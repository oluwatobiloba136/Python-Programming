import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    r"SERVER=DESKTOP-5UF6M9T\SRV_01;"
    "DATABASE=TWO16;"
    "UID=sa;"
    "PWD=Gen31**13;"
    "Trusted_Connection=yes;"
)

sql = """
select databases.name AS database_name,
physical_database_name
from sys.databases
"""

df = pd.read_sql(sql, conn)

df.to_json(
    "customers.json",
    orient="records"
)

conn.close()

print("Export Complete")