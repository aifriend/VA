FROM python:3.6-slim

ENV RASA_ACTION_HOME=/app

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

WORKDIR ${RASA_ACTION_HOME}

COPY . .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r docker/requirements.txt

RUN pip install --no-cache-dir rasa_core_sdk

RUN chmod +x ./entrypoint.sh

VOLUME ["/app/logs"]

EXPOSE 5055

ENTRYPOINT ["./entrypoint.sh"]
