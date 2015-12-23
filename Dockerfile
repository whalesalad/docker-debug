FROM gliderlabs/alpine:3.2

RUN apk --update add python

EXPOSE 8080 8080

WORKDIR /app

ADD . /app

ENTRYPOINT ["python", "/app/app.py"]
