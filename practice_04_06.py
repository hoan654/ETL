
import pandas as pd
import requests

# ===== 1. Tải file enrollies_education.xlsx =====
excel_url = 'https://assets.swisscoding.edu.vn/company_course/enrollies_education.xlsx'
excel_filename = 'enrollies_education.xlsx'
excel_response = requests.get(excel_url)
with open(excel_filename, 'wb') as file:
    file.write(excel_response.content)

enrollies_education = pd.read_excel(excel_filename)
print("Enrollies Education:")
print(enrollies_education.head())

# ===== 2. Tải file work_experience.csv =====
csv_url = 'https://assets.swisscoding.edu.vn/company_course/work_experience.csv'
csv_filename = 'work_experience.csv'
csv_response = requests.get(csv_url)
with open(csv_filename, 'wb') as file:
    file.write(csv_response.content)

work_experience = pd.read_csv(csv_filename)
print("\nWork Experience:")
print(work_experience.head())

# ===== 3. Tải Google Sheet và đọc bằng pandas =====
google_sheet_id = '1VCkHWbJjGRJ21asd9pxW4_0z2PWuKhbLR3gUHm-p4GI'
gsheet_url = f'https://docs.google.com/spreadsheets/d/{google_sheet_id}/export?format=xlsx'
gsheet_filename = 'enrollies_google_sheet.xlsx'

gsheet_response = requests.get(gsheet_url)
with open(gsheet_filename, 'wb') as file:
    file.write(gsheet_response.content)

enrollies_data = pd.read_excel(gsheet_filename, sheet_name='enrolllies')
print("\nEnrollies Google Sheet:")
print(enrollies_data.head())
