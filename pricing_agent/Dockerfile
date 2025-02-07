# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p /app/uploads

# Expose port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=pricing_agent.py
ENV FLASK_ENV=production

# Run application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "pricing_agent:app"]