# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /src

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application code into the container
COPY src /src

# Command to run the FastAPI application within the container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
