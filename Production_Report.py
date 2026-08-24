
import pandas as pd 
df = pd.read_excel(r"C:\Users\ADMIN\Downloads\production_data.xlsx")
line_summary = df.groupby("Production_Line")["Defective_Units"].agg(["sum", "mean","min", "max"])
shift_summary = df.groupby("Shift")["Defective_Units"].agg(["sum","mean","min","max"])

report_text = f"""

DAILY PRODUCTION REPORT

--- Summary by Production_Line ---
{line_summary.to_string()}

--- Summary by Shift ---
{shift_summary.to_string()}

"""

import smtplib
from email.message import EmailMessage

message = EmailMessage()

sender_email = "***********S"
receiver_email = "***********"
password = "*******"

message["Subject"] = "Daily Prodution Report"
message["From"] = sender_email
message["To"] = receiver_email

message.set_content(report_text)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(sender_email, password)
    smtp.send_message(message)


print("Email Sent!")


