FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . /app/

# Expose the port
EXPOSE 8080

# Command to run the app
CMD ["gunicorn", "jokerandomizer.wsgi:application", "--bind", "0.0.0.0:8080"]