## Dockerfile app

FROM tensorflow/tensorflow:latest

WORKDIR /app

COPY . /app

# Install system dependencies for Pillow
RUN apt-get update \
    && apt-get install -y libjpeg-dev zlib1g-dev libtiff5-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install mysql-connector-python

EXPOSE 80

# Run the create_and_train_model then app.py when the container launches
CMD ["python", "create_and_train_model.py", "app.py"]
