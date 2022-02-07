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


heading1 = jsonData.get("heading1")
name = jsonData.get("name")
address = jsonData.get("address")
contact = jsonData.get("contact information")
course = jsonData.get("course")

heading2 = jsonData.get("heading2")
profile = jsonData.get("profile")

heading3 = jsonData.get("heading3")
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


class PDF(FPDF):
	def header (self):
		self.image("resume_pic.png", 158, 15, 40)


pdf = PDF("P", "mm", "Letter")
pdf.add_page()


def type_personal_information ():
	pdf.set_font("helvetica", "B")
	pdf.set_font_size (14)
	pdf.cell(40, 10, f"{heading1}", ln=True)
	pdf.set_font("helvetica", "I")
	pdf.set_font_size (12)
	pdf.cell (40, 8, f"{name}", ln=True)
	pdf.cell (40, 8, f"{address}", ln=True)
	pdf.cell (40, 8, f"{contact}", ln=True)
	pdf.cell (40, 8, f"{course}", ln=True)
	
def type_profile ():
	pdf.set_font("helvetica", "B")
	pdf.set_font_size (14)
	pdf.cell(40, 15, f"{heading2}", ln=True)
	pdf.set_font("helvetica")
	pdf.set_font_size (12)
	pdf.cell(40, 8, f"{profile}", ln=True)
		
def type_skills ():
	pdf.set_font("helvetica", "B")
	pdf.set_font_size (14)
	pdf.cell(40, 15, f"{heading3}", ln=True)

	pdf.set_font("helvetica")
	pdf.set_font_size (12)
	pdf.cell(40, 8, f"{skill1}", ln=True)
	pdf.cell (40, 8, f"{skill2}", ln=True)
	pdf.cell (40, 8, f"{skill3}", ln=True)
	pdf.cell (40, 8, f"{skill4}", ln=True)

def type_school():
	pdf.set_font("helvetica", "B")
	pdf.set_font_size (14)
	pdf.cell(40, 15, f"{heading4}", ln=True)

	pdf.set_font("helvetica")
	pdf.set_font_size (12)
	pdf.cell(40, 8, f"{school1}", ln=True)
	pdf.cell (40, 8, f"{school2}", ln=True)
	pdf.cell (40, 8, f"{school3}", ln=True)
	pdf.cell (40, 8, f"{school4}", ln=True)

def type_orgs():
	pdf.set_font("helvetica", "B")
	pdf.set_font_size (14)
	pdf.cell(40, 15, f"{heading5}", ln=True)

	pdf.set_font("helvetica")
	pdf.set_font_size (12)
	pdf.cell(40, 8, f"{org1}", ln=True)
	pdf.cell (40, 8, f"{org2}", ln=True)


type_personal_information()
type_profile()
type_skills()
type_school()
type_orgs()


pdf.output("PANGILINAN_GABRIELLE.pdf")
print("To get PDF, type: python [full name of document] in terminal (ex: python Assignment9_PDF_Resume.py)")










