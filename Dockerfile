FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y \
    python3.9 \
    python3-pip \
    r-base \
    julia \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .