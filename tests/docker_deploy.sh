OPT=$1
echo $OPT

if [ "$OPT" = "" ];
then
    OPT=-d
fi

docker run --rm -v `pwd`:/root/git/sphinx_automated -w /root/git --name test -t $OPT jfloff/alpine-python:3.6 /bin/bash

if [ "$OPT" = "-d" ];
then
docker exec test pip install sphinx_automated/.
docker exec test pip list | grep -i sphinx
docker exec test cd /root/; python -c "import sphinx_automated as sauto; print(sauto)"
docker stop test
fi
