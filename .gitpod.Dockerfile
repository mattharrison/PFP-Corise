FROM gitpod/workspace-full:latest

USER gitpod

RUN pip3 install -U pip
RUN pip3 install flask==2.1.3 pytest==7.1.1
