FROM ubuntu

# Comments are like this

# Make logging work with Docker
ENV PYTHONBUFFERED=1 


# Runs:

RUN apt-get update && apt-get upgrade -y && apt-get install python3-pip python-pandas -y && pip3 install;

