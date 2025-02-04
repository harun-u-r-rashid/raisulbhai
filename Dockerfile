# Use official Python image
FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose port 8000 for Django
EXPOSE 8000

# Start Django app with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "aaracol_healthcare.wsgi:application"]
