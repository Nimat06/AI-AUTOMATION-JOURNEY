# AI-AUTOMATION-JOURNEY
This repo tracks my learning journey.

## calculator.py

A simple calculator that performs +, -, *, / on two numbers, with error handling for invalid operations and division by zero.

**Example:**
result = calculator(10, 2, "/")
print(result) # 5.0



## file_organizer.py

This is a file organizer that basically scans a folder and automatically sorts files into subfolders based on file type 
(Document, Application, Subtitle, Calendar, Spreadsheet, Other).

**Example:** running the script on a folder full of mixed files (.docx, .exe, .srt, .csv, etc.) 
automatically creates category subfolders and moves each file into the right one.

## Tools used

Python standard library only — `pathlib`, `shutil` (file organizer).

## excel_report_generator.py : part 1

It reads production data and generates a multi-sheet Excel summary report-
grouped statistics (sum, mean, min, max) by Production Line and by Shift.

**What it does:**
- Reads raw production data from Excel into a DataFrame
- Groups by `Production_Line` and calculates sum/mean/min/max of `Defective_Units`
- Groups by `Shift` and calculates the same stats
- Writes both summaries into one Excel file, each on its own sheet (`By_Line`, `By_Shift`)

**Input:** `production_data.xlsx`
**Output:** `Full_report.xlsx` — multi-sheet summary report

**Tools used:** pandas, openpyxl

