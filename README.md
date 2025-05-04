# Student Payment Tracker

A Streamlit application to track student payments and store them in an Excel file.

## Features

- Enter student name, payment amount, and date
- Data is saved in an Excel file
- View all payment records in a table
- Download the Excel file directly from the app
- Data starts at row 15 in the Excel file to allow space for headers, logos, etc.

## Installation

### Quick Installation (Recommended)

Use the provided installation script:

```
./install.sh
```

This will:

1. Create a virtual environment
2. Install all required dependencies
3. Set up everything needed to run the application

After installation, run the app with:

```
./run.sh
```

### Manual Installation

1. Create a virtual environment:

   ```
   python -m venv venv
   ```

2. Activate the virtual environment:

   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
   - On Windows:
     ```
     venv\Scripts\activate
     ```

3. Install dependencies:

   ```
   pip install --upgrade pip wheel setuptools
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   streamlit run app.py
   ```

## Usage

1. Enter the student name, payment amount, and date in the form
2. Click "Submit Payment" to save the data
3. The payment record will appear in the table below
4. Use the "Download Excel File" button to download the Excel file

## Requirements

- Python 3.7+
- Streamlit 1.28.0+
- OpenPyXL 3.1.2
- Pillow 10.0.0+
- Watchdog (for better performance)
- Wheel (for faster package installation)
