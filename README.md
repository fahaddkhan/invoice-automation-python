# 📄 Invoice Automation (Python)

A professional invoice automation script written in Python 🐍 that reads invoice data from an Excel file and generates **multi-item PDF invoices** with tax, total, and your business branding.

---

## 🚀 Features

✅ Generate PDF invoices from Excel  
✅ Supports **multiple items per invoice**  
✅ Auto-calculates total and tax  
✅ Saves each invoice in a separate file  
✅ Includes logo, company details, and customer info  
✅ Clean and professional layout  
✅ Easy to customize for your business

---

## 📁 Sample Excel Format

| Invoice Number | Invoice Date | Customer Name | Item         | Quantity | Price | Tax |
|----------------|--------------|----------------|--------------|----------|-------|-----|
| 001            | 2025-08-06   | John Smith     | Web Design   | 1        | 500   | 50  |
| 001            | 2025-08-06   | John Smith     | Hosting      | 1        | 100   | 0   |
| 002            | 2025-08-06   | Sarah Lee      | Logo Design  | 2        | 150   | 15  |

> 📂 Each invoice will be grouped by invoice number and created as a separate PDF.

---

## 🧰 Requirements

```bash
pip install pandas reportlab openpyxl
