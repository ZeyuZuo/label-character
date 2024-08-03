import pandas as pd
from sqlalchemy import create_engine

# 连接数据库
engine = create_engine('mysql+pymysql://root:123456@localhost/ry')

# 获取所有表名
tables = pd.read_sql("SHOW TABLES", engine)

# 遍历所有表
for table in tables.values.flatten():
    # 获取所有列名
    columns = pd.read_sql(f"SHOW COLUMNS FROM {table}", engine)
    for column in columns['Field']:
        try:
            # 查找特定数据
            result = pd.read_sql(f"SELECT * FROM {table} WHERE {column} LIKE '%分配角色%'", engine)
            if not result.empty:
                print(f"Found in table {table}, column {column}")
        except Exception as e:
            pass
