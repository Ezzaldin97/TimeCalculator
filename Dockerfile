FROM python:3.9

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --trusted-host pypi.python.org --no-cache-dir
COPY ./src ./src
COPY ./utils ./utils
COPY main.py main.py

ENTRYPOINT [ "/bin/bash" ]