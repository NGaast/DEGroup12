# Using python 3.7 full image as the base image
FROM python:3.7.7-slim

# Defining working directory and copy the requirements file. We will run the commands inside this new directory
WORKDIR /src

# Copy requirements.txt  to the working directory
COPY requirements.txt .

# Install required python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files in Data_ingestion local host directory to /src in Docker container
COPY . .

# Expose the port that our app runs in
EXPOSE 5000

# Enviroment Variables
ENV PIPELINE_NAME=housing-price
ENV PIPELINE_TEMPLATE=./house_pricing_training_pipeline.json
ENV PIPELINE_FOLDER=gs://de_jads_temp_ng
ENV PIPELINE_PARAMETERS=./parameters.json

# Run our App
CMD ["python3","app.py"]