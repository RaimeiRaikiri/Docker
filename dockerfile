FROM python:latest

ADD main.py .
RUN pip install requests

WORKDIR /usr/src/app
COPY main.py ./
CMD ["python", "./main.py"]