# Step 1: Choosing base image
FROM python:3.9-slim

# Step 2: Create and set working directory
WORKDIR /app

# Step 3: Copy requirements file
COPY requirements.txt .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy application code
COPY . .

# Step 6: Expose port, e.g., 8080
EXPOSE 8080

# Step 7: Download bioclip dependencies
RUN python -m src.get_bioclip

# Step 7: Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]