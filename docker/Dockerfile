#FROM tensorflow/tensorflow:2.9.1-gpu-jupyter # started with existing container on disk
#FROM python:3.8.16-slim-bullseye  # wanted to shrink container size, further tf is not needed, but numpy indexing is erroring out, likely need to figure out right version for numpy... thus wen back to tf-cpu-only container
FROM tensorflow/tensorflow:2.9.1

RUN apt-get update && \
    apt-get install ffmpeg libsm6 libxext6  -y

RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

