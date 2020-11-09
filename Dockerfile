FROM tiangolo/meinheld-gunicorn-flask:python3.8 AS base

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY openapi-specs/SAP/SAP.yaml /app/openapi-specs/SAP/

COPY ["main.py", "start.sh", "gunicorn_conf.py", "web", "/app/"]
RUN chmod +x start.sh

FROM base as testing
COPY ./requirements-dev.txt .
RUN pip install -r requirements-dev.txt
RUN pytest tests --junitxml=junit.xml 

FROM base
RUN rm -r /app/tests