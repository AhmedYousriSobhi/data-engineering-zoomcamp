FROM python:3.9.1

RUN pip install pandas

# Specify working directory
# Like cd app
WORKDIR /app

# Source -> Destination
COPY pipeline.py pipeline.py

# Specify Entrypoint when the docker is run.
ENTRYPOINT [ "bash" ]