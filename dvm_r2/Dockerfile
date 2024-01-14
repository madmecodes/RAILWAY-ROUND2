FROM python:3.11.4-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

RUN pip install gunicorn

CMD ["bash", "-c", "\
python manage.py makemigrations && \
python manage.py migrate && \
python manage.py create_initial_trains && \
python manage.py populate_myapp_station && \
python manage.py makemigrations && \
python manage.py migrate && \ 
python manage.py runserver 0.0.0.0:8000"]


