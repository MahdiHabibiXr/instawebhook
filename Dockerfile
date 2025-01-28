# Use an official Python runtime
FROM python:3.10

# Set the working directory
WORKDIR /app

# Install system dependencies (including FFmpeg)
RUN apt-get update && apt-get install -y ffmpeg

# Copy the project files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the correct port
EXPOSE 8000

# Run the app with Uvicorn inside Gunicorn (for async support)
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000", "main:app"]
