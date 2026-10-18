import openpyxl

def build(filename="data.xlsx"):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Name", "Score"])
    for name, score in [("Alice", 88), ("Bob", 92), ("Carol", 79)]:
        ws.append([name, score])

    ws.append(["Average", f"=AVERAGE(B2:B4"])
    wb.save(filename)
    print("Saved", filename)

if __name__ == "__main__":
    build()