# Deploying to Render

This document provides instructions for deploying the YouTube Downloader application to Render.

## Prerequisites

1. A Render account (sign up at [render.com](https://render.com))
2. This repository connected to Render

## Deployment Steps

1. Go to your Render Dashboard
2. Click "New" and select "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - Name: youtube-downloader
   - Environment: Python 3
   - Build command: `./build.sh`
   - Start command: `gunicorn app:app`
   - Auto-deploy: Yes (recommended)

5. Add environment variables (if needed):
   - PORT: 5000 (Render will automatically set this)

6. Click "Create Web Service"

## How it Works

The deployment process:

1. Render runs the `build.sh` script which:
   - Installs Python dependencies from `requirements.txt`
   - Installs Node.js (if not available)
   - Installs frontend dependencies
   - Builds the React frontend

2. Render then starts the application using Gunicorn with the command `gunicorn app:app`

## File Structure for Render

```
youtube-downloader/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── runtime.txt         # Python version
├── build.sh            # Build script
├── render.yaml         # Render configuration
├── youtube_downloader.py  # YouTube download script
├── frontend/           # React frontend
│   ├── package.json
│   ├── src/
│   └── build/          # Created during build
└── downloads/          # Directory for downloaded files
```

## Environment Variables

Render automatically provides the `PORT` environment variable. The application is configured to use this port.

## Troubleshooting

1. **Build Failures**: Check the build logs in the Render dashboard
2. **Runtime Errors**: Check the application logs in the Render dashboard
3. **Frontend Issues**: Ensure the React build is successful
4. **Dependency Issues**: Verify all dependencies are in `requirements.txt`

## Custom Domain

To use a custom domain:
1. Go to your service in the Render dashboard
2. Click "Settings"
3. Scroll to "Custom Domains"
4. Follow the instructions to add your domain

## Scaling

Render automatically handles scaling for the free tier. For paid tiers, you can configure:
- Instance count
- Instance size
- Auto-scaling rules