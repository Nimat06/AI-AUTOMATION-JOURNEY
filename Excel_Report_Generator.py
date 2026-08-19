
import pandas as pd 
df = pd.read_excel(r"C:\Users\ADMIN\Downloads\production_data.xlsx")
shift_summary = df.groupby("Shift")["Defective_Units"].agg(["sum","mean","min","max"])
line_summary = df.groupby("Production_Line")["Defective_Units"].agg(["sum","mean","min","max"])

with pd.ExcelWriter("Full_report.xlsx") as writer:
    line_summary.to_excel(writer, sheet_name = "By_Line")
    shift_summary.to_excel(writer, sheet_name = "By_Shift")
