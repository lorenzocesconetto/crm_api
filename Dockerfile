FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
COPY . /code
RUN pip install -r code/requirements/base.txt

COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

WORKDIR /code

ENTRYPOINT ["/docker-entrypoint.sh"]
