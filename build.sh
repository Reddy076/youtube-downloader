#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Install Node.js and npm using nvm if not available
if ! command -v node &> /dev/null; then
    echo "Installing Node.js..."
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
    nvm install node
fi

# Install frontend dependencies and build
cd frontend
npm install
npm run build
cd ..

echo "Build completed successfully!"