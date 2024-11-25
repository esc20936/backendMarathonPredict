# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

EXPOSE 8000

# Specify the command to run your application (adjust as necessary)
CMD ["uvicorn", "Server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

