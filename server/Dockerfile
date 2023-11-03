FROM python:3.8-slim

WORKDIR /app

COPY *requirements.txt /app/

RUN apt-get update && apt-get install git -y &&\
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app
RUN pip install -e .

EXPOSE 8000
ENTRYPOINT ["./entrypoint.sh"]
