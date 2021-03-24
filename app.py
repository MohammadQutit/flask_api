from flask import Flask,request,jsonify
import logging
from functions import cpu_stat,disk_stat,memory_stat,disk_one,memory_one,cpu_one
app=Flask(__name__)
import schema

def some(func):
    """wrapper function to log the api call and functions used in it"""
    def wrapper(* args,** kwargs):
        logging.basicConfig(filename='error.log',level=logging.DEBUG)
        logging.info(request.url + " : " + str(request.remote_addr)+" using function "+func.__name__ )
        return func(* args,** kwargs)

    wrapper.__name__ = func.__name__    
    return wrapper


@app.route("/")
@some
def home():
    return "<h1>Monitoring</h1>"

    
   

@app.route("/memory")
@some
def memory():
    result=memory_stat()
    return result

@app.route("/memory/now")
@some
def memory_now():
    result=memory_one()
    return result


@app.route("/cpu")
@some
def cpu():
    result=cpu_stat()
    return jsonify(result)
        
@app.route("/cpu/now")
@some
def cpu_now():
    result=cpu_one()
    return result

@app.route("/disk")
@some
def disk():
    result=disk_stat()
    return result



@app.route("/disk/now")
@some
def disk_now():
    result=disk_one()
    return result

if __name__=="__main__":
    app.run(host="0.0.0.0")

