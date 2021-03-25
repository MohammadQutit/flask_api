# flask_api

Flask API to monitor and provide CPU, Memory and Disk statistics.
* [dokcer-hub image](https://hub.docker.com/r/mohammadqutit/flask_api)


## Getting Started

To start a container from this image

$ docker run --rm  --env host=mysql-server-ip --env user=user of the database --env  port=port-number-mysql-server --env password=password-for-database-user --env database=name-of-database -p 5000:5000  flask_api:v1

The app soucre code will be in /opt/sourceCode

### Prerequisities


In order to run this container you'll need docker installed.

Also you need to run mysql container from mysql image
* [mysql](https://hub.docker.com/_/mysql)



#### Environment Variables

* `host` - mysql server ip to connect the service to
* `user` - The name of the user used to connect to the database.
* `password` - Password set to the user to connect to the database.
* `port`: port number used by the mysql server
* `database`: Database name that the application will create to save the statistics.




## Built With

* Python3
* Flask
* mysql.connector

