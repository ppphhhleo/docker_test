FROM tiangolo/uwsgi-nginx-flask:python3.8
#ENV STATIC_INDEX 1
ENV STATIC_PATH /app/app/static
COPY ./app /app
