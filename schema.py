import mysql.connector
import os
host=os.environ["host"]
user=os.environ["user"]
port=os.environ["port"]
password=os.environ["password"]
database=os.environ["database"]
# This module used to create the initial database schema if it doesn't exists
def create_DB():
    """Create The database"""
    conn = mysql.connector.connect(
        host=host,
        user=user,
        port=port,
        password=password
    )
    cursor=conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS "+database)
    conn.commit()
    conn.close()
    
def create_tables():
    "Create three tables cpu, disk and memory "
    conn = mysql.connector.connect(
        host=os.environ["host"],
        user=os.environ["user"],
        port=os.environ["port"],
        password=os.environ["password"],
        database=os.environ["database"]
    )
    cursor=conn.cursor()
    cursor.execute("CREATE table IF NOT EXISTS cpu(time timestamp DEFAULT CURRENT_TIMESTAMP,idle float, used float)")
    cursor.execute("CREATE table IF NOT EXISTS disk(time timestamp DEFAULT CURRENT_TIMESTAMP,total int,used int, free int)")
    cursor.execute("CREATE table IF NOT EXISTS memory(time timestamp DEFAULT CURRENT_TIMESTAMP,total int,used int, free int)")
    conn.commit()
    conn.close()

create_DB()
create_tables()
