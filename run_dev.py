#!/usr/bin/env python3
"""
Script to run both the backend API and frontend development server simultaneously.
"""

import subprocess
import sys
import os
import signal

# Global variables to keep track of processes
processes = []

def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully by terminating all subprocesses."""
    print("\nShutting down development servers...")
    for process in processes:
        try:
            process.terminate()
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
        except Exception as e:
            print(f"Error terminating process: {e}")
    sys.exit(0)

def run_backend():
    """Start the Flask backend server."""
    print("Starting Flask backend server...")
    backend = subprocess.Popen([sys.executable, "app.py"])
    processes.append(backend)
    return backend

def run_frontend():
    """Start the React frontend development server."""
    print("Starting React frontend development server...")
    frontend = subprocess.Popen(["npm", "start"], cwd="frontend")
    processes.append(frontend)
    return frontend

def main():
    """Main function to start both servers."""
    # Set up signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    
    try:
        # Start both servers
        backend_process = run_backend()
        frontend_process = run_frontend()
        
        print("\nDevelopment servers started successfully!")
        print("Backend API: http://localhost:5000")
        print("Frontend: http://localhost:3000")
        print("Press Ctrl+C to stop both servers.\n")
        
        # Wait for both processes
        while True:
            try:
                # Check if any process has terminated
                if backend_process.poll() is not None:
                    print("Backend process terminated unexpectedly")
                    break
                if frontend_process.poll() is not None:
                    print("Frontend process terminated unexpectedly")
                    break
            except Exception as e:
                print(f"Error checking processes: {e}")
                break
            
            # Small delay to prevent busy waiting
            signal.pause()
            
    except Exception as e:
        print(f"Error starting development servers: {e}")
    finally:
        signal_handler(signal.SIGINT, None)

if __name__ == "__main__":
    main()