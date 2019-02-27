FROM python:3.6-slim

ENV RASA_CORE_HOME=/app

SHELL ["/bin/bash", "-c"]

RUN apt-get update -qq && \
  apt-get install -y --no-install-recommends \
  build-essential \
  wget \
  openssh-client \
  graphviz-dev \
  pkg-config \
  git-core \
  openssl \
  libssl-dev \
  libffi6 \
  libffi-dev \
  libpng-dev \
  curl && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
  mkdir /app

WORKDIR ${RASA_CORE_HOME}

COPY . .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r docker/requirements.txt

RUN chmod +x ./entrypoint.sh

RUN rm -rf ./usecase/callcenter/models

RUN python ./usecase/callcenter/train_core.py

VOLUME ["/app/logs"]

EXPOSE 5005

ENTRYPOINT ["./entrypoint.sh"]
