#!/bin/bash

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Update pip and install wheel if needed
pip install --upgrade pip wheel setuptools

# Install dependencies if needed
if [ ! -f "venv/installed.flag" ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
    touch venv/installed.flag
fi

# Run the Streamlit app
streamlit run app.py 