# Concept 1: Base Image (starting point with Python pre-installed)
FROM python:3.10-slim

# Concept 2: Working Directory (sets directory inside container)
WORKDIR /app

# Concept 3: Copying files (copies dependency lists first for build caching)
COPY requirements.txt .

# Concept 4: RUN command (executes setup commands inside container)
RUN pip install --no-cache-dir -r requirements.txt

# Copy source application into container
COPY . .

# Concept 5: EXPOSE (documents port service operates on)
EXPOSE 8000

# Concept 6: CMD (command executed when container boots up)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]