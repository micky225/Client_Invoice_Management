FROM python:3.11

RUN apt-get update
RUN pip install --upgrade pip

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /setup

# Install dependencies
COPY requirements.txt /setup
RUN pip install --no-cache-dir -r requirements.txt && pip check

# Copy project
COPY . /setup


# Command to run when the container starts
CMD ["gunicorn", "setup.wsgi:application", "--bind","8000"]