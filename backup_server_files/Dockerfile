FROM python:3
MAINTAINER Artem Melnyk

RUN echo "deb http://repo.mysql.com/apt/ubuntu/ bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 8C718D3B5072E1F5
RUN useradd python-app && mkdir -p /opt/web-app && chown -R python-app:root /opt/web-app && \
    apt-get update && \
    apt-get install -y mysql-client

WORKDIR /opt/web-app

COPY app-files/ ./

RUN pip3 install --no-cache-dir -r requirements.txt

USER python-app
CMD ["python3","-u","backup_server.py"]



