# Use the latest Python image from the Docker Hub (Python 3.13)
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose port 5000
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]
