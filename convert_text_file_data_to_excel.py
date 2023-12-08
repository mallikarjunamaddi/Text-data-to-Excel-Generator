#Run the following command: pip install openpyxl
import csv
from openpyxl import Workbook 

# Create a new workbook and select the active sheet
wb = Workbook()
ws = wb.active

# Open the text file and read the data
with open('inputData.txt', 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        ws.append(row)

# Save the data to an Excel file
wb.save('outputData.xlsx')

print("---------------------Excel sheet is ready.-------------------")