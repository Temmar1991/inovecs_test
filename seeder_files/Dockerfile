FROM python:3
MAINTAINER Artem Melnyk
RUN useradd python-app && mkdir -p /opt/web-app && chown -R python-app:root /opt/web-app && \ 
    apt-get update && \
    apt-get install -y libmariadb-dev

WORKDIR /opt/web-app

COPY app-files/ ./

RUN pip3 install --no-cache-dir -r requirements.txt

USER python-app
CMD ["python3","-u", "seeder.py"]



