FROM python:3.8.2-buster AS build-stage

LABEL maintainer="David Boateng Adams <davidba941@gmail.com> <https://github.com/hopeswiller/voicecontrol>"

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# RUN apk add --no-cache --update \
#     build-base \
#     python3-dev \
#     musl-dev \
#     libffi-dev \
#     openssl-dev \
#     rust \
#     cargo \
#     postgresql-dev=13.3-r0 --repository=http://dl-cdn.alpinelinux.org/alpine/v3.14/main 

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

###############################################################


FROM python:3.8.2-buster

WORKDIR /app

# RUN apk add --no-cache --update postgresql-dev=13.3-r0 --repository=http://dl-cdn.alpinelinux.org/alpine/v3.14/main 
# RUN apk add --no-cache --upgrade figlet

COPY --from=build-stage /usr/local /usr/local
COPY --from=build-stage /app /app

RUN adduser -D hopeswiller && chown -R hopeswiller:hopeswiller /app/
USER hopeswiller
