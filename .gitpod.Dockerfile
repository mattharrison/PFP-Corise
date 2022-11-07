FROM gitpod/workspace-full:latest

USER gitpod

COPY requirements.txt .
RUN pip3 install -U pip
RUN pip3 install -r requirements.txt
