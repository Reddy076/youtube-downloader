# Environment Variables

This document describes the environment variables that can be used with the YouTube Downloader application.

## Current Environment Variables

### PORT
- **Purpose**: Specifies the port on which the Flask application will run
- **Default**: 5000
- **Usage**: Automatically used by Render and other cloud platforms
- **Example**: `PORT=8000`

## Suggested Environment Variables

To make the application more configurable, you might consider adding support for these environment variables:

### FLASK_DEBUG
- **Purpose**: Enable or disable debug mode for the Flask application
- **Default**: False (disabled in production)
- **Usage**: Set to "True" to enable debug mode
- **Example**: `FLASK_DEBUG=True`

### DOWNLOADS_DIR
- **Purpose**: Specify the directory where downloaded videos will be saved
- **Default**: "downloads" (relative to application directory)
- **Usage**: Set to an absolute path for a specific download location
- **Example**: `DOWNLOADS_DIR=/var/www/downloads`

### YOUTUBE_DOWNLOADER_OUTPUT_DIR
- **Purpose**: Override the default output directory for the youtube_downloader.py script
- **Default**: "downloads"
- **Usage**: Set to customize where files are saved
- **Example**: `YOUTUBE_DOWNLOADER_OUTPUT_DIR=/home/user/youtube-videos`

### CORS_ORIGINS
- **Purpose**: Specify allowed origins for Cross-Origin Resource Sharing
- **Default**: "*" (all origins)
- **Usage**: Set to a specific domain or comma-separated list of domains
- **Example**: `CORS_ORIGINS=https://yourdomain.com,https://www.yourdomain.com`

### MAX_FILE_SIZE
- **Purpose**: Limit the maximum file size that can be downloaded (in MB)
- **Default**: No limit
- **Usage**: Set to restrict download size
- **Example**: `MAX_FILE_SIZE=500`

## Implementation Examples

### Adding FLASK_DEBUG Support

Modify [app.py](file:///c%3A/Users/mulac/Downloads/youtube-downloader/app.py):
```python
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', debug=debug, port=port)
```

### Adding DOWNLOADS_DIR Support

Modify [youtube_downloader.py](file:///c%3A/Users/mulac/Downloads/youtube-downloader/youtube_downloader.py) in the YouTubeDownloader class:
```python
def __init__(self, output_dir: str = None):
    """Initialize the YouTube downloader.
    
    Args:
        output_dir: Directory where downloaded files will be saved.
                   If None, uses DOWNLOADS_DIR environment variable or defaults to "downloads".
    """
    if output_dir is None:
        output_dir = os.environ.get('DOWNLOADS_DIR', 'downloads')
    
    self.output_dir = output_dir
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
```

### Adding CORS_ORIGINS Support

Modify [app.py](file:///c%3A/Users/mulac/Downloads/youtube-downloader/app.py):
```python
# Get CORS origins from environment variable, default to all origins
cors_origins = os.environ.get('CORS_ORIGINS', '*')
if cors_origins == '*':
    CORS(app)  # Enable CORS for all routes
else:
    origins = cors_origins.split(',')
    CORS(app, origins=origins)
```

## Using Environment Variables

### Local Development

Create a `.env` file in the project root:
```bash
PORT=5000
FLASK_DEBUG=True
DOWNLOADS_DIR=./downloads
CORS_ORIGINS=*
```

Then load it in [app.py](file:///c%3A/Users/mulac/Downloads/youtube-downloader/app.py):
```python
from dotenv import load_dotenv
load_dotenv()
```

### Render Deployment

In the Render dashboard:
1. Go to your service settings
2. Scroll to "Environment Variables"
3. Add variables as needed:
   - Key: `FLASK_DEBUG`, Value: `False`
   - Key: `DOWNLOADS_DIR`, Value: `/opt/render/downloads`

### Docker Deployment

Create a `.env` file and use it with Docker:
```bash
docker run -p 5000:5000 --env-file .env youtube-downloader
```

Or specify variables directly:
```bash
docker run -p 5000:5000 -e FLASK_DEBUG=True -e DOWNLOADS_DIR=/downloads youtube-downloader
```

## Security Considerations

1. **Never commit sensitive environment variables** to version control
2. **Use different variables for development and production**
3. **Validate environment variable values** before using them
4. **Provide sensible defaults** for all environment variables

## Best Practices

1. **Document all environment variables** in your README
2. **Use descriptive names** for environment variables
3. **Group related variables** with consistent naming (e.g., `YOUTUBE_DOWNLOADER_*`)
4. **Provide default values** for all environment variables
5. **Validate environment variable values** before using them

## Example Configuration

### Development Environment (.env file)
```bash
PORT=5000
FLASK_DEBUG=True
DOWNLOADS_DIR=./downloads
CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

### Production Environment (Render)
```bash
PORT=5000
FLASK_DEBUG=False
DOWNLOADS_DIR=/opt/render/downloads
CORS_ORIGINS=https://yourdomain.com
```

These environment variables will make your application more flexible and easier to configure across different deployment environments.