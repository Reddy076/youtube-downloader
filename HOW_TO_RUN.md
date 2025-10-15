# How to Run the YouTube Downloader Application

## Prerequisites
- Python 3.6+
- Node.js 12+
- npm 6+

## Installation

1. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Install frontend dependencies:
   ```
   cd frontend
   npm install
   ```

## Running the Application

You can run the backend and frontend separately:

### Running the Backend (Flask API)
From the root directory:
```
python app.py
```
The backend will be available at http://localhost:5000

### Running the Frontend (React)
From the root directory:
```
cd frontend
npm start
```
The frontend will be available at http://localhost:3000

## Development Script (Alternative)
You can also try using the development script:
```
python run_dev.py
```
However, this might not work properly on all systems, particularly Windows.

## API Endpoints
- GET `/api/status` - Check if the API is running
- POST `/api/download` - Download a YouTube video

The frontend will communicate with the backend API to download videos.