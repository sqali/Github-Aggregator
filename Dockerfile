# Use the official Python base image with version 3.9
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the Python code and other necessary files to the working directory
COPY app.py requirements.txt ./

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the Flask application will run (if applicable)
EXPOSE 5000

# Set the command to run your Flask application
CMD ["python", "app.py"]
