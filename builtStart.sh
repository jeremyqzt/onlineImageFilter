#!/bin/bash
app="filter"
docker container stop ${app}
docker image rm ${app}
docker build -t ${app} .

docker run -p 5000:80 ${app}
