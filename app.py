import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import subprocess
import sys

app = Flask(__name__, static_folder='frontend/build')
CORS(app)  # Enable CORS for all routes

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and app.static_folder and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html') if app.static_folder else "Static folder not configured"

@app.route('/api/download', methods=['POST'])
def download_video():
    try:
        data = request.get_json()
        url = data.get('url')
        resolution = data.get('resolution', '720p')
        format_id = data.get('format', 'mp4')
        audio_only = data.get('audioOnly', False)
        audio_format = data.get('audioFormat', 'mp3')
        
        if not url:
            return jsonify({'error': 'URL is required'}), 400
        
        # Build command to call the youtube_downloader.py script
        cmd = [sys.executable, os.path.join(current_dir, 'youtube_downloader.py'), url]
        
        if audio_only:
            cmd.extend(['-a', '--audio-format', audio_format])
        else:
            cmd.extend(['-r', resolution, '-f', format_id])
        
        # Execute the command
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=current_dir)
        
        if result.returncode == 0:
            return jsonify({
                'success': True,
                'message': 'Download completed successfully!',
                'output': result.stdout
            })
        else:
            return jsonify({
                'success': False,
                'error': f'Download failed: {result.stderr}'
            }), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({'status': 'YouTube Downloader API is running'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', debug=False, port=port)