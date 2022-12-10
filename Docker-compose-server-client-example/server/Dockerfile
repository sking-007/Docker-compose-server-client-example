# Just a remember, dockerfile must always start by importing the base image.
# We use the keyword 'FROM' to do that.
# In our example, we want to import the python image (from DockerHub).
# So, we write 'python' for the image name and 'latest' for the version
FROM python:3.9-alpine




WORKDIR /server/
#Install Pika
RUN pip3 install pika
# Install any needed packages specified in requirements.txt
#RUN pip install --trusted-host pypi.python.org -r requirements.txt
#COPY requirements.txt ./

# Here we put files at the image '/server/' folder.
ADD server.py /server/
#ADD index.html /server/
ADD dataStructures.py /server/
ADD receive.py /server/
ADD init.sh /server/

#Install Pika
RUN pip install pika

CMD ["/bin/sh", "./config/init/init.sh"]
