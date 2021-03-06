FROM python:3.9

COPY get_secrets.py /get_secrets.py
COPY requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "/get_secrets.py" ]