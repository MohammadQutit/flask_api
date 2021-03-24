import mysql.connector
import json
import datetime
import os

# read the environmemt variables and store them
user= os.environ["user"]
host= os.environ["host"]
port= os.environ["port"]
password=os.environ["password"]
database=os.environ["database"]

def create_connection(user,host,port,password,database):
    """return connection object on the specified database"""
    try:
        connection = mysql.connector.connect(
                    user=user,
                    host=host,
                    port=port,
                    password=password,
                    database=database
                    )
        return connection
    except Exception as error:
        raise Exception(str(error))


# def myconverter(o):
#     if isinstance(o, datetime.datetime):
#         return o.__str__()

def cpu_stat():
    """raead the cpu statistics and append the to database"""
    try:
        connection=create_connection(user,host,port,password,database)
        cursor = connection.cursor()
        query="select * from cpu order by time desc limit 24;"
        cursor.execute(query)
        result=cursor.fetchall()
        j={"data":[]}
        final=tuple(result)
        for i in final:
            x={"time":i[0],"used":i[1],"free":i[2]}
            j["data"].append(x)
        connection.close()
        return j
    except Exception as error:
        raise Exception(str(error))

def cpu_one():
    """return the cpu statistics now"""
    result = tuple(
        map(float, os.popen("mpstat").readlines()[-1].split()[3:13]))
    print(result)
    sum_used = 0
    for i in range(0, 9):
        sum_used += result[i]

    return json.dumps({"data":{"idle":result[-1],"used":sum_used}})



def memory_stat():
    """raead the memory statistics and append the to database"""
    try:
        connection=create_connection(user,host,port,password,database)
        cursor = connection.cursor()
        query="select * from memory order by time desc limit 24;"
        cursor.execute(query)
        result=cursor.fetchall()
        final=tuple(result)
        j={"data":[]}
        
        for i in final:
            x={"time":i[0],"total":i[1],"used":i[2],"free":i[3]}
            j["data"].append(x)
        connection.close()
        return j
    except Exception as error:
        raise Exception(str(error))


def memory_one():
    """return the memory statistics now"""
    tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
    return json.dumps({"data":{"total":tot_m,"free":free_m,"used":used_m}})



def disk_stat():
    """raead the disk statistics and append the to database"""
    try:
        connection=create_connection(user,host,port,password,database)
        cursor = connection.cursor()
        query="select * from disk order by time desc limit 24;"
        cursor.execute(query)
        result=cursor.fetchall()
        final=tuple(result)
        connection.close()
        j={"data":[]}
        
        for i in final:
            x={"time":i[0],"total":i[1],"used":i[2],"free":i[3]}
            j["data"].append(x)
        connection.close()
        return j
    except Exception as error:
        raise Exception(str(error))

def disk_one():
    """return the disk statistics now"""
    tot_d,used_t,free_t=map(int,os.popen("df --total").readlines()[-1].split()[1:4])
    return json.dumps({"data":{"total":tot_d,"free":free_t,"used":used_t}})

