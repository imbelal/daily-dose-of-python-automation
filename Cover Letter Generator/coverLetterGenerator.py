from docx import Document
import os

template_file_path = 'cover_letter_template.docx'
output_file_path = 'final_cover_letter.docx'

Company_Name = input('Enter company name: ')
Company_Address = input('Enter company address: ')
Job_Title = input('Enter job title: ')
Date = input('Enter application date: ')

variables = {
    "Company_Name": Company_Name,
    "Company_Address": Company_Address,
    "Job_Title": Job_Title,
    "Date": Date
}

template_document = Document(template_file_path)

for key, value in variables.items():
    for paragraph in template_document.paragraphs:
        if key in paragraph.text:
            inline = paragraph.runs
            for item in inline:
                if key in item.text:
                    item.text = item.text.replace(key, value)

template_document.save(output_file_path)
