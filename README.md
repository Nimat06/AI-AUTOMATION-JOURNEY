# AI-AUTOMATION-JOURNEY
This repo tracks my learning journey.

## calculator.py

A simple calculator that does +, -, *, / on two numbers. Has error handling 
built in so it doesn't crash on invalid operations or division by zero — 
just returns a message instead.

Example: `calculator(10, 2, "/")` → `5.0`

## file_organizer.py

It scans a folder and sorts files into subfolders based on their file type — 
documents, applications, subtitles, calendars, spreadsheets, and anything 
else goes into "Other". Useful for cleaning up a messy downloads folder.

**Tools used:** pathlib, shutil

## excel_report_generator.py : part 1

It reads production data and turns it into a summary report. Groups the data 
by Production Line and by Shift, then calculates sum/mean/min/max for 
defective units, and writes it all into one Excel file with separate 
sheets for each summary.

Input: production_data.xlsx
Output: Full_report.xlsx

**Tools used:** pandas, openpyxl


## data_cleaning.py

It takes messy production data and actually cleans it up — fills in missing 
values, fixes inconsistent text (like "line a" vs "LINE A " all becoming 
"Line A"), sorts out mixed date formats, and drops duplicate rows.

Standardized the text using `.str.strip()` (removes extra spaces) and 
`.str.title()` (fixes capitalization).

Input: dirty_production_data.xlsx
Output: Cleaned_Production_Data.xlsx — went from 156 rows down to 150 after removing duplicates


**Tools used:** pandas, openpyxl


## email_report_system.py

It reads production data, generates a summary report, and automatically emails it 
framed as a daily production report sent to a recipient.

**What it does:**
- Reads production data from Excel into a DataFrame
- Groups by `Production_Line` and `Shift`, calculating sum/mean/min/max of `Defective_Units`
- Formats both summaries into a plain-text report
- Sends the report via Gmail (using `smtplib` + an App Password) to a specified recipient

**Input:** `production_data.xlsx`
**Output:** an emailed report 

**Tools used:** pandas, smtplib, email.message


## production_report_automation.py

This one pulls together everything I built this week. It takes messy 
production data, cleans it up, summarizes it, makes a couple of charts, 
and then emails the whole thing out as a report — no manual work needed 
once it's running.

Reads dirty_production_data.xlsx → cleans missing values/text/dates → 
groups by line and shift → charts average units produced → builds a 
multi-sheet Excel file → emails it with the file attached.

**Tools used:** pandas, matplotlib, openpyxl, smtplib


