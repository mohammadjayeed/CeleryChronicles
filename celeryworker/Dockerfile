FROM python:3.11.4-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# ensure Python output is sent directly to the terminal without buffering
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

# Copy the requirements file into the container
COPY ./requirements.txt /usr/src/app/

# Install the Python dependencies
RUN pip install -r requirements.txt


COPY . /usr/src/app/