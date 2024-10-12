# Use a base image from Docker Hub
FROM python:3.9-slim-bullseye

# Set the working directory inside the container
WORKDIR /app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application files from the host machine to the container
COPY . .

# Expose a port for the application (optional)
EXPOSE 8501

# Define the command to run when the container starts
CMD [ "streamlit", "run", "app.py" ]