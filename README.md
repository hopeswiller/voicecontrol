# Voice Control

> A Voice Recognition System that takes voice commands from users to either shutdown or lock your computer. Also gives current weather status

## Table of contents

- [General info](#general-info)
- [Technologies](#technologies)
- [Setup](#setup)
- [Features](#features)
- [Status](#status)

## General info

This project is primarily developed to help .....


## Technologies

- Python - version 3.8
- pyttsx3 - version 2.71
- pyaudio- version 0.2.11
- speechrecognition - version 3.8.1
- OpenWeather Map API - <https://openweathermap.org/api>


## Setup

Setup can be done manually or via Docker which is recommended

- #### Manual
Remove pywin32==301 from requirements file if any as it's only supported till python 3.3

    >_ pip install -r requirements.txt
    >_ ./start.sh

> Having installations issues with pyaudio on windows? 

    >_ pip install pipwin
    >_ pipwin install pyaudio

- ## Docker

    You require the name of your recording sound device for this. To find it use `arecord -l | grep -i card`. You should get something similiar to `card 2: Generic_1 [HD-Audio Generic], device 0: ALC285 Analog [ALC285 Analog]`. In this case the name of the sound card is `Generic_1`. 
    
    ```
    export ALSA_CARD=<your card name>
    docker-compose up --build
    ```
    


## Features

List of features ready and TODOs for future development

- [x] Interact with an assistant (Will)
- [x] Check weather status of current location
- [x] Shutdown your computer
- [x] Lock you computer


TODOs:

- [ ] Configure sphinx docs
- [ ] Add pre-commit hooks
- [ ] Add more tests
- [ ] Solve docker build issues


## Status

Project is: _in progress_
