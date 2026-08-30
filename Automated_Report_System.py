 


import pandas as pd 

df = pd.read_excel(r"C:\Users\ADMIN\Downloads\dirty_production_data.xlsx")

df["Shift"] = df["Shift"].fillna("Unknown")
df["Units_Produced"] = df["Units_Produced"].fillna(df["Units_Produced"].mean())
df["Defect_Rate_%"] = df["Defect_Rate_%"].fillna(df["Defect_Rate_%"].mean())
df["Downtime_Minutes"] = df["Downtime_Minutes"].fillna(0)

df["Production_Line"] = df["Production_Line"].str.strip().str.title()
df["Shift"] = df["Shift"].str.strip().str.title()

df["Date"] = pd.to_datetime(df["Date"], format = "mixed")

df = df.drop_duplicates()

line_summary = df.groupby("Production_Line")["Units_Produced"].describe()
shift_summary = df.groupby("Shift")["Units_Produced"].describe()

import matplotlib.pyplot as plt

plt.bar(line_summary.index, line_summary["mean"])
plt.title("Average Units Produced By Line")
plt.xlabel("Production Line")
plt.ylabel("Average Unit Produced")
plt.savefig("Line_chart.png")
plt.show()

plt.clf()

plt.bar(shift_summary.index, shift_summary["mean"])
plt.title("Average Units Produced By Shift")
plt.ylabel("Average Units Produced")
plt.xlabel("Shift")
plt.savefig("Shift_chart.png")
plt.show()

import pandas as pd
from openpyxl.drawing.image import Image

with pd.ExcelWriter("Production_Report.xlsx", engine = "openpyxl") as writer:
    line_summary.to_excel(writer, sheet_name= "By Line")
    shift_summary.to_excel(writer, sheet_name= "By Shift")

    workbook = writer.book
    chart_sheet = workbook.create_sheet("Chart")

    img1 = Image("Line_chart.png")
    chart_sheet.add_image(img1, "A1")

    img2 = Image("Shift_chart.png")
    chart_sheet.add_image(img2, "A20")


import smtplib
from email.message import EmailMessage

message = EmailMessage()

sender_email = "***********"
receiver_email = "**********"
password = "**************"

message["Subject"] = "Automated Daily Production Report"
message["From"] = sender_email
message["To"] = receiver_email

message.set_content("""
Hello,

Please find attached today's production report. 

If you have any questions, feel free to reach out.

Regards,
Automated Report Team.
""")

with open("Production_Report.xlsx", "rb") as file:
    file_data = file.read()
    file_name = "Production_Report.xlsx"

message.add_attachment(file_data, maintype = "application", subtype = "octet-stream",filename = file_name)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(sender_email, password)
    smtp.send_message(message)


print("Email sent!")


