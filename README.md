# docker-debug

[![Docker Stars](https://img.shields.io/docker/stars/whalesalad/docker-debug.svg)](https://hub.docker.com/r/whalesalad/docker-debug/)
[![Docker Pulls](https://img.shields.io/docker/pulls/whalesalad/docker-debug.svg)](https://hub.docker.com/r/whalesalad/docker-debug/)
[![Image Size](https://img.shields.io/imagelayers/image-size/whalesalad/docker-debug/latest.svg)](https://imagelayers.io/?images=whalesalad/docker-debug:latest)
[![Image Layers](https://img.shields.io/imagelayers/layers/whalesalad/docker-debug/latest.svg)](https://imagelayers.io/?images=whalesalad/docker-debug:latest)

A simple python http application running inside of docker container that prints out environment variables. This is useful for debugging a [12-factor-app](http://12factor.net/) style service deployment.

![](http://i.imgur.com/oWpIlvz.png)

#### To Build

    docker build -t whalesalad/docker-debug .

#### To Run
    
    # Daemon Mode
    docker run -d -p 8080:8080 whalesalad/docker-debug

    # Attached
    docker run -i -t -p 8080:8080 whalesalad/docker-debug

#### TODO

- [ ] Enable content negotiation and/or a `.json` endpoint to request a json format of this instead of HTML.
