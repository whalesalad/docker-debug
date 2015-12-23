# Docker Debug

A simple python http application running inside of docker container that prints out environment variables. This is useful for debugging a [12-factor-app](http://12factor.net/) style service deployment.

#### To Build

    docker build -t whalesalad/docker-debug .

#### To Run
    
    # Daemon Mode
    docker run -d -p 8080:8080 whalesalad/docker-debug

    # Attached
    docker run -i -t -p 8080:8080 whalesalad/docker-debug
