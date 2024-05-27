import tkinter as tk
from tkinter import ttk
from fpdf import FPDF

class ResumePDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Your Resume', 0, 1, 'C')

    def add_section_title(self, title, font='Arial', size=12, style='U'):
        self.set_font(font, style, size)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def add_section_body(self, body, font='Arial', size=12):
        self.set_font(font, '', size)
        self.multi_cell(0, 10, body)

def generate_resume(name, address, phone, email, degree, school, graduation_year, position, company, duration, skills):
    pdf = ResumePDF()
    pdf.add_page()

    # Add Title
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, f'{name} - Resume', 0, 1, 'C')
    pdf.ln(10)

    # Add Personal Information
    pdf.add_section_title('Personal Information', font='Times', size=14, style='U')
    personal_info = f"""
    Name: {name}
    Address: {address}
    Phone: {phone}
    Email: {email}
    """
    pdf.add_section_body(personal_info)

    # Add Education Section
    pdf.add_section_title('Education', font='Helvetica', size=14, style='U')
    education_info = f"""
    - Degree: {degree}
    - School: {school}
    - Graduation Year: {graduation_year}
    """
    pdf.add_section_body(education_info)

    # Add Work Experience Section
    pdf.add_section_title('Work Experience', font='Courier', size=14, style='U')
    work_experience_info = f"""
    - Position: {position}
    - Company: {company}
    - Duration: {duration}
    """
    pdf.add_section_body(work_experience_info)

    # Add Skills Section
    pdf.add_section_title('Skills', font='Arial', size=14, style='U')
    skills_info = "\n".join(f"- {skill}" for skill in skills.split('\n'))
    pdf.add_section_body(skills_info)

    # Save the PDF
    pdf.output('formatted_resume.pdf')
    print("Resume has been saved to formatted_resume.pdf")

def submit_details():
    name = entry_name.get()
    address = entry_address.get()
    phone = entry_phone.get()
    email = entry_email.get()
    degree = entry_degree.get()
    school = entry_school.get()
    graduation_year = entry_graduation_year.get()
    position = entry_position.get()
    company = entry_company.get()
    duration = entry_duration.get()
    skills = text_skills.get("1.0", tk.END).strip()

    generate_resume(name, address, phone, email, degree, school, graduation_year, position, company, duration, skills)

# Create the main window
root = tk.Tk()
root.title("Resume Generator")

# Create and place the form elements
form_frame = ttk.Frame(root, padding=10)
form_frame.grid(row=0, column=0)

labels = ["Name:", "Address:", "Phone:", "Email:", "Degree:", "School:", "Graduation Year:",
          "Position:", "Company:", "Duration:", "Skills:"]

for i, label_text in enumerate(labels):
    label = ttk.Label(form_frame, text=label_text)
    label.grid(row=i, column=0, sticky=tk.W, pady=5, padx=5)

entry_name = ttk.Entry(form_frame)
entry_name.grid(row=0, column=1, columnspan=2, pady=5, padx=5)

entry_address = ttk.Entry(form_frame)
entry_address.grid(row=1, column=1, columnspan=2, pady=5, padx=5)

entry_phone = ttk.Entry(form_frame)
entry_phone.grid(row=2, column=1, columnspan=2, pady=5, padx=5)

entry_email = ttk.Entry(form_frame)
entry_email.grid(row=3, column=1, columnspan=2, pady=5, padx=5)

entry_degree = ttk.Entry(form_frame)
entry_degree.grid(row=4, column=1, columnspan=2, pady=5, padx=5)

entry_school = ttk.Entry(form_frame)
entry_school.grid(row=5, column=1, columnspan=2, pady=5, padx=5)

entry_graduation_year = ttk.Entry(form_frame)
entry_graduation_year.grid(row=6, column=1, columnspan=2, pady=5, padx=5)

entry_position = ttk.Entry(form_frame)
entry_position.grid(row=7, column=1, columnspan=2, pady=5, padx=5)

entry_company = ttk.Entry(form_frame)
entry_company.grid(row=8, column=1, columnspan=2, pady=5, padx=5)

entry_duration = ttk.Entry(form_frame)
entry_duration.grid(row=9, column=1, columnspan=2, pady=5, padx=5)

text_skills = tk.Text(form_frame, height=4, width=30)
text_skills.grid(row=10, column=1, columnspan=2, pady=5, padx=5)

submit_button = ttk.Button(form_frame, text="Generate Resume", command=submit_details)
submit_button.grid(row=11, column=0, columnspan=3, pady=10)

root.mainloop()
