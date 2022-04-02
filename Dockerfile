FROM python:3.9-slim

COPY . .
RUN apt-get update -y && apt-get install make gcc i2c-tools -y
RUN pip install -r requirements.txt

ENTRYPOINT [ "entrypoint.sh" ]