FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY demo-app.py .

# Expose port for Flask
EXPOSE 5000

# Run the app
CMD ["python", "-u", "demo-app.py"]