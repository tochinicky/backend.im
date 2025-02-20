# Use official Python image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy project files
COPY main.py requirements.txt /app/
COPY test /app/test/ 

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt pytest

# Set PYTHONPATH so Python finds main.py
ENV PYTHONPATH="/app"

# Expose FastAPI port
EXPOSE 8000

# Command to run the API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]