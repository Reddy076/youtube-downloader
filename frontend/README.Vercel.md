# Deploying Frontend to Vercel

This document provides instructions for deploying the YouTube Downloader frontend to Vercel while keeping the backend on Render.

## Prerequisites

1. A Vercel account (sign up at [vercel.com](https://vercel.com))
2. This repository forked to your GitHub account
3. Backend deployed to Render (see main README for instructions)

## Deployment Steps

### 1. Prepare Your Repository

1. Make sure your repository is pushed to GitHub
2. Ensure the frontend code is in the `frontend` directory

### 2. Deploy to Vercel

1. Go to your Vercel Dashboard
2. Click "New Project"
3. Import your GitHub repository
4. Configure the project:
   - Framework Preset: `Create React App`
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `build`
   - Install Command: `npm install`

5. Set Environment Variables:
   - Add `REACT_APP_API_URL` with the URL of your Render backend
   - For your deployment: `https://youtube-downloader-i1z1.onrender.com`

6. Click "Deploy"

## Environment Variables

### Required Variables

- `REACT_APP_API_URL`: The base URL of your backend API
  - Development: `http://localhost:5000`
  - Production: `https://youtube-downloader-i1z1.onrender.com`

### Setting Environment Variables in Vercel

1. Go to your project in the Vercel Dashboard
2. Click "Settings"
3. Click "Environment Variables"
4. Add the `REACT_APP_API_URL` variable with value: `https://youtube-downloader-i1z1.onrender.com`

## How It Works

1. Vercel automatically detects the React application
2. It runs `npm install` to install dependencies
3. It runs `npm run build` to create the production build
4. The built files are served from the `build` directory
5. API requests are directed to your Render backend using the environment variable

## Configuration Files

### vercel.json
This file configures the Vercel deployment:
```json
{
  "version": 2,
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/static-build",
      "config": {
        "distDir": "build"
      }
    }
  ]
}
```

### Environment Files
- `.env`: Local development variables
- `.env.production`: Production variables (not committed to git)
- `.env.example`: Example variables for new developers

## Updating the Frontend

After making changes to the frontend:

1. Commit and push your changes to GitHub
2. Vercel will automatically deploy the new version
3. Or manually trigger a deployment from the Vercel Dashboard

## Troubleshooting

### Blank Page Issue

If you're seeing a blank page after deployment, try these steps:

1. **Check the browser console** for JavaScript errors
2. **Verify environment variables** are set correctly in Vercel
3. **Check the build logs** in Vercel for any errors during the build process
4. **Ensure the `homepage` field** in `package.json` is set to `"."`
5. **Redeploy** the application after making changes

### API Connection Issues
1. Verify that your Render backend is running at `https://youtube-downloader-i1z1.onrender.com`
2. Check that `REACT_APP_API_URL` is set correctly in Vercel
3. Ensure CORS is properly configured on your backend

### Build Failures
1. Check the build logs in the Vercel Dashboard
2. Ensure all dependencies are in `package.json`
3. Verify the build command is correct

### Environment Variables Not Working
1. Make sure variables are prefixed with `REACT_APP_`
2. Check that variables are set in the Vercel Dashboard
3. Redeploy the application after changing environment variables

## Custom Domain

To use a custom domain:

1. Go to your project in the Vercel Dashboard
2. Click "Settings"
3. Click "Domains"
4. Add your custom domain
5. Follow the DNS configuration instructions

## Notes

- The frontend and backend are deployed separately
- The frontend makes API calls to the Render backend at `https://youtube-downloader-i1z1.onrender.com`
- Environment variables are used to configure the API endpoint
- Vercel provides automatic HTTPS for custom domains