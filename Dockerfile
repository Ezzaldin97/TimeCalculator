FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY src /app/src
COPY utils /app/utils
COPY main.py /app/main.py

ENTRYPOINT [ "/bin/bash" ]