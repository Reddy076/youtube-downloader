# YouTube Downloader Frontend

A React-based web interface for the YouTube Video Downloader application.

## Features

- User-friendly web interface for downloading YouTube videos
- Supports video downloads in various resolutions (360p, 480p, 720p, 1080p, best)
- Supports audio extraction in MP3 or M4A formats
- Real-time download status updates

## Prerequisites

- Node.js (version 14 or higher)
- npm (usually comes with Node.js)

## Installation

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install the required dependencies:
   ```bash
   npm install
   ```

## Running the Application

1. Start the development server:
   ```bash
   npm start
   ```

2. Open your browser and navigate to `http://localhost:3000`

## Building for Production

To create a production build:
```bash
npm run build
```

## Project Structure

- `src/App.js` - Main application component
- `src/App.css` - Application styles
- `src/index.js` - Entry point

## How It Works

The frontend communicates with a Flask backend API that executes the Python YouTube downloader script. The backend API is available at `http://localhost:5000`.

## Development

To modify the application:
1. Edit files in the `src` directory
2. The application will automatically reload with your changes
3. For major changes, you may need to restart the development server

## Troubleshooting

If you encounter issues:
1. Make sure all dependencies are installed: `npm install`
2. Ensure the backend server is running on port 5000
3. Check the browser console for any error messages
4. Verify that the YouTube URL is valid