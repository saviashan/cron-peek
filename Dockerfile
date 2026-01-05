# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container at /app
COPY main.py .

# Define the entrypoint for the container.
# This will execute the cron-peek tool when the container starts.
ENTRYPOINT ["python", "main.py"]

# Set the default command to an empty string.
# This allows users to pass the cron expression directly to `docker run`.
CMD [""]
