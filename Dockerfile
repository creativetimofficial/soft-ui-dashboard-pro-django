FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Accept build arguments for GitHub token
ARG GITHUB_TOKEN

# Use the GitHub token during pip install
RUN git config --global url."https://${GITHUB_TOKEN}:x-oauth-basic@github.com/".insteadOf "https://github.com/"

# Debugging: Print the GITHUB_TOKEN during the build process
RUN echo "GITHUB_TOKEN=${GITHUB_TOKEN}"

# Copy requirements.txt
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Running migrations
RUN python manage.py migrate

# gunicorn command
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]
