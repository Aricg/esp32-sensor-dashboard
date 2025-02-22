# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY web_server/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY web_server /app

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
