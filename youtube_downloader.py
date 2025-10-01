#!/usr/bin/env python3

import argparse
import os
import sys
from typing import List, Optional

try:
    import yt_dlp
except ImportError:
    print("Error: yt-dlp is not installed. Please install it using 'pip install yt-dlp'")
    sys.exit(1)


class YouTubeDownloader:
    """A command-line YouTube video downloader using yt-dlp."""

    def __init__(self, output_dir: str = "downloads"):
        """Initialize the YouTube downloader.

        Args:
            output_dir: Directory where downloaded files will be saved
        """
        self.output_dir = output_dir
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

    def download_video(self, url: str, resolution: str = "720p", format_id: str = "mp4") -> None:
        """Download a YouTube video.

        Args:
            url: YouTube video URL
            resolution: Video resolution (e.g., 360p, 720p, 1080p)
            format_id: Video format (e.g., mp4, webm)
        """
        print(f"Downloading video: {url}")
        print(f"Resolution: {resolution}, Format: {format_id}")

        # Convert resolution to format string
        if resolution == "best":
            # Try merged format first, fall back to single format if ffmpeg is not available
            format_string = f"bestvideo[ext={format_id}]+bestaudio[ext=m4a]/best[ext={format_id}]"
        else:
            # Remove 'p' from resolution (e.g., 720p -> 720)
            height = resolution.rstrip("p")
            # Try merged format first, fall back to single format if ffmpeg is not available
            format_string = f"bestvideo[height<={height}][ext={format_id}]+bestaudio[ext=m4a]/best[height<={height}][ext={format_id}]/best[ext={format_id}]"

        ydl_opts = {
            'format': format_string,
            'outtmpl': os.path.join(self.output_dir, '%(title)s.%(ext)s'),
            'noplaylist': True,
            'progress_hooks': [self._progress_hook],
            'merge_output_format': format_id,  # Specify output format for merged files
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print("Download completed successfully!")
        except yt_dlp.DownloadError as e:
            if "ffmpeg" in str(e).lower():
                print("Warning: ffmpeg not found. Trying single format download...")
                # Fallback to single format when ffmpeg is not available
                if resolution == "best":
                    format_string = f"best[ext={format_id}]"
                else:
                    height = resolution.rstrip("p")
                    format_string = f"best[height<={height}][ext={format_id}]"
                
                ydl_opts['format'] = format_string
                try:
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                    print("Download completed successfully!")
                except Exception as e2:
                    print(f"Error downloading video: {e2}")
            else:
                print(f"Error downloading video: {e}")
        except Exception as e:
            print(f"Error downloading video: {e}")

    def extract_audio(self, url: str, audio_format: str = "mp3") -> None:
        """Extract audio from a YouTube video.

        Args:
            url: YouTube video URL
            audio_format: Audio format (e.g., mp3, m4a)
        """
        print(f"Extracting audio from: {url}")
        print(f"Audio format: {audio_format}")

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': audio_format,
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(self.output_dir, '%(title)s.%(ext)s'),
            'progress_hooks': [self._progress_hook],
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print("Audio extraction completed successfully!")
        except yt_dlp.DownloadError as e:
            if "ffmpeg" in str(e).lower():
                print("Warning: ffmpeg not found. Trying to download audio without post-processing...")
                # Fallback to simple audio download when ffmpeg is not available
                ydl_opts.pop('postprocessors', None)
                ydl_opts['format'] = 'bestaudio[ext=m4a]/bestaudio/best'
                try:
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                    print("Audio download completed successfully!")
                except Exception as e2:
                    print(f"Error downloading audio: {e2}")
            else:
                print(f"Error extracting audio: {e}")
        except Exception as e:
            print(f"Error extracting audio: {e}")

    def batch_download(self, urls: List[str], resolution: str = "720p", format_id: str = "mp4", audio_only: bool = False) -> None:
        """Download multiple YouTube videos.

        Args:
            urls: List of YouTube video URLs
            resolution: Video resolution (e.g., 360p, 720p, 1080p)
            format_id: Video format (e.g., mp4, webm)
            audio_only: If True, extract audio only
        """
        print(f"Batch downloading {len(urls)} videos")

        for i, url in enumerate(urls, 1):
            print(f"\nProcessing video {i}/{len(urls)}")
            if audio_only:
                self.extract_audio(url)
            else:
                self.download_video(url, resolution, format_id)

    def _progress_hook(self, d: dict) -> None:
        """Progress hook for yt-dlp.

        Args:
            d: Progress information dictionary
        """
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', 'N/A')
            speed = d.get('_speed_str', 'N/A')
            eta = d.get('_eta_str', 'N/A')
            print(f"\rDownloading... {percent} at {speed} ETA: {eta}", end='', flush=True)
        elif d['status'] == 'finished':
            print("\nDownload finished, now converting...")


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments.

    Returns:
        Parsed arguments
    """
    parser = argparse.ArgumentParser(description="YouTube Video Downloader with yt-dlp")
    parser.add_argument(
        "urls", nargs="+", help="YouTube video URL(s) to download"
    )
    parser.add_argument(
        "-o", "--output-dir", default="downloads",
        help="Directory to save downloaded files (default: downloads)"
    )
    parser.add_argument(
        "-r", "--resolution", default="720p",
        help="Video resolution (e.g., 360p, 720p, 1080p, best) (default: 720p)"
    )
    parser.add_argument(
        "-f", "--format", default="mp4",
        help="Video format (e.g., mp4, webm) (default: mp4)"
    )
    parser.add_argument(
        "-a", "--audio-only", action="store_true",
        help="Extract audio only"
    )
    parser.add_argument(
        "--audio-format", default="mp3",
        help="Audio format when using --audio-only (e.g., mp3, m4a) (default: mp3)"
    )

    return parser.parse_args()


def main() -> None:
    """Main function."""
    args = parse_arguments()
    downloader = YouTubeDownloader(args.output_dir)

    if len(args.urls) == 1:
        # Single video download
        if args.audio_only:
            downloader.extract_audio(args.urls[0], args.audio_format)
        else:
            downloader.download_video(args.urls[0], args.resolution, args.format)
    else:
        # Batch download
        downloader.batch_download(args.urls, args.resolution, args.format, args.audio_only)


if __name__ == "__main__":
    main()