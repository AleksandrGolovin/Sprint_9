FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y openjdk-17-jre-headless && \
    wget https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.tgz && \
    tar -zxvf allure-2.27.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.27.0/bin/allure /usr/bin/allure && \
    rm allure-2.27.0.tgz

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# CMD ["pytest", "--alluredir=allure-results"]