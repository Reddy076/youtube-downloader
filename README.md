# YouTube Video Downloader with yt-dlp Integration

A command-line based YouTube Video Downloader that integrates with yt-dlp to allow users to download videos from YouTube in various formats and resolutions.

## Features

- **Download YouTube Videos**: Download videos in various resolutions (360p, 720p, 1080p, etc.)
- **Audio Extraction**: Extract and download only the audio from a YouTube video
- **Multiple Formats**: Support for multiple video formats like MP4, WebM, and audio formats like MP3, M4A
- **Batch Downloading**: Download multiple videos at once by providing a list of URLs
- **Simple Command-Line Interface**: Easy-to-use command-line input for seamless user experience

## Requirements

- Python 3.6 or higher
- yt-dlp package

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/YouTube-Video-Downloader.git
   cd YouTube-Video-Downloader
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

To download a YouTube video in the default format (720p MP4):

```bash
python youtube_downloader.py https://www.youtube.com/watch?v=VIDEO_ID
```

### Specify Resolution and Format

```bash
python youtube_downloader.py https://www.youtube.com/watch?v=VIDEO_ID -r 1080p -f mp4
```

### Extract Audio Only

```bash
python youtube_downloader.py https://www.youtube.com/watch?v=VIDEO_ID -a --audio-format mp3
```

### Batch Download Multiple Videos

```bash
python youtube_downloader.py https://www.youtube.com/watch?v=VIDEO_ID1 https://www.youtube.com/watch?v=VIDEO_ID2
```

### Change Output Directory

```bash
python youtube_downloader.py https://www.youtube.com/watch?v=VIDEO_ID -o /path/to/output/directory
```

## Command-Line Options

- `urls`: YouTube video URL(s) to download
- `-o, --output-dir`: Directory to save downloaded files (default: downloads)
- `-r, --resolution`: Video resolution (e.g., 360p, 720p, 1080p, best) (default: 720p)
- `-f, --format`: Video format (e.g., mp4, webm) (default: mp4)
- `-a, --audio-only`: Extract audio only
- `--audio-format`: Audio format when using --audio-only (e.g., mp3, m4a) (default: mp3)

## Examples

1. Download a video in best quality:
   ```bash
   python youtube_downloader.py https://www.youtube.com/watch?v=VIDEO_ID -r best
   ```

2. Download multiple videos in 480p WebM format:
   ```bash
   python youtube_downloader.py https://www.youtube.com/watch?v=VIDEO_ID1 https://www.youtube.com/watch?v=VIDEO_ID2 -r 480p -f webm
   ```

3. Extract audio from multiple videos in M4A format:
   ```bash
   python youtube_downloader.py https://www.youtube.com/watch?v=VIDEO_ID1 https://www.youtube.com/watch?v=VIDEO_ID2 -a --audio-format m4a
   ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - The powerful downloader that this tool is built upon