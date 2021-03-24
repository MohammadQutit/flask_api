#!/bin/bash

# prepend application environment variables to crontab
env | cat - /opt/sourceCode/c > /etc/cron.d/c
# enable crond service
/usr/sbin/crond
# start crontab
crontab /etc/cron.d/c
#start the flask sevice
/opt/sourceCode/sample.sh