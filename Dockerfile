FROM python:3.13-slim

# Install dependencies for Playwright browsers
RUN apt-get update && apt-get install -y \
    wget \
    libnss3 \
    libglib2.0-0 \
    libgtk-3-0 \
    libdbus-glib-1-2 \
    libx11-xcb1 \
    libasound2 \
    libatk1.0-0 \
    libcups2 \
    libexpat1 \
    libatk-bridge2.0-0 \
    libxcomposite1 \
    libxrandr2 \
    libxss1 \
    libxkbcommon-x11-0 \
    libgbm1 \
    libcairo2 \
    libpango-1.0-0 \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install

# Copy the source code
COPY src /app/src

# Command to run Xvfb and then the bot
CMD ["sh", "-c", "Xvfb :99 -screen 0 1280x720x24 & DISPLAY=:99 python src/bot.py"]