FROM python:3.8-alpine 
LABEL MAINTAINER Kavitha

# Install needed packages. Notes:
#   * bash: so we can access /bin/bash
#   * git: to ease up clones of repos
#   * ca-certificates: for SSL verification during Pip and easy_install

ENV PACKAGES="bash \
  git \
  libffi \
  libffi-dev \
  openssl-dev \
  musl \
  build-base \
  ca-certificates"

ADD . /opt/intellisense
WORKDIR /opt/intellisense

RUN apk add --no-cache $PACKAGES

# Install and upgrade Pip & Requeriments
RUN easy_install pip \
    && pip install --upgrade pip \
    && pip install -r /opt/intellisense/requeriments.txt

# since we will be "always" mounting the volume, we can set this up
CMD ["python", "main.py"]