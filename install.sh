#!/bin/bash

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Update pip, wheel and setuptools
pip install --upgrade pip wheel setuptools

# Install core dependencies without optional extras
pip install --no-deps streamlit==1.24.0
pip install openpyxl==3.1.2
pip install watchdog>=3.0.0
pip install pillow>=10.0.0

# Create a flag file to indicate installation is complete
touch venv/installed.flag

echo "Installation complete! Run './run.sh' to start the application." 