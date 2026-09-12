# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the script and dataset into the container
COPY ml_example.py .
COPY data.csv .

# Install required Python packages for the ML script
RUN pip install --no-cache-dir pandas scikit-learn numpy

# Specify the command to run your ML script
CMD ["python", "ml_example.py"]