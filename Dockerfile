FROM python:3.10


COPY requirements.txt /var/api/

RUN pip install -r /var/api/requirements.txt

COPY . /var/api/app

WORKDIR /var/api/app

ARG MONGO_USERNAME
ARG MONGO_PASSWORD

ENV MONGO_USERNAME=$MONGO_USERNAME
ENV MONGO_PASSWORD=$MONGO_PASSWORD

CMD ["gunicorn", "--workers", "4", "--threads", "3", "--env", "SCRIPT_NAME=/api", "--bind", "0.0.0.0:5000", "--timeout", "60", "app:app"]
