FROM python:3.6

ADD . /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

RUN echo yes | python manage.py collectstatic

EXPOSE 8000

CMD exec gunicorn humo.wsgi:application --bind 0.0.0.0:8000 --workers 3