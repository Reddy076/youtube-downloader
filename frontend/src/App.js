import React, { useState } from 'react';
import './App.css';

// Use environment variable for API base URL, fallback to localhost for development
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

function App() {
  const [url, setUrl] = useState('');
  const [resolution, setResolution] = useState('720p');
  const [format, setFormat] = useState('mp4');
  const [audioOnly, setAudioOnly] = useState(false);
  const [audioFormat, setAudioFormat] = useState('mp3');
  const [isDownloading, setIsDownloading] = useState(false);
  const [downloadStatus, setDownloadStatus] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsDownloading(true);
    setDownloadStatus('Starting download...');
    
    try {
      const response = await fetch(`${API_BASE_URL}/api/download`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          url,
          resolution,
          format,
          audioOnly,
          audioFormat
        }),
      });
      
      const data = await response.json();
      
      if (response.ok && data.success) {
        setDownloadStatus('Download completed successfully!');
      } else {
        setDownloadStatus(`Error: ${data.error || 'Download failed'}`);
      }
    } catch (error) {
      setDownloadStatus(`Error: ${error.message}`);
    } finally {
      setIsDownloading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>YouTube Video Downloader</h1>
        <p>Download videos and audio from YouTube easily</p>
      </header>
      
      <main className="main-content">
        <form onSubmit={handleSubmit} className="download-form">
          <div className="form-group">
            <label htmlFor="url">YouTube URL:</label>
            <input
              type="text"
              id="url"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              placeholder="https://www.youtube.com/watch?v=..."
              required
            />
          </div>
          
          <div className="form-group checkbox-group">
            <label>
              <input
                type="checkbox"
                checked={audioOnly}
                onChange={(e) => setAudioOnly(e.target.checked)}
              />
              Audio Only
            </label>
          </div>
          
          {!audioOnly ? (
            <>
              <div className="form-group">
                <label htmlFor="resolution">Resolution:</label>
                <select
                  id="resolution"
                  value={resolution}
                  onChange={(e) => setResolution(e.target.value)}
                >
                  <option value="360p">360p</option>
                  <option value="480p">480p</option>
                  <option value="720p">720p</option>
                  <option value="1080p">1080p</option>
                  <option value="best">Best Available</option>
                </select>
              </div>
              
              <div className="form-group">
                <label htmlFor="format">Video Format:</label>
                <select
                  id="format"
                  value={format}
                  onChange={(e) => setFormat(e.target.value)}
                >
                  <option value="mp4">MP4</option>
                  <option value="webm">WebM</option>
                </select>
              </div>
            </>
          ) : (
            <div className="form-group">
              <label htmlFor="audioFormat">Audio Format:</label>
              <select
                id="audioFormat"
                value={audioFormat}
                onChange={(e) => setAudioFormat(e.target.value)}
              >
                <option value="mp3">MP3</option>
                <option value="m4a">M4A</option>
              </select>
            </div>
          )}
          
          <button 
            type="submit" 
            disabled={isDownloading}
            className="download-button"
          >
            {isDownloading ? 'Downloading...' : 'Download'}
          </button>
        </form>
        
        {downloadStatus && (
          <div className={`status-message ${downloadStatus.includes('Error') ? 'error' : 'success'}`}>
            {downloadStatus}
          </div>
        )}
        
        <div className="instructions">
          <h2>How to Use</h2>
          <ol>
            <li>Enter the YouTube URL you want to download</li>
            <li>Choose your preferred settings (resolution, format, etc.)</li>
            <li>Click the Download button</li>
            <li>Check your downloads folder for the file</li>
          </ol>
        </div>
      </main>
      
      <footer className="App-footer">
        <p>YouTube Video Downloader &copy; {new Date().getFullYear()}</p>
      </footer>
    </div>
  );
}

export default App;