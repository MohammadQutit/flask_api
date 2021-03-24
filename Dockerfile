FROM centos:7

RUN yum install -y python3
RUN yum install -y sysstat
RUN yum install -y cronie
RUN pip3 install flask
RUN pip3 install mysql-connector-python
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

COPY . /opt/sourceCode
Run chmod -v +x /opt/sourceCode/sample.sh
Run chmod -v +x /opt/sourceCode/read.py
Run chmod -v +x /opt/sourceCode/run.sh
ADD c /etc/cron.d/c
RUN chmod 0644 /etc/cron.d/c
RUN touch /var/log/cron.log

ENTRYPOINT ["/opt/sourceCode/run.sh"]

