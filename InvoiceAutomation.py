from reportlab.pdfgen import canvas

# Create a PDF file called 'test_invoice.pdf'
c = canvas.Canvas("test_invoice.pdf")

# Add some text
c.drawString(100, 750, "Invoice #001")
c.drawString(100, 730, "Customer: John Smith")
c.drawString(100, 710, "Item: Web Design Service")
c.drawString(100, 690, "Total: $550")

# Save the PDF
c.save()

print("PDF created successfully!")
