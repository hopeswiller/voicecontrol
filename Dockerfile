FROM python:3.8.2-buster AS build-stage

LABEL maintainer="David Boateng Adams <davidba941@gmail.com> <https://github.com/hopeswiller/voicecontrol>"

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

###############################################################


FROM python:3.8.2-buster

WORKDIR /app

# RUN apk add --no-cache --upgrade figlet

COPY --from=build-stage /usr/local /usr/local
COPY --from=build-stage /app /app

RUN adduser -D hopeswiller && chown -R hopeswiller:hopeswiller /app/
USER hopeswiller
