import os

import pyodbc
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DATA_DIR, exist_ok=True)


def read_sql_dataframe(conn, query):
    """Execute a SQL query and return a DataFrame.

    This supports multi-statement scripts (for example, DDL + cursor loops + final SELECT),
    which pandas.read_sql() may reject with the HY007 error for SQL Server.
    """
    cursor = conn.cursor()
    cursor.execute(query)

    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()

    return pd.DataFrame.from_records(rows, columns=columns)


# ==========================================
# CONNECT TO SQL SERVER
# ==========================================

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    r"SERVER=DESKTOP-5UF6M9T\SRV_01;"
    "DATABASE=TWO16;"
    "UID=sa;"
    "PWD=Gen31**13;"
)

# =======================**=================
# 1. DATABASES
# OUTPUT: databases.json
# ========**================================
sql_databases = """
SELECT
    databases.name AS database_name,
    physical_database_name,
    create_date
FROM sys.databases
"""

df_databases = pd.read_sql(sql_databases, conn)

df_databases.to_json(
    os.path.join(DATA_DIR, "databases.json"),
    orient="records",
    date_format="iso",
    indent=4
)

print(f"databases.json exported ({len(df_databases)} records)")
# ==============================**==========
# 2. TABLES
# OUTPUT: **bles.json
# =====================**===================

sql_tables ="""
SELECT
    DB_NAME() AS DATABASE_NAME,
    S.NAME AS SCHEMA_NAME,
    T.NAME AS TABLE_NAME
FROM SYS.SCHEMAS S
INNER JOIN SYS.TABLES T
  ON S.SCHEMA_ID = T.SCHEMA_ID
WHERE T.IS_MS_SHIPPED = 0
ORDER BY
    S.NAME,
    T.NAME
"""

df_tables = pd.read_sql(sql_tables, conn)

df_tables.to_json(
    os.path.join(DATA_DIR, "tables.json"),
    orient="records",
    indent=4
)

print(f"tables.json exported ({len(df_tables)} records)")


# ==========================================
# 3. VIEW DEPENDENCIES
# OUTPUT: view_dep.json
# ==========================================

sql_views = """
SELECT
    referencing_object.name AS [Source Object Name],
    referencing_object.type_desc AS [Source Object Type],
    referenced_schema_name AS [Referenced Schema],
    referenced_entity_name AS [Referenced Table Name]
FROM
    sys.sql_expression_dependencies AS dep
INNER JOIN
    sys.objects AS referencing_object
        ON dep.referencing_id = referencing_object.object_id
WHERE
    referencing_object.type IN ('V')
    AND dep.referenced_class = 1
ORDER BY
    [Source Object Type],
    [Source Object Name]
"""

df_views = pd.read_sql(sql_views, conn)

df_views.to_json(
    os.path.join(DATA_DIR, "view_dep.json"),
    orient="records",
    indent=4
)

print(f"view_dep.json exported ({len(df_views)} records)")

# ==========================================
# 4. VIEW 
# OUTPUT: views.json
# ==========================================

sql_vws = """
SELECT
  DB_NAME() AS DATABASE_NAME,
  S.NAME AS SCHEMA_NAME,
  V.NAME AS VIEW_NAME
FROM SYS.SCHEMAS S
INNER JOIN SYS.VIEWS V
  ON S.SCHEMA_ID = V.SCHEMA_ID
WHERE V.IS_MS_SHIPPED = 0
ORDER BY
  S.NAME,
  V.NAME;
"""

df_vws = pd.read_sql(sql_vws, conn)

df_vws.to_json(
    os.path.join(DATA_DIR, "views.json"),
    orient="records",
    indent=4
)

print(f"views.json exported ({len(df_vws)} records)")

# ==========================================
# 5. VIEW Definitions
# OUTPUT: views_definitions.json
# ==========================================

sql_vwdef = """
SELECT
    o.object_id,
    SCHEMA_NAME(o.schema_id) AS schema_name,
    o.name AS object_name,
    m.definition
FROM sys.objects o
JOIN sys.sql_modules m
    ON m.object_id = o.object_id
WHERE o.type = 'V' ;
"""

df_vwdef = pd.read_sql(sql_vwdef, conn)

df_vwdef.to_json(
    os.path.join(DATA_DIR, "views_definitions.json"),
    orient="records",
    indent=4
)

print(f"views_definitions.json exported ({len(df_vwdef)} records)")
# ==========================================
# 6. Columns
# OUTPUT: columns.json
# ==========================================

sql_columns = """
SELECT
db_name() AS database_name,
tables.name AS table_name,
columns.name AS column_name,
'Column' AS object_type
FROM sys.tables
INNER JOIN sys.columns
ON tables.object_id = columns.object_id
"""

df_columns = pd.read_sql(sql_columns, conn)

df_columns.to_json(
    os.path.join(DATA_DIR, "columns.json"),
    orient="records",
    indent=4
)

print(f"columns.json exported ({len(df_columns)} records)")
# ==========================================
# 7. VIEW dependencies - columns
# OUTPUT: view_dep_columns.json
# ==========================================

sql_vws = """
SET NOCOUNT ON;

IF OBJECT_ID('tempdb..#DEPENDENCIES') IS NOT NULL
    DROP TABLE #DEPENDENCIES;

CREATE TABLE #DEPENDENCIES
(
  SOURCE_OBJECT           SYSNAME NULL,
  SOURCE_TYPE             VARCHAR(60) NULL,
  REFERENCED_SCHEMA       SYSNAME NULL,
  REFERENCED_TABLE        SYSNAME NULL,
  REFERENCED_COLUMN       SYSNAME NULL,
  REFERENCED_OBJECT_TYPE  VARCHAR(60) NULL,
  IS_DIRECT_TABLE_COLUMN  BIT NULL,
  ERROR_MESSAGE           NVARCHAR(4000) NULL
);

DECLARE @OBJECT_NAME NVARCHAR(517);
DECLARE @SQL NVARCHAR(MAX);

DECLARE CUR CURSOR FAST_FORWARD FOR
SELECT
  QUOTENAME(SCHEMA_NAME(SCHEMA_ID))
  + '.'
  + QUOTENAME(NAME)
FROM SYS.VIEWS;

OPEN CUR;

FETCH NEXT FROM CUR INTO @OBJECT_NAME;

WHILE @@FETCH_STATUS = 0
BEGIN

  BEGIN TRY

    SET @SQL = N'

    INSERT INTO #DEPENDENCIES
    (
      SOURCE_OBJECT,
      SOURCE_TYPE,
      REFERENCED_SCHEMA,
      REFERENCED_TABLE,
      REFERENCED_COLUMN,
      REFERENCED_OBJECT_TYPE,
      IS_DIRECT_TABLE_COLUMN,
      ERROR_MESSAGE
    )
    SELECT
      ''' + @OBJECT_NAME + ''',
      O.TYPE_DESC,
      ISNULL(D.REFERENCED_SCHEMA_NAME,''UNKNOWN''),
      ISNULL(D.REFERENCED_ENTITY_NAME,''UNKNOWN''),
      D.REFERENCED_MINOR_NAME,
      COALESCE(RO.TYPE_DESC,''UNKNOWN''),
      CASE
        WHEN RO.TYPE = ''U'' THEN 1
        ELSE 0
      END,
      NULL
    FROM SYS.DM_SQL_REFERENCED_ENTITIES
    (
      ''' + @OBJECT_NAME + ''',
      ''OBJECT''
    ) D
    LEFT JOIN SYS.OBJECTS RO
      ON RO.OBJECT_ID =
      OBJECT_ID(
        QUOTENAME(D.REFERENCED_SCHEMA_NAME)
        + ''.''
        + QUOTENAME(D.REFERENCED_ENTITY_NAME)
      )
    CROSS JOIN
    (
      SELECT TYPE_DESC
      FROM SYS.OBJECTS
      WHERE OBJECT_ID = OBJECT_ID(''' + @OBJECT_NAME + ''')
    ) O;
    ';

    EXEC SYS.SP_EXECUTESQL @SQL;

  END TRY
  BEGIN CATCH

    INSERT INTO #DEPENDENCIES
    (
      SOURCE_OBJECT,
      SOURCE_TYPE,
      ERROR_MESSAGE
    )
    VALUES
    (
      @OBJECT_NAME,
      'VIEW',
      ERROR_MESSAGE()
    );

  END CATCH;

  FETCH NEXT FROM CUR INTO @OBJECT_NAME;

END

CLOSE CUR;
DEALLOCATE CUR;

SELECT *
FROM #DEPENDENCIES
ORDER BY
  SOURCE_OBJECT,
  REFERENCED_TABLE,
  REFERENCED_COLUMN;
"""

df_vws_col = read_sql_dataframe(conn, sql_vws)

df_vws_col.to_json(
    os.path.join(DATA_DIR, "view_dep_columns.json"),
    orient="records",
    indent=4
)

print(f"view_dep_columns.json exported ({len(df_vws_col)} records)")


# ==========================================
# CLOSE CONNECTION
# ==========================================

conn.close()

print("Export Complete")