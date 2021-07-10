FROM python:3.8.2-buster AS build-stage

LABEL maintainer="<davidba941@gmail.com> <https://github.com/hopeswiller/voicecontrol>"


RUN apt-get update
RUN apt-get install -y portaudio19-dev \
    python-all-dev python3-all-dev

# RUN apt-get install -y python-pyaudio python3-pyaudio

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt requirements.txt


# RUN pip install --upgrade pip
RUN pip install pyaudio
RUN pip install -r requirements.txt

COPY . .

###############################################################


FROM python:3.8.2-buster

WORKDIR /app

COPY --from=build-stage /usr/local /usr/local
COPY --from=build-stage /app /app

RUN adduser -D hopeswiller && chown -R hopeswiller:hopeswiller /app/
USER hopeswiller
