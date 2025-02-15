# Job Buddy - Resume Builder for Optimized ATS

## Overview
Job Buddy is an AI-powered resume builder designed to optimize resumes for Applicant Tracking Systems (ATS). By analyzing job descriptions and tailoring resumes accordingly, Job Buddy ensures that your resume stands out and gets past ATS filters effectively.

## Features
- Upload an existing resume (PDF or DOCX format) for optimization (mandatory).
- Input job descriptions (JD) to tailor resumes to specific roles.
- Provide a LaTeX template for generating formatted resumes.
- Auto-generate ATS-optimized resumes based on user input.
- Manually enter professional details if no resume is available.
- Save manually entered information for future resume generations.
- Download the resume in a structured DOCX format for future use.
- Add custom resume and cover letter prompt templates for personalization.

## How It Works
1. **Enter Contact Details**: Provide your full name, email, phone number, LinkedIn, GitHub, and other professional links.
2. **Specify Target Company**: Enter the company name for customization.
3. **Upload Job Description (JD)**: Paste the job description to tailor your resume accordingly.
4. **Upload Existing Resume**: Upload a PDF or DOCX resume for optimization (mandatory).
5. **Provide LaTeX Template**: Upload a LaTeX template to format your resume correctly.
6. **Generate Resume**: The app processes the input and generates an ATS-friendly resume.
7. **Download Resume**: Download the generated resume in DOCX format.
8. **Alternative Input Option**: If no resume is available, manually input experience, education, skills, projects, patents, and publications. This information can be saved and reused for generating future resumes.

## Tech Stack
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)

- **Frontend**: Streamlit
- **Backend**: Python, LangChain
- **Document Processing**: PyMuPDF (fitz) for PDFs, python-docx for DOCX files
- **AI Integration**: LangChain, OpenAI API
- **Libraries Used**:
  - `langchain`
  - `langchain_openai`
  - `streamlit`
  - `python-docx`
  - `fitz (PyMuPDF)`
  - `dotenv`

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/sayanchaudhuri14/Job-Buddy.git
   ```
2. Navigate to the project folder:
   ```bash
   cd Job-Buddy
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Future Enhancements
- AI-powered resume suggestions for better job matching.
- Integration with job portals for direct application submissions.
- Support for multiple resume formats (e.g., Word, PDF, Markdown).
- Advanced ATS scoring metrics and feedback.

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## Contact
For support or inquiries, reach out via sayanchaudhuri14@gmail.com

