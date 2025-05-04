# Student Payment Tracker

A Streamlit application to track student payments and store them in an Excel file.

## Features

- Enter student name, payment amount, and date
- Data is saved in an Excel file (`student_payments.xlsx`)
- View all payment records in a table
- Download the Excel file directly from the app
- Data starts at row 15 in the Excel file to allow space for headers, logos, etc.

## Installation

### Option 1: Using Virtual Environment (Recommended)

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

3. Install wheel and setuptools first for faster dependency installation:

   ```
   pip install --upgrade pip wheel setuptools
   ```

4. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

   Or install directly from the setup.py:

   ```
   pip install -e .
   ```

5. Install watchdog for better performance (optional):

   ```
   pip install watchdog
   ```

6. Run the application:

   ```
   streamlit run app.py
   ```

   Or use the provided script:

   ```
   ./run.sh
   ```

### Option 2: Direct Installation

1. Install wheel for faster dependency installation:

   ```
   pip install --upgrade pip wheel setuptools
   ```

2. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

3. Run the application:
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
- Streamlit 1.24.0
- Pandas 2.0.3
- OpenPyXL 3.1.2
- Watchdog (recommended for better performance)
- Wheel (for faster package installation)
