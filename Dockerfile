FROM tiangolo/uwsgi-nginx-flask:python3.8
#ENV STATIC_INDEX 1
ENV STATIC_PATH /app/app/static

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app
