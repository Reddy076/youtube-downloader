# Render-Ready YouTube Downloader

This application is now configured for deployment to Render with the following changes:

## Files Added/Modified

1. **[app.py](file:///c%3A/Users/mulac/Downloads/youtube-downloader/app.py)** - Updated to serve React frontend and work with Render environment
   - Added static file serving for React build
   - Configured to use PORT environment variable
   - Disabled debug mode for production

2. **[requirements.txt](file:///c%3A/Users/mulac/Downloads/youtube-downloader/requirements.txt)** - Added gunicorn for production deployment
   - yt-dlp>=2023.3.4
   - Flask>=2.0.0
   - Flask-CORS>=3.0.0
   - gunicorn>=20.1.0

3. **[render.yaml](file:///c%3A/Users/mulac/Downloads/youtube-downloader/render.yaml)** - Render deployment configuration
   - Defines web service with build and start commands
   - Specifies Python version

4. **[build.sh](file:///c%3A/Users/mulac/Downloads/youtube-downloader/build.sh)** - Build script for Render
   - Installs Python dependencies
   - Installs Node.js if needed
   - Builds React frontend

5. **[runtime.txt](file:///c%3A/Users/mulac/Downloads/youtube-downloader/runtime.txt)** - Specifies Python version for Render
   - python-3.9.6

6. **[README.Render.md](file:///c%3A/Users/mulac/Downloads/youtube-downloader/README.Render.md)** - Detailed Render deployment instructions
   - Step-by-step deployment guide
   - Troubleshooting tips
   - File structure explanation

7. **[README.md](file:///c%3A/Users/mulac/Downloads/youtube-downloader/README.md)** - Updated with Render deployment section
   - Quick deploy instructions
   - Link to detailed Render guide

8. **[.gitignore](file:///c%3A/Users/mulac/Downloads/youtube-downloader/.gitignore)** - Updated to exclude Node.js files
   - Added node_modules and build directories

## Deployment Instructions

### Quick Deploy to Render:

1. Fork this repository to your GitHub account
2. Sign up at [render.com](https://render.com)
3. Create a new Web Service
4. Connect your GitHub repository
5. Use these settings:
   - Build command: `./build.sh`
   - Start command: `gunicorn app:app`
6. Deploy!

### Manual Deployment Steps:

1. **Build the frontend** (locally or on Render):
   ```bash
   cd frontend
   npm install
   npm run build
   ```

2. **Deploy to Render**:
   - Environment: Python 3
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`

## How It Works

1. **Build Phase**:
   - Render runs `build.sh` which installs dependencies and builds the React frontend
   - The build output is placed in `frontend/build/`

2. **Runtime**:
   - The Flask app serves both the API endpoints and the React frontend
   - Static files are served from `frontend/build/`
   - API requests are handled by Flask routes

3. **Environment**:
   - Uses PORT environment variable provided by Render
   - Debug mode is disabled for production

## Testing Locally

To test the Render-ready configuration locally:

1. Build the frontend:
   ```bash
   cd frontend
   npm install
   npm run build
   cd ..
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Visit `http://localhost:5000` to see the React frontend
4. Test the API at `http://localhost:5000/api/status`

## File Structure

```
youtube-downloader/
├── app.py              # Flask application (serves API + frontend)
├── requirements.txt    # Python dependencies (including gunicorn)
├── runtime.txt         # Python version for Render
├── build.sh            # Build script for Render
├── render.yaml         # Render deployment configuration
├── README.Render.md    # Render deployment guide
├── youtube_downloader.py  # YouTube download script
├── frontend/           # React frontend
│   ├── package.json
│   ├── src/
│   └── build/          # Created during build
└── downloads/          # Directory for downloaded files
```

## Notes

- The application is configured to work with Render's free tier
- Downloads will be stored in the `downloads/` directory (note: files may be lost when the service restarts on the free tier)
- CORS is enabled for all origins in the Flask app
- The React frontend is built and served statically by the Flask app