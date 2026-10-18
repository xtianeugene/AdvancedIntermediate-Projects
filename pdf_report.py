from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def make(data, filename="report.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    y = 750
    for line in data:
        c.drawString(50, y, line)
        y -= 20
    c.save()
    print("Saved", filename)

if __name__ == "__main__":
    make(["Monthly Report", "Revenue: 1000", "Expenses: 400", "Profit: 600"])