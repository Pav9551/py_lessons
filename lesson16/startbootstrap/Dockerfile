FROM python:3.9
WORKDIR /startbootstrap
COPY requirements.txt /startbootstrap
COPY . /startbootstrap
RUN pip3 install --upgrade pip -r requirements.txt
CMD python /startbootstrap/main.py
