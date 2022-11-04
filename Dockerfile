FROM python:3.10


COPY requirements.txt /var/api/

RUN pip install -r /var/api/requirements.txt

COPY . /var/api/app

WORKDIR /var/api/app

ENV SCRIPT_NAME=/api

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "600", "app:app"]
