# Use an official Python runtime
FROM python:3.10

# Set the working directory
WORKDIR /app

# Install system dependencies (including FFmpeg)
RUN apt-get update && apt-get install -y ffmpeg

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create directory for files
RUN mkdir -p files

# Expose port 5000 (matches the port in main.py)
EXPOSE 5000

# Run the Flask app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]