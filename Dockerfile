FROM python:3.6.8-alpine3.9

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./
COPY requirements requirements/

RUN apk update \
    && apk add --no-cache --virtual .build-deps \
        gcc \
        musl-dev \
        python3-dev \
        postgresql-dev \
    && pip install -r requirements.txt \
    && apk del .build-deps \
    && apk add --no-cache libpq

COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
