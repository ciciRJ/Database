import pyodbc

def get_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=LAPTOP-789KN2BS;"  
        "DATABASE=JY;"             
        "Trusted_Connection=yes;"  # 使用Windows身份验证
    )
    return conn

