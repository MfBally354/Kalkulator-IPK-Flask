# Base image Python
FROM python:3.11-slim

# Set folder kerja di container
WORKDIR /app

# Copy file requirements
COPY requirements.txt .

# Install dependency
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua file ke container
COPY . .

# Buka port Flask
EXPOSE 5000

# Jalankan Flask
CMD ["python", "app.py"]

