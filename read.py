import os
import mysql.connector

user = os.environ["user"]
host = os.environ["host"]
port = os.environ["port"]
password = os.environ["password"]
database = os.environ["database"]


def mem():
    result = tuple(
        map(int, os.popen('free -t -m').readlines()[-1].split()[1:]))
    try:
        connection = mysql.connector.connect(
            user=user,
            host=host,
            port=port,
            password=password,
            database=database
        )
        cursor = connection.cursor()
        cursor.execute(
            "insert into memory (total,used,free) values(%s,%s,%s)", result)
        connection.commit()
        connection.close()
        return True
    except Exception as e:
        print(str(e))
        return str(e)


def disk():
    result = tuple(
        map(int, os.popen("df --total").readlines()[-1].split()[1:4]))
    print(result)
    try:
        connection = mysql.connector.connect(
            user=user,
            host=host,
            port=port,
            password=password,
            database=database
        )
        cursor = connection.cursor()
        cursor.execute(
            "insert into disk (total,used,free) values(%s,%s,%s)", result)
        connection.commit()
        connection.close()
        return True
    except Exception as e:
        return str(e)


def cpu():
    result = tuple(
        map(float, os.popen("mpstat").readlines()[-1].split()[3:13]))
    print(result)
    sum_used = 0
    for i in range(0, 9):
        sum_used += result[i]

    x = (sum_used,result[-1])

    try:
        connection = mysql.connector.connect(
            user=user,
            host=host,
            port=port,
            password=password,
            database=database
        )
        cursor = connection.cursor()
        cursor.execute("insert into cpu (used,idle) values(%s,%s)", x)
        connection.commit()
        connection.close()
        return True
    except Exception as e:
        return str(e)


disk()
mem()
cpu()
