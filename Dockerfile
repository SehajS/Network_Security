FROM python:3.12-slim-buster

WORKDIR /app

COPY . /app

RUN apt update -y

RUN apt-get update && pip install -r rqeuirements.txt

CMD ["python3", "app.py"]