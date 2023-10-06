import docx
import os

# Get a list of all the Word documents in the folder
files = [f for f in os.listdir('.') if f.endswith('.docx')]

# Create an empty Word document
merged_document = docx.Document()

# Loop through each document and add it to the merged document
for file in files:
    doc = docx.Document(file)
    for element in doc.element.body:
        merged_document.element.body.append(element)

# Save the merged document
merged_document.save('merged.docx')
