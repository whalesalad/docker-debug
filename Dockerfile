FROM python:2.7.10

EXPOSE 8080 8080

WORKDIR /app

ADD . /app

ENTRYPOINT ["python", "/app/app.py"]
