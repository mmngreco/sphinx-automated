FROM jfloff/alpine-python:3.6

RUN apk add tmux vim
RUN mkdir -p /root/git
WORKDIR /root/git
RUN python -m venv venv
RUN git clone https://github.com/mmngreco/sphinx-automated
# https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
CMD source venv/bin/activate && /bin/bash
