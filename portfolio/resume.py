from fpdf import FPDF

class ResumePDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Kamron Matkarimov - Python Developer', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_contact_info(self):
        self.set_font('Arial', '', 12)
        self.cell(0, 10, 'Telegram: @matkarimovv7', 0, 1, 'L')
        self.cell(0, 10, 'Instagram: @matkarimovff', 0, 1, 'L')
        self.ln()

    def add_skills(self):
        skills = [
            'Python', 'Django', 'HTML', 'CSS', 'JavaScript', 'MySQL', 'Git'
        ]
        self.chapter_title('Skills')
        for skill in skills:
            self.chapter_body(f'- {skill}')
        self.ln()

    def add_experience(self):
        self.chapter_title('Experience')
        self.chapter_body(
            '''Backend Developer at Company XYZ (2023-present)
            - Developed and maintained Python/Django applications.
            - Worked with databases like MySQL and PostgreSQL.
            - Implemented RESTful APIs and collaborated with front-end developers.'''
        )
        self.ln()

    def add_education(self):
        self.chapter_title('Education')
        self.chapter_body(
            '''Bachelor of Science in Computer Science, University of ABC (2021-2023)
            - Learned about software engineering, data structures, and algorithms.
            - Participated in multiple coding competitions and hackathons.'''
        )
        self.ln()

    def add_resume(self):
        self.add_contact_info()
        self.add_skills()
        self.add_experience()
        self.add_education()

# Create PDF
pdf = ResumePDF()
pdf.add_page()
pdf.add_resume()
pdf.output("Kamron_Matkarimov_Resume.pdf")
