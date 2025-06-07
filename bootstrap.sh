#!/bin/zsh

# Checking if .venv exist
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv .venv
fi

# Activating .venv
echo "Activating virtual environment..."
source .venv/bin/activate

# Installing requirements.txt if exist
if [ -f "requirements.txt" ]; then
  echo "Installing dependencies..."
  pip install -r requirements.txt
fi

# Check if playwright is installed, if not install it and run playwright install
if ! python -c "import playwright" &> /dev/null; then
  echo "Installing playwright..."
  pip install playwright
  playwright install
else
  echo "Playwright is already installed."
fi