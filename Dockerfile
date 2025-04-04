FROM python:3.12-bookworm

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file separately to leverage Docker cache
COPY requirements.txt .

# Install any system dependencies
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y dist-upgrade && \
    apt-get -y autoremove && \
    apt-get install -y --no-install-recommends \
    espeak \
    ffmpeg \
    libespeak1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Run the application
CMD ["python", "main.py"]
