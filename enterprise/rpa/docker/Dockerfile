FROM python:3.6-slim

ENV RPA_HOME=/app

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

WORKDIR ${RPA_HOME}

COPY . .

RUN pip install --upgrade pip

RUN pip install -r docker/requirements.txt --no-cache-dir

RUN chmod +x ./entrypoint.sh

VOLUME ["/app/logs"]

EXPOSE 8095

ENTRYPOINT ["./entrypoint.sh"]

