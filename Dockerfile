
FROM debian:oldstable-20240904
FROM python:3.12

WORKDIR /usr/project

COPY requirements.txt /usr/project/requirements.txt
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY src/app.py /usr/project/src/app.py
COPY src/config.py /usr/project/src/config.py
COPY src/depends.py /usr/project/src/depends.py

COPY src/repositories /usr/project/src/repositories
COPY src/schemes /usr/project/src/schemes
COPY src/routers /usr/project/src/routers

COPY service.py /usr/project/service.py

CMD ["apt-get", "update"]
CMD ["apt-get", "install", "upgrade"]

