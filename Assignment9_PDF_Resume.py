#PDF Resume Creator
	#- Create a python program that will create your personal resume in PDF format
	#- All personal details are stored in a JSON file
	#- Your program should read the JSON file and write the details in the PDF
	#- The output file should be: LASTNAME_FIRSTNAME.pdf

#Note:
	#- Search for available PDF library that you can use
	#- Search how data is structured using JSON format
	#- Search how to read JSON file
	#- You will create the JSON file manually

from fpdf import FPDF

import json

filename = input("Enter filename (ex: Resume.json): ")
data =  open(filename)
jsonData = json.load(data)

#format for calling key and array
print (jsonData.get("name"))
print (jsonData.get("skills")[0])


heading1 = jsonData.get("heading1")
name = jsonData.get("name")
address = jsonData.get("address")
contact = jsonData.get("contact information")
course = jsonData.get("course")

heading2 = jsonData.get("heading2")
profile = jsonData.get("profile")

heading3 = jsonData.get("skills")
skill1 = jsonData.get("skills")[0]
skill2 = jsonData.get("skills")[1]
skill3 = jsonData.get("skills")[2]
skill4 = jsonData.get("skills")[3]

heading4 = jsonData.get("heading4")
school1 = jsonData.get("education")[0]
school2 = jsonData.get("education")[1]
school3 = jsonData.get("education")[2]
school4 = jsonData.get("education")[3]

heading5 = jsonData.get("heading5")
org1 = jsonData.get("academic orgs")[0]
org2 = jsonData.get("academic orgs")[1]



pdf = FPDF("P", "mm", "Letter")
pdf.add_page()

pdf.set_font("times", "B")
pdf.set_font_size (15)
pdf.cell(40, 10, f"{heading1}", ln=2)

pdf.set_font("times")
pdf.set_font_size (13)
pdf.cell (40, 10, f"{name}", ln=1)
pdf.cell (40, 10, f"{address}", ln=1)
pdf.cell (40, 10, f"{contact}", ln=1)
pdf.cell (40, 10, f"{course}", ln=3)


pdf.set_font("times", "B")
pdf.set_font_size (15)
pdf.cell(40, 10, f"{heading2}", ln=2)
































pdf.output("PANGILINAN_GABRIELLE.pdf")

