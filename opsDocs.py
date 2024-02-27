import os
from openpyxl import load_workbook
import requests
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to your service account credentials JSON file
credentials_file = 'C:/Users/lenovo/Desktop/docsProject/ops-do-ab53a8422146.json'

# Create credentials for Google Drive API
credentials = service_account.Credentials.from_service_account_file(
    credentials_file, scopes=['https://www.googleapis.com/auth/drive'])

# Build the Drive API service
drive_service = build('drive', 'v3', credentials=credentials)


# Define the path to your desktop folder
desktop_folder = os.path.expanduser("C:/Users/lenovo/Desktop/docsProject/ops_docs")
excel_file = 'C:/Users/lenovo/Desktop/docsProject/docs.xlsx'

# Load the Excel workbook
workbook = load_workbook(excel_file)
sheet = workbook.active

# Iterate over rows and columns to find photo URLs
for row_index, row in enumerate(sheet.iter_rows(min_row=2, max_row=sheet.max_row, min_col=1, max_col=sheet.max_column)):
    driver_id = row[0].value  #driver ID is in the first column
    
    for column_index, cell in enumerate(row[1:], start=2):  # Start from the second column
        photo_file_link = cell.value
        # Find the position of '/d/' and '/view' in the link
        start_index = photo_file_link.find('/d/') + 3
        end_index = photo_file_link.find('/view')

        # Extract the file ID using slicing
        photo_file_id = photo_file_link[start_index:end_index]
        
        if photo_file_id:
            photo_column_header = sheet.cell(row=1, column=column_index).value  # Get the column header
            filename = f"{driver_id} - {photo_column_header}.jpg"
            
            # Use the Drive API service to download the file
            request = drive_service.files().get_media(fileId=photo_file_id)
            file_content = request.execute()
            
            # Save the file content to the desktop folder
            with open(os.path.join(desktop_folder, filename), 'wb') as f:
                f.write(file_content)
                
            print(f"Downloaded {filename} to desktop folder.")

# Close the workbook after finishing
workbook.close()
