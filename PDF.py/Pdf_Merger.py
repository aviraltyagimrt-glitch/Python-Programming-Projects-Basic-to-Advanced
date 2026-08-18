import os
from PyPDF2 import PdfMerger  
merger = PdfMerger()
files = os.listdir("PDF.py")
i = 1
for j in files:
    if j.endswith(".pdf"):
        # new_name = os.rename(f"PDF.py/{j}",f"PDF.py/File - {i}.pdf")
        # old_path = os.path.join("PDF.py", j)
        # new_name = f"File{i}.pdf"
        # new_path = os.path.join("PDF.py", new_name)
        print(j)
        new_path = f"PDF.py/File - {i}.pdf"
        os.rename(f"PDF.py/{j}", new_path)
        merger.append(new_path)
        # merger.append(f"PDF.py/{j}")
        i += 1

merger.write("PDF.py/Mergerd_pdf.pdf")
merger.close()