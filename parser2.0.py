from calendar import weekday
import re
from docx import Document
import aspose.words as aw
import parcer
import json



data = {}

file = open("otus.txt", "w")
doc = Document("raspisanie.docx")


for table in doc.tables:
    for row in table.rows:
        for cell in row.cells:
            file.write(cell.text)
            
file.close()

