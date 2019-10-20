FROM python:3
MAINTAINER Artem Melnyk
RUN useradd python-app && mkdir -p /opt/web-app && chown -R python-app:root /opt/web-app

USER python-app

WORKDIR /opt/web-app

COPY app-files/ ./

USER root
RUN pip3 install --no-cache-dir -r requirements.txt

USER python-app
CMD ["python3", "-u", "client.py"]



