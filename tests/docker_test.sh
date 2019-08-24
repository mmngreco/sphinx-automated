docker build -t sphx:tst -f ./Dockerfile .
docker run --rm -d -i sphx:tst
docker exec test pip install sphinx_automated/. && \
docker exec test pip list | grep -i sphinx && \
docker exec test python -m sphinx_automated.run && \
docker stop test
