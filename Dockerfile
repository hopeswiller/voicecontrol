FROM python:3.8.11-buster AS build-stage

LABEL maintainer="<davidba941@gmail.com> <https://github.com/hopeswiller/voicecontrol>"

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
ARG USER=hopeswiller

RUN apt-get update && \
    apt-get install libasound-dev libportaudio2 \
    libportaudiocpp0 portaudio19-dev python-pyaudio -y
    
RUN apt-get install libespeak-dev -y

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./src .

RUN addgroup --gid 1000 --system ${USER} && \
    adduser --uid 1000 --system ${USER} --gid 1000 && \
    addgroup ${USER} audio 

RUN chmod -R 777 /app/ && \
    chown -Rf ${USER}:${USER} /app/

USER ${USER} 
CMD python app.py

######################################################################