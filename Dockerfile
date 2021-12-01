# Pobranie obrazu pythonowego
FROM python:3.9-slim
# Ustawienie folderu /usr/src/app
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
 

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Zanstalowanie apt zależności netcat gcc
RUN apt-get update \
    && apt-get install -y netcat gcc \
    && apt-get clean

# Zainstalowanie zależności pythonowych
COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt 

# Skopiowanie apki
COPY . .
