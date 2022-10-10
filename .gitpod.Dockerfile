FROM gitpod/workspace-full:latest

USER gitpod

RUN npm i @learnpack/learnpack@2.1.20 -g && learnpack plugins:install @learnpack/python@1.0.0

ENV VENV=coriseenv
#RUN pip3 install pytest==4.4.2 mock pytest-testdox toml

RUN python3 -m venv $VENV
RUN ls .

COPY requirements.txt .
RUN . $VENV/bin/activate && pip install -r requirements.txt