import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
import os

# 1️⃣ Read Excel file
df = pd.read_excel("invoices.xlsx")

# 2️⃣ Create folder for invoices
output_folder = "Generated_Invoices"
os.makedirs(output_folder, exist_ok=True)

# 3️⃣ Group by Invoice Number
grouped = df.groupby("Invoice Number")

# 4️⃣ Loop through each invoice
for invoice_number, data in grouped:
    customer_name = data.iloc[0]["Customer Name"]
    invoice_date = data.iloc[0]["Invoice Date"]

    # File path
    file_name = f"Invoice_{invoice_number}.pdf"
    file_path = os.path.join(output_folder, file_name)

    # Create PDF
    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    # --- Company Logo ---
    try:
        c.drawImage("logo.png", 20*mm, height - 40*mm, width=40*mm, preserveAspectRatio=True, mask='auto')
    except:
        print("⚠ Logo not found, skipping logo.")

    # --- Company Info ---
    c.setFont("Helvetica-Bold", 14)
    c.drawString(70*mm, height - 20*mm, "Your Company Name")
    c.setFont("Helvetica", 10)
    c.drawString(70*mm, height - 25*mm, "123 Business Street, City, Country")
    c.drawString(70*mm, height - 30*mm, "Email: your@email.com | Phone: +123 456 7890")

    # --- Invoice Title ---
    c.setFont("Helvetica-Bold", 20)
    c.drawString(20*mm, height - 50*mm, "INVOICE")

    # --- Invoice Details ---
    c.setFont("Helvetica", 10)
    c.drawString(20*mm, height - 60*mm, f"Invoice Number: {invoice_number}")
    c.drawString(20*mm, height - 65*mm, f"Date: {invoice_date}")

    # --- Bill To ---
    c.setFont("Helvetica-Bold", 12)
    c.drawString(20*mm, height - 80*mm, "Bill To:")
    c.setFont("Helvetica", 10)
    c.drawString(20*mm, height - 85*mm, customer_name)

    # --- Table Header ---
    table_y = height - 100*mm
    c.setFont("Helvetica-Bold", 10)
    c.drawString(20*mm, table_y, "Item")
    c.drawString(90*mm, table_y, "Quantity")
    c.drawString(120*mm, table_y, "Price")
    c.drawString(150*mm, table_y, "Tax")
    c.drawString(170*mm, table_y, "Total")

    # --- Table Rows ---
    c.setFont("Helvetica", 10)
    y = table_y - 10
    grand_total = 0

    for _, row in data.iterrows():
        item_total = (row["Quantity"] * row["Price"]) + row["Tax"]
        c.drawString(20*mm, y, str(row["Item"]))
        c.drawString(90*mm, y, str(row["Quantity"]))
        c.drawString(120*mm, y, f"${row['Price']:.2f}")
        c.drawString(150*mm, y, f"${row['Tax']:.2f}")
        c.drawString(170*mm, y, f"${item_total:.2f}")
        y -= 10
        grand_total += item_total

    # --- Grand Total ---
    c.setFont("Helvetica-Bold", 12)
    c.drawString(150*mm, y - 10, f"Total: ${grand_total:.2f}")

    # --- Footer ---
    c.setFont("Helvetica", 9)
    c.setFillColor(colors.grey)
    c.drawString(20*mm, 20*mm, "Thank you for your business!")

    c.save()
    print(f"✅ Created multi-item invoice: {file_name}")

print("🎉 All professional multi-item invoices created in 'Generated_Invoices' folder!")
