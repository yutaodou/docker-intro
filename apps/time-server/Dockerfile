FROM python:3.7.0-alpine3.8

RUN pip install Flask

ADD app.py /home/app.py

WORKDIR /home

EXPOSE 5000

ENTRYPOINT ["python", "app.py"]