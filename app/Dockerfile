## Dockerfile

# Use an official TensorFlow runtime as a parent image
FROM tensorflow/tensorflow:latest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies for Pillow
RUN apt-get update \
    && apt-get install -y libjpeg-dev zlib1g-dev libtiff5-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Flask and other required libraries
RUN pip install --no-cache-dir -r requirements.txt

# Install MySQL Connector
RUN pip install mysql-connector-python

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the app.py when the container launches
CMD ["python", "app.py"]
