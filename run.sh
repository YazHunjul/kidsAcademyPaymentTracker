#!/bin/bash

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Running installation script..."
    bash ./install.sh
fi

# Activate virtual environment
source venv/bin/activate

# Run the Streamlit app
streamlit run app.py 