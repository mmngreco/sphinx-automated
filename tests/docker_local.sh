OPT=$1

if [ "$OPT" = "" ];
then
    OPT=-d
fi

docker build -t sphx:tst -f  ./Dockerfile .
docker run --rm \
    -v `pwd`:/root/git/sphinx_automated \
    -w /root/git \
    --name test \
    -t $OPT jfloff/alpine-python:3.6 \
    /bin/bash

if [ "$OPT" = "-d" ];
then

docker exec test pip install sphinx_automated/. && \
docker exec test pip list | grep -i sphinx && \
docker exec test python -m sphinx_automated.run && \
docker stop test

fi
