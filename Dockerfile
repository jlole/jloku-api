FROM python:3.10


COPY requirements.txt /var/api/

RUN pip install -r /var/api/requirements.txt

COPY . /var/api/app

WORKDIR /var/api/app


RUN --mount=type=secret,id=MONGO_USERNAME \
  --mount=type=secret,id=MONGO_PASSWORD \
   export MONGO_USERNAME=$(cat /run/secrets/MONGO_USERNAME) && \
   export MONGO_PASSWORD=$(cat /run/secrets/MONGO_PASSWORD)


CMD ["gunicorn", "--env", "SCRIPT_NAME=/api", "--bind", "0.0.0.0:5000", "--timeout", "600", "app:app"]
