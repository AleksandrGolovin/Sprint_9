FROM python:3.11-slim

# Установка необходимых утилит и Java 21
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        openjdk-21-jre-headless && \
    # Установка Allure
    wget -q https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.tgz && \
    tar -zxvf allure-2.27.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.27.0/bin/allure /usr/bin/allure && \
    # Очистка кэша
    rm allure-2.27.0.tgz && \
    apt-get purge -y --auto-remove wget && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# CMD ["pytest", "--alluredir=allure-results"]