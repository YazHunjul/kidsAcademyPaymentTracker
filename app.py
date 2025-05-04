import streamlit as st
from datetime import date
import os
import openpyxl
import shutil
from datetime import datetime
from openpyxl.styles import Alignment, PatternFill, Font, Border, Side

# Set page title and configuration
st.set_page_config(page_title="Student Payment Tracker", layout="wide")
st.title("Student Payment Tracker")

# Define file paths
template_file = "resources/Student Payment Tracker.xlsx"
output_dir = "output"

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to write data to Excel while preserving template formatting
def write_excel_file(file_path, student_data):
    # Define the header row - start at row 15 as requested
    HEADER_ROW = 15
    
    # Check if template exists to preserve its formatting
    if os.path.exists(template_file):
        # Make a copy of the template to preserve logos and formatting
        shutil.copy(template_file, file_path)
        # Open the copied template
        wb = openpyxl.load_workbook(file_path)
        ws = wb.active
    else:
        # If template doesn't exist, create a new workbook
        wb = openpyxl.Workbook()
        ws = wb.active
    
    # ALWAYS write the column headers starting at row 15
    # Set up headers with each column taking two columns
    # Student Name: A15:B15, Payment Amount: C15:D15, Payment Date: E15:F15
    try:
        # Attempt to unmerge first in case they are already merged
        try:
            ws.unmerge_cells(f'A{HEADER_ROW}:B{HEADER_ROW}')
        except:
            pass
        ws.merge_cells(f'A{HEADER_ROW}:B{HEADER_ROW}')
        header_cell = ws.cell(row=HEADER_ROW, column=1)
        header_cell.value = "Student Name"
        header_cell.alignment = Alignment(horizontal='center', vertical='center')
        header_cell.font = Font(bold=True)
        
        try:
            ws.unmerge_cells(f'C{HEADER_ROW}:D{HEADER_ROW}')
        except:
            pass
        ws.merge_cells(f'C{HEADER_ROW}:D{HEADER_ROW}')
        header_cell = ws.cell(row=HEADER_ROW, column=3)
        header_cell.value = "Payment Amount"
        header_cell.alignment = Alignment(horizontal='center', vertical='center')
        header_cell.font = Font(bold=True)
        
        try:
            ws.unmerge_cells(f'E{HEADER_ROW}:F{HEADER_ROW}')
        except:
            pass
        ws.merge_cells(f'E{HEADER_ROW}:F{HEADER_ROW}')
        header_cell = ws.cell(row=HEADER_ROW, column=5)
        header_cell.value = "Payment Date"
        header_cell.alignment = Alignment(horizontal='center', vertical='center')
        header_cell.font = Font(bold=True)
    except Exception as e:
        st.warning(f"Could not set headers: {str(e)}")
    
    # Define cell styling for centering
    center_alignment = Alignment(horizontal='center', vertical='center')
    
    # Define color fills for alternating rows
    # Range of light colors for better readability
    colors = [
        "FFD6E0", "FFE8D6", "D6EAD6", "D6E0EA", "E0D6EA", 
        "EAD6E0", "EAE0D6", "E0EAD6", "D6EAEA", "E0D6EA"
    ]
    
    # Set column widths if not using template
    if not os.path.exists(template_file):
        for col in "ABCDEF":
            ws.column_dimensions[col].width = 15
    
    # Start filling data from one row after the header
    start_row = HEADER_ROW + 1
    
    # Calculate total payment amount
    total_payment = 0.0
    
    # Fill in data, making each value occupy two columns
    for row_idx, row_data in enumerate(student_data, start=start_row):
        # Set row color
        color_idx = (row_idx - start_row) % len(colors)
        row_fill = PatternFill(start_color=colors[color_idx], end_color=colors[color_idx], fill_type="solid")
        
        try:
            # Student Name in A and B (ensure title case)
            # Always merge these cells regardless of existing content
            try:
                ws.merge_cells(f'A{row_idx}:B{row_idx}')
            except:
                # If cells are already merged, unmerge and then merge again
                try:
                    ws.unmerge_cells(f'A{row_idx}:B{row_idx}')
                    ws.merge_cells(f'A{row_idx}:B{row_idx}')
                except:
                    pass  # If this fails too, just proceed
                
            cell = ws.cell(row=row_idx, column=1)
            student_name_val = str(row_data["Student Name"]).title() if row_data["Student Name"] is not None else ""
            cell.value = student_name_val
            cell.alignment = center_alignment
            cell.fill = row_fill
        
            # Payment Amount in C and D - add AED prefix
            try:
                ws.merge_cells(f'C{row_idx}:D{row_idx}')
            except:
                try:
                    ws.unmerge_cells(f'C{row_idx}:D{row_idx}')
                    ws.merge_cells(f'C{row_idx}:D{row_idx}')
                except:
                    pass
                
            cell = ws.cell(row=row_idx, column=3)
            # Handle the payment amount appropriately
            amount_value = row_data["Payment Amount"]  # Payment Amount
            
            # Try to convert to float for accumulating the total
            try:
                if amount_value is not None and str(amount_value).strip() != "":
                    numeric_amount = float(amount_value)
                    total_payment += numeric_amount
                    cell.value = f"AED {numeric_amount:.2f}"
                else:
                    cell.value = "AED 0.00"
            except (ValueError, TypeError):
                cell.value = f"AED {amount_value}"
            
            cell.alignment = center_alignment
            cell.fill = row_fill
            
            # Payment Date in E and F
            try:
                ws.merge_cells(f'E{row_idx}:F{row_idx}')
            except:
                try:
                    ws.unmerge_cells(f'E{row_idx}:F{row_idx}')
                    ws.merge_cells(f'E{row_idx}:F{row_idx}')
                except:
                    pass
                
            cell = ws.cell(row=row_idx, column=5)
            date_val = str(row_data["Payment Date"]) if row_data["Payment Date"] is not None else ""
            cell.value = date_val
            cell.alignment = center_alignment
            cell.fill = row_fill
        except Exception as e:
            st.error(f"Error writing row {row_idx}: {str(e)}")
            continue  # Skip this row if there's an error
    
    # Add a total row ONLY after the last student
    total_row = len(student_data) + start_row  # +start_row to account for headers
    
    # "Total" label in columns A and B
    try:
        ws.merge_cells(f'A{total_row}:B{total_row}')
    except:
        try:
            ws.unmerge_cells(f'A{total_row}:B{total_row}')
            ws.merge_cells(f'A{total_row}:B{total_row}')
        except:
            pass
            
    cell = ws.cell(row=total_row, column=1)
    cell.value = "Total"
    cell.alignment = center_alignment
    cell.font = Font(bold=True)
    
    # Total amount in columns C and D
    try:
        ws.merge_cells(f'C{total_row}:D{total_row}')
    except:
        try:
            ws.unmerge_cells(f'C{total_row}:D{total_row}')
            ws.merge_cells(f'C{total_row}:D{total_row}')
        except:
            pass
            
    cell = ws.cell(row=total_row, column=3)
    cell.value = f"AED {total_payment:.2f}"
    cell.alignment = center_alignment
    cell.font = Font(bold=True)
    
    # Empty cell in columns E and F
    try:
        ws.merge_cells(f'E{total_row}:F{total_row}')
    except:
        try:
            ws.unmerge_cells(f'E{total_row}:F{total_row}')
            ws.merge_cells(f'E{total_row}:F{total_row}')
        except:
            pass
    
    # Save the workbook
    try:
        wb.save(file_path)
    except Exception as e:
        st.error(f"Error saving workbook: {str(e)}")

# Function to read data from Excel file
def read_excel_file(file_path):
    student_data = []
    if not os.path.exists(file_path):
        return student_data
    
    try:
        wb = openpyxl.load_workbook(file_path)
        ws = wb.active
        
        # Find where the data starts - row 16 (after header at row 15)
        data_start_row = 16
        
        # Read rows until we find an empty row or "Total"
        row = data_start_row
        while True:
            student_name = ws.cell(row=row, column=1).value
            
            # Stop if we hit an empty row or "Total"
            if not student_name or (isinstance(student_name, str) and student_name.lower() == "total"):
                break
                
            payment_cell = ws.cell(row=row, column=3).value
            payment_amount = 0.0
            
            # Try to extract numeric value from payment cell
            if payment_cell:
                try:
                    # Remove "AED" and convert to float
                    payment_str = str(payment_cell).replace("AED", "").strip()
                    payment_amount = float(payment_str) if payment_str else 0.0
                except (ValueError, TypeError):
                    payment_amount = 0.0
            
            payment_date = ws.cell(row=row, column=5).value
            payment_date_str = str(payment_date) if payment_date else ""
            
            # Add to our data collection
            student_data.append({
                "Student Name": student_name,
                "Payment Amount": payment_amount,
                "Payment Date": payment_date_str
            })
            
            row += 1
    except Exception as e:
        st.warning(f"Could not read data from template: {str(e)}")
    
    return student_data

# Make sure we're using a fresh session state with no pandas objects
if 'student_data' in st.session_state:
    # Check if student_data is a pandas DataFrame (from a previous run)
    # If so, convert it to a list of dictionaries
    if hasattr(st.session_state.student_data, 'to_dict'):
        try:
            # Convert pandas DataFrame to list of dictionaries
            pandas_data = st.session_state.student_data
            records = pandas_data.to_dict('records')
            st.session_state.student_data = records
        except Exception as e:
            # If conversion fails, start with an empty list
            st.warning(f"Resetting data due to format change: {str(e)}")
            st.session_state.student_data = []
elif 'student_data' not in st.session_state:
    # Initialize with empty list if not present
    st.session_state.student_data = []

# Generate a unique filename for this session
if 'current_file' not in st.session_state:
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    excel_file = f"{output_dir}/Student_Payment_Tracker_{current_time}.xlsx"
    st.session_state.current_file = excel_file
else:
    excel_file = st.session_state.current_file

# Load data if needed - using len() is safer than direct boolean check
if len(st.session_state.student_data) == 0 and os.path.exists(template_file):
    # Try to read from template if it exists
    student_data = read_excel_file(template_file)
    if student_data:
        st.session_state.student_data = student_data

# Display current file being used
st.info(f"Working with file: {os.path.basename(excel_file)}")

# Create form for data entry
with st.form("payment_form", clear_on_submit=True):
    st.subheader("Enter Payment Information")
    
    # Create two columns for the form layout
    col1, col2 = st.columns(2)
    
    # Input fields in columns
    with col1:
        student_name = st.text_input("Student Name")
    
    with col2:
        payment_amount = st.number_input("Payment Amount (AED)", min_value=0.0, step=0.01, format="%.2f")
    
    # Date picker in its own row spanning two columns
    payment_date = st.date_input("Payment Date", value=date.today())
    
    # Submit button
    submitted = st.form_submit_button("Submit Payment")
    
    if submitted:
        if not student_name:  # Validate student name is not empty
            st.error("Please enter a student name")
        else:
            # Format student name in title case (capitalize first letter of each word)
            formatted_name = student_name.title()
            
            # Format date as YYYY-MM-DD string
            formatted_date = payment_date.strftime('%Y-%m-%d')
            
            # Add new data
            new_data = {
                "Student Name": formatted_name,
                "Payment Amount": payment_amount,
                "Payment Date": formatted_date
            }
            
            # Append to the session state data
            st.session_state.student_data.append(new_data)
            
            # Write the Excel file with all entries
            write_excel_file(excel_file, st.session_state.student_data)
            
            st.success(f"Payment of AED {payment_amount:.2f} for {formatted_name} has been recorded!")

# Display existing data
st.subheader("Payment Records")
if len(st.session_state.student_data) > 0:
    # Create a display version of the data
    display_data = []
    total_amount = 0.0
    
    for entry in st.session_state.student_data:
        # Format student name in title case
        name = str(entry["Student Name"]).title() if entry["Student Name"] else ""
        
        # Format payment amount
        try:
            amount = float(entry["Payment Amount"]) if entry["Payment Amount"] is not None else 0.0
            total_amount += amount
            formatted_amount = f"AED {amount:.2f}"
        except (ValueError, TypeError):
            formatted_amount = f"AED {entry['Payment Amount']}" if entry["Payment Amount"] else "AED 0.00"
        
        # Add to display data
        display_data.append({
            "Student Name": name,
            "Payment Amount": formatted_amount,
            "Payment Date": entry["Payment Date"]
        })
    
    # Show the data in a Streamlit table
    st.dataframe(
        display_data,
        column_config={
            "Student Name": st.column_config.TextColumn("Student Name", width="large"),
            "Payment Amount": st.column_config.TextColumn("Payment Amount", width="medium"),
            "Payment Date": st.column_config.TextColumn("Payment Date", width="medium"),
        },
        use_container_width=True
    )
    
    # Display the total
    st.info(f"Total Amount: AED {total_amount:.2f}")
else:
    st.info("No payment records found. Add a payment to get started!")

# Add download button for the Excel file
if os.path.exists(excel_file):
    with open(excel_file, "rb") as file:
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        st.download_button(
            label="Download Excel File",
            data=file,
            file_name=f"Student_Payment_Tracker_{current_time}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        ) 