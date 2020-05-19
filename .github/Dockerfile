FROM ubuntu:16.04 AS base

# Install system requirements
RUN apt update \
    && apt install -y --no-install-recommends python2.7 python-dev python-pip python-setuptools libmysqlclient-dev mysql-client git make build-essential gcc locales \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip

# Setup system locales, this is used to fix accent in code
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

ADD . /openedx/notifier
WORKDIR /openedx/notifier

RUN pip install -r requirements.txt \
  && pip install python-json-logger==0.1.11

FROM base AS scheduler
CMD ["python", "manage.py", "scheduler"]

FROM base AS worker
CMD ["python", "manage.py", "celery", "worker"]
