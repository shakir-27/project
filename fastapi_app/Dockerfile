
# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./requirements.txt .
COPY ./main.py .
COPY ./frontend ./frontend

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variables
ENV TORRENT_STORAGE_PATH="/app/torrents"
ENV DATABASE_URL="/app/torrents.db"
ENV SECRET_KEY="your-very-secret-key-here"

# Run the uvicorn server when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
