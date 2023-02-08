# Set base image (host OS)
FROM python:3.11-slim

# By default, listen on port 8000
EXPOSE 5000/tcp
# EXPOSE 8000/tcp

# # Set the working directory in the container
# WORKDIR /app

RUN apt update
RUN apt install -y curl

# Copy the dependencies file to the working directory
COPY requirements.txt .

# UPGRADE
RUN pip install --upgrade pip

# RUN apt install -y curl
# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
ADD . /flask
WORKDIR /flask
COPY entrypoint.sh .

# Specify the command to run on container start
# CMD [ "flask", "run" ]
# CMD [ "python", "app.py" ]
ENTRYPOINT ["bash", "entrypoint.sh"]