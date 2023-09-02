# Use an official Python runtime as a parent image
FROM python:3.11.4

# Install system dependencies
RUN apt-get update && apt-get install -y curl

# Install poetry
RUN curl -sSL https://install.python-poetry.org/ | python -
ENV PATH="/root/.local/bin:$PATH"

# Set the working directory to /app
WORKDIR /app

# Install Tesseract OCR
RUN apt-get install -y tesseract-ocr

# Copy the project files into the container
COPY . /app

# Configure poetry and install dependencies
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Set the working directory to /app/src/api
WORKDIR /app/src/api

