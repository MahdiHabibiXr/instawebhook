# Use an official Python runtime
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the correct port
EXPOSE 8000

# Use Gunicorn to run the Flask app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "main:app"]
