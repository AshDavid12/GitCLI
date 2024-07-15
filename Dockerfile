# Use the official Python image as the base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy only the poetry.lock and pyproject.toml files to the working directory
COPY pyproject.toml poetry.lock /app/

# Install Poetry
RUN pip install poetry

# Install project dependencies
RUN poetry install --no-root

# Copy the rest of the application code to the working directory
COPY . /app/

# Set the default command to run the CLI
CMD ["poetry", "run", "python", "cli.py"]
