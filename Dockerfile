FROM python:3.8.2-buster AS build-stage

LABEL maintainer="<davidba941@gmail.com> <https://github.com/hopeswiller/voicecontrol>"

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && \ 
    apt-get install -y portaudio19-dev python-all-dev python3-all-dev
    # libasound2 alsa-utils alsa-oss
    # alsa-utils alsa-lib 
    # alsa-firmware 
    # alsa-oss

# RUN apt-get clean && \
    # rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./src .

###############################################################

FROM python:3.8.2-buster

WORKDIR /app
ARG USER=hopeswiller

# RUN apt-get update && apt-get install -y portaudio19-dev

COPY --from=build-stage /usr/local /usr/local
COPY --from=build-stage /app /app

RUN addgroup --gid 1000 --system ${USER} && \
    adduser --uid 1000 --system ${USER} --gid 1000

RUN chmod -R 777 /app/ && \
    chown -Rf ${USER}:${USER} /app/

USER ${USER} 
CMD python app.py