FROM jupyter/pyspark-notebook

USER root

COPY /requirements.txt /

RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libffi-dev

RUN pip install --upgrade pip setuptools wheel

RUN apt-get install build-essential swig
# Install packages from requirements.txt file
RUN pip install -r /requirements.txt