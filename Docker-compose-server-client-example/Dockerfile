FROM rabbitmq


#install Python
RUN apt-get update &&\
    apt-get install -y \
    python3-pip
WORKDIR /rabbitmq/
#Install Pika
RUN pip3 install pika
ADD init.sh /server/
CMD ["python3", "ffmpeg.py"]
