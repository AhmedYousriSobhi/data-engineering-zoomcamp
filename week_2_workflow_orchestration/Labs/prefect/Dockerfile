FROM python:3.9

COPY requirements.txt requirements.txt

RUN apt-get install wget
RUN pip install -r requirements.txt
RUN pip install --upgrade uvicorn  daphne  asgi_lifespan

WORKDIR /app
COPY ingest_data.py ingest_data.py

ENTRYPOINT [ "python", "ingest_data.py" ]