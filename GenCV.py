from tkinter import *
from tkinter import messagebox
from fpdf import FPDF

def generate_resume(name, phone, email, degree, school, graduation_year, position, company, duration, skills, projects, achievements, hobbies):
    pdf = FPDF()
    pdf.add_page()

    # Add Title
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, f"{name}", 0, 1, 'C')
    pdf.cell(0, 10, f"{email}-{phone}", 0, 1, 'C')
    pdf.ln(10)
    
    # Adding carrier objective
    pdf.set_font('Helvetica', 'UB', 14)
    pdf.cell(0, 10, 'Carrier Objective', 0, 1, 'L')
    objective = f"To obtain a challenging position in the field of software development where my skills and experience can be utilized to their fullest potential."
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 5, objective)
    
    # Add Education Section
    pdf.set_font('Helvetica', 'UB', 14)
    pdf.cell(0, 10, 'Education', 0, 1, 'L')
    education_info = f"""
    - Degree: {degree}
    - College: {school}
    - Graduation Year: {graduation_year}
    """
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 5, education_info)
    
    # Add Skills Section
    pdf.set_font('Helvetica', 'UB', 14)
    pdf.cell(0, 10, 'Skills', 0, 1, 'L')
    skills_info = "\n".join(f"- {skill}" for skill in skills.split('\n'))
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 5, skills_info)
    
    #Adding projects Section
    pdf.set_font('Arial', 'UB', 14)
    pdf.cell(0, 10, 'Projects', 0, 1, 'L')
    project_lines = projects.split('\n')
    formatted_projects = ""
    for i in range(0, len(project_lines), 2):
        title = project_lines[i]
        description = project_lines[i + 1] if i + 1 < len(project_lines) else ""
        formatted_projects += f"{title}\n{description}\n"
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 5, formatted_projects)
    
    # Add Work Experience Section
    pdf.set_font('Helvetica', 'UB', 14)
    pdf.cell(0, 10, 'Work Experience', 0, 1, 'L')
    work_experience_info = f"""
    - Position: {position}
    - Company: {company}
    - Duration: {duration}
    """
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 5, work_experience_info)
    
    # Add Achievements Section
    pdf.set_font('Arial', 'UB', 14)
    pdf.cell(0, 10, 'Achievements', 0, 1, 'L')
    achievements_info = "\n".join(f"- {achievement}" for achievement in achievements.split('\n'))
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 5, achievements_info)

    # Add Hobbies Section
    pdf.set_font('Arial', 'UB', 14)
    pdf.cell(0, 10, 'Hobbies', 0, 1, 'L')
    hobbies_info = "\n".join(f"- {hobby}" for hobby in hobbies.split('\n'))
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 5, hobbies_info)

    # Add Declaration Section
    pdf.set_font('Arial', 'UB', 14)
    pdf.cell(0, 10, 'Declaration', 0, 1, 'L')
    declaration = "I hereby declare that the above information is true and correct to the best of my knowledge."
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 5, declaration)

    # Save the PDF
    pdf.output('CV.pdf')
    messagebox.showinfo("Success", "Resume has been saved to CV.pdf")

def submit_details():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    degree = entry_degree.get()
    college = entry_college.get()
    graduation_year = entry_graduation_year.get()
    position = entry_position.get()
    company = entry_company.get()
    duration = entry_duration.get()
    skills = text_skills.get("1.0", END).strip()
    projects = text_projects.get("1.0", END).strip()
    achievements = text_achievements.get("1.0", END).strip()
    hobbies = text_hobbies.get("1.0", END).strip()

    generate_resume(name, phone, email, degree, college, graduation_year, position, company, duration, skills, projects, achievements, hobbies)

# Create the main window
root = Tk()
root.title("CV_Builder")

# Create and place the form elements
form_frame = Frame(root, padx=10, pady=10)
form_frame.grid(row=0, column=0)

labels = ["Name:", "Phone:", "Email:", "Degree:", "College:", "Graduation Year:",
          "Position:", "Company:", "Duration:", "Skills:", "Projects:", "Achievements:", "Hobbies:"]

for i in range(len(labels)):
    label = Label(form_frame, text=labels[i])
    label.grid(row=i, column=0, sticky=W, pady=5, padx=5)

entry_name = Entry(form_frame)
entry_name.grid(row=0, column=1, columnspan=2, pady=5, padx=5)

entry_phone = Entry(form_frame)
entry_phone.grid(row=1, column=1, columnspan=2, pady=5, padx=5)

entry_email = Entry(form_frame)
entry_email.grid(row=2, column=1, columnspan=2, pady=5, padx=5)

entry_degree = Entry(form_frame)
entry_degree.grid(row=3, column=1, columnspan=2, pady=5, padx=5)

entry_college = Entry(form_frame)
entry_college.grid(row=4, column=1, columnspan=2, pady=5, padx=5)

entry_graduation_year = Entry(form_frame)
entry_graduation_year.grid(row=5, column=1, columnspan=2, pady=5, padx=5)

entry_position = Entry(form_frame)
entry_position.grid(row=6, column=1, columnspan=2, pady=5, padx=5)

entry_company = Entry(form_frame)
entry_company.grid(row=7, column=1, columnspan=2, pady=5, padx=5)

entry_duration = Entry(form_frame)
entry_duration.grid(row=8, column=1, columnspan=2, pady=5, padx=5)

text_skills = Text(form_frame, height=4, width=30)
text_skills.grid(row=9, column=1, columnspan=2, pady=5, padx=5)

text_projects = Text(form_frame, height=4, width=30)
text_projects.grid(row=10, column=1, columnspan=2, pady=5, padx=5)

text_achievements = Text(form_frame, height=4, width=30)
text_achievements.grid(row=11, column=1, columnspan=2, pady=5, padx=5)

text_hobbies = Text(form_frame, height=4, width=30)
text_hobbies.grid(row=12, column=1, columnspan=2, pady=5, padx=5)

submit_button = Button(form_frame, text="Generate Resume", command=submit_details)
submit_button.grid(row=13, column=0, columnspan=3, pady=10)

root.mainloop()
