#pdf to txt
#avoid direct pptx to txt, as libraries broken there
#manually save as from pptx to pdf

import os
import PyPDF2

# Get the list of PDF files in the current directory
pdf_files = [f for f in os.listdir() if f.endswith('.pdf')]

# Print the list of PDF files and their numbers
print('PDF files found in the directory:')
for i, pdf_file in enumerate(pdf_files):
    print(f'{i+1}: {pdf_file}')

# Ask the user to select a file
selection = int(input('Enter the number of the file to extract text from: '))

# Open the selected PDF file
pdf_file = open(pdf_files[selection-1], 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Get the number of pages in the PDF file
num_pages = len(pdf_reader.pages)

# Create a new text file to write the extracted text to
text_file = open(f'{pdf_files[selection-1][:-4]}.txt', 'w', encoding='utf-8')

# Loop through each page of the PDF file and extract the text
for page in range(num_pages):
    # Get the page object
    pdf_page = pdf_reader.pages[page]
    
    # Extract the text from the page
    page_text = pdf_page.extract_text()
    
    # Write the text to the text file
    text_file.write(page_text)
    
    # Add a separator with the page number
    separator = f"\n\nNEXT PAGE IS {page+1}\n\n"
    text_file.write(separator)
    
# Close the PDF and text files
pdf_file.close()
text_file.close()
print('All done')