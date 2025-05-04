# Student Payment Tracker

A Streamlit application to track student payments and store them in an Excel file.

## Features

- Enter student name, payment amount, and date
- Data is saved in an Excel file (`student_payments.xlsx`)
- View all payment records in a table
- Download the Excel file directly from the app

## Installation

1. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

2. Run the application:
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
- Streamlit
- Pandas
- OpenPyXL
