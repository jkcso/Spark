FROM python:3.5

# This is a standard line
ENV PYTHONUNBUFFERED 1

RUN apt-get update

# Copying the files in the repo into the docker image
RUN mkdir /spark_app
WORKDIR /spark_webapp
COPY ./spark /spark_webapp

# Install requirements
RUN pip install -U pip
RUN pip install -Ur requirements.txt

# Making the port 8000 available to outside the container
EXPOSE 8000

# startup.sh would be ran when the image starts
CMD ["startup.sh"]
