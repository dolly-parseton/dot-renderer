FROM ubuntu:latest

RUN apt update && apt-get install -y software-properties-common python3 python3-pip xdg-utils
RUN add-apt-repository universe
RUN apt-get install -y graphviz

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "app.py" ]