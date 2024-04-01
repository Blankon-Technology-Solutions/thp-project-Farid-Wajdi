# Use an official Python runtime as a parent image
FROM python:3.10-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install Cython
RUN pip install --no-cache-dir Cython
RUN pip install --no-cache-dir daphne

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /code/

# Expose the port the app runs in
EXPOSE 8000

# Define the command to start the app
CMD ["daphne", "todo_list.asgi:application", "-b","0.0.0.0","--port", "8000"]
