PRJ_DIR=/Users/mmngreco/github/mmngreco/sphinx-automated
docker build -t sphx:tst -f $PRJ_DIR/Dockerfile $PRJ_DIR
test=$(docker run --rm -v $PRJ_DIR:/root/sphinx_automated/ -d -i sphx:tst /bin/bash)
docker exec $test pip install /root/sphinx_automated/.
docker exec $test pip list | grep -i sphinx
docker exec $test python -m sphinx_automated.run -c /root/sphinx_automated/tests/project.ini
docker stop $test
