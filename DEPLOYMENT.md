# Deployment Guide for YouTube Downloader

This guide covers different deployment options for the YouTube Downloader application, from simple local deployment to production-ready setups.

## Deployment Options

### 1. Local Development Deployment (Current Setup)
For development and testing purposes, you can run the application locally as described in [HOW_TO_RUN.md](HOW_TO_RUN.md):

1. **Backend (Flask API)**:
   ```bash
   python app.py
   ```
   Runs on: http://localhost:5000

2. **Frontend (React)**:
   ```bash
   cd frontend
   npm start
   ```
   Runs on: http://localhost:3000

### 2. Production Deployment Options

#### Option A: Static Frontend + Flask Backend (Recommended for simplicity)

1. **Build the React Frontend for Production**:
   ```bash
   cd frontend
   npm run build
   ```
   This creates a `build` directory with optimized static files.

2. **Modify Flask App to Serve Static Files**:
   Update [app.py](file:///c%3A/Users/mulac/Downloads/youtube-downloader/app.py) to serve the React build:
   ```python
   from flask import Flask, request, jsonify, send_from_directory
   from flask_cors import CORS
   import subprocess
   import os
   import sys
   
   app = Flask(__name__, static_folder='frontend/build')
   CORS(app)  # Enable CORS for all routes
   
   # Get the directory of the current script
   current_dir = os.path.dirname(os.path.abspath(__file__))
   
   # Serve React App
   @app.route('/', defaults={'path': ''})
   @app.route('/<path:path>')
   def serve(path):
       if path != "" and os.path.exists(app.static_folder + '/' + path):
           return send_from_directory(app.static_folder, path)
       else:
           return send_from_directory(app.static_folder, 'index.html')
   
   # Your existing API routes...
   
   if __name__ == '__main__':
       # Serve on all addresses in production
       app.run(host='0.0.0.0', debug=False, port=5000)
   ```

3. **Run the Production Server**:
   ```bash
   python app.py
   ```
   Access the application at: http://your-server-ip:5000

#### Option B: Separate Servers with Reverse Proxy (Recommended for scalability)

1. **Build the React Frontend**:
   ```bash
   cd frontend
   npm run build
   ```

2. **Serve the Frontend with a Web Server** (Nginx example):
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;
       
       location / {
           root /path/to/your/project/frontend/build;
           try_files $uri $uri/ /index.html;
       }
   }
   ```

3. **Run the Flask Backend**:
   ```bash
   python app.py
   ```
   Or use a WSGI server like Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

4. **Configure Reverse Proxy** (Nginx example):
   ```nginx
   server {
       listen 80;
       server_name api.your-domain.com;
       
       location / {
           proxy_pass http://localhost:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

#### Option C: Containerized Deployment (Docker)

1. **Create a Dockerfile for the Backend**:
   ```dockerfile
   FROM python:3.9-slim
   
   WORKDIR /app
   
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   
   COPY . .
   
   # Build frontend
   RUN cd frontend && npm install && npm run build
   
   EXPOSE 5000
   
   CMD ["python", "app.py"]
   ```

2. **Create a docker-compose.yml**:
   ```yaml
   version: '3.8'
   
   services:
     youtube-downloader:
       build: .
       ports:
         - "5000:5000"
       volumes:
         - ./downloads:/app/downloads
   ```

3. **Run with Docker Compose**:
   ```bash
   docker-compose up -d
   ```

## Server Requirements

### Minimum Requirements
- Python 3.6+
- Node.js 12+ (for building frontend)
- 1 GB RAM
- 1 CPU core
- Storage space for downloaded videos

### Recommended Requirements
- Python 3.8+
- Node.js 14+ (for building frontend)
- 2 GB RAM
- 2+ CPU cores
- Sufficient storage space for downloaded videos

## Security Considerations

1. **Disable Debug Mode**: 
   Ensure `debug=False` in production:
   ```python
   app.run(debug=False, host='0.0.0.0', port=5000)
   ```

2. **Use a Reverse Proxy**: 
   Deploy behind Nginx or Apache for better security and performance.

3. **Rate Limiting**: 
   Implement rate limiting to prevent abuse:
   ```bash
   pip install Flask-Limiter
   ```
   
   Add to [app.py](file:///c%3A/Users/mulac/Downloads/youtube-downloader/app.py):
   ```python
   from flask_limiter import Limiter
   from flask_limiter.util import get_remote_address
   
   limiter = Limiter(
       app,
       key_func=get_remote_address,
       default_limits=["100 per hour", "10 per minute"]
   )
   
   @app.route('/api/download', methods=['POST'])
   @limiter.limit("5 per minute")
   def download_video():
   ```

4. **Input Validation**: 
   Add URL validation to ensure only YouTube URLs are processed.

5. **File System Security**: 
   Restrict download directory access and prevent directory traversal attacks.

## Environment Configuration

Create a `.env` file for configuration:
```bash
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=your-secret-key
DOWNLOAD_DIR=/path/to/downloads
```

Install python-dotenv:
```bash
pip install python-dotenv
```

Update [app.py](file:///c%3A/Users/mulac/Downloads/youtube-downloader/app.py):
```python
from dotenv import load_dotenv
load_dotenv()

# Use environment variables
download_dir = os.getenv('DOWNLOAD_DIR', 'downloads')
```

## Monitoring and Logging

1. **Add Logging to Flask App**:
   ```python
   import logging
   
   if __name__ == '__main__':
       logging.basicConfig(level=logging.INFO)
       app.run(host='0.0.0.0', debug=False, port=5000)
   ```

2. **Use Process Managers**:
   For production, use process managers like:
   - Gunicorn with Supervisor
   - PM2 for Node.js components
   - Systemd services

## Backup and Maintenance

1. **Regular Backups**: 
   Schedule backups of the download directory.

2. **Log Rotation**: 
   Implement log rotation to prevent disk space issues.

3. **Dependency Updates**: 
   Regularly update dependencies:
   ```bash
   pip install --upgrade -r requirements.txt
   cd frontend && npm update
   ```

## Troubleshooting

1. **Port Conflicts**: 
   Change the port if 5000 is in use:
   ```python
   app.run(host='0.0.0.0', debug=False, port=8000)
   ```

2. **Permission Issues**: 
   Ensure the application has write permissions to the download directory.

3. **yt-dlp Issues**: 
   Keep yt-dlp updated:
   ```bash
   pip install --upgrade yt-dlp
   ```

4. **ffmpeg Missing**: 
   Install ffmpeg for audio extraction:
   ```bash
   # Ubuntu/Debian
   sudo apt install ffmpeg
   
   # CentOS/RHEL
   sudo yum install ffmpeg
   
   # macOS
   brew install ffmpeg
   ```

## Scaling Considerations

1. **Multiple Workers**: 
   Use Gunicorn with multiple workers for handling concurrent requests.

2. **Asynchronous Processing**: 
   For heavy download tasks, consider using Celery with Redis/RabbitMQ for background processing.

3. **Load Balancing**: 
   Deploy multiple instances behind a load balancer for high availability.

4. **CDN Integration**: 
   For serving downloaded content, consider using a CDN.

This deployment guide should help you get the YouTube Downloader application running in various environments, from local development to production servers.