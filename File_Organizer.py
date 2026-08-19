
from pathlib import Path
import shutil

Document = [".docx"]
Application = [".exe"]
Subtitle = [".srt"]
Calendar = [".ics"]
Spreadsheet = [".csv"]

folder = Path(r"C:\Users\ADMIN\fake")
for item in folder.iterdir():
    if item.is_file():
        if item.suffix in Document:
            category = "Document"
        elif item.suffix in Application:
            category = "Application"
        elif item.suffix in Subtitle:
            category = "Subtitle"
        elif item.suffix in Calendar:
            category = "Calendar"
        elif item.suffix in Spreadsheet:
            category = "Spreadsheet"
        else:
            category = "Other"
        Destination = folder/category
        Destination.mkdir(exist_ok=True)
        new_location = Destination/item.name
        shutil.move(str(item), str(new_location))
    
