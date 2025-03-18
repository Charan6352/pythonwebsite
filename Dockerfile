# Use the appropriate base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your project files into the container
COPY . .

# Install necessary dependencies (if using Flask/Django, adapt this step)
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your application will run on (default is 5000 for Flask)
EXPOSE 5000

# Define the command to run your application (replace 'app.py' with your main file)
CMD ["python", "app.py"]
