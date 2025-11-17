FROM alpine:latest
WORKDIR /app
COPY . /app

RUN apk update && apk upgrade
RUN apk add python3 py3-pip
RUN pip3 install requests --break-system-packages
ENTRYPOINT ["python3", "setup.py"]
