import os
import streamlit as st
from datetime import datetime
from utils.document_parser import extract_candidate_info
from resume_generator.resume_chain import generate_resume
from resume_generator.cover_letter_chain import generate_cover_letter
from docx import Document

# Initialize session state for form data
if 'experience_entries' not in st.session_state:
    st.session_state.experience_entries = []
if 'education_entries' not in st.session_state:
    st.session_state.education_entries = []
if 'technical_skills' not in st.session_state:
    st.session_state.technical_skills = []
if 'languages' not in st.session_state:
    st.session_state.languages = []
if 'certifications' not in st.session_state:
    st.session_state.certifications = []
if 'patents' not in st.session_state:
    st.session_state.patents = []
if 'publications' not in st.session_state:
    st.session_state.publications = []

# Streamlit UI
st.set_page_config(layout="wide")
st.title('Resume and Cover Letter Generator')

st.markdown("## Enter Your Information")

# Create a container for the 'Enter Your Information' form
with st.expander("Enter here", expanded=False):
    # Collecting Personal Information
    name = st.text_input("Name (Required)", key="name")
    contact = st.text_input("Contact Number (Required)", key="contact")
    email = st.text_input("Email Address (Required)", key="email")
    address = st.text_input("Address (Required)", key="address")

    # Collecting optional Links
    linkedin = st.text_input("LinkedIn Link", key="linkedin")
    github = st.text_input("GitHub Link", key="github")
    other_links = st.text_area("Other Links", key="other_links")

    # Add Resume Headline and Profile Summary
    st.subheader("Resume Headline & Profile Summary")
    headline = st.text_input("Resume Headline (Optional)", key="headline")
    profile_summary = st.text_area("Profile Summary (Optional)", key="profile_summary")

    # Experience Section
    st.subheader("Experience")
    if st.button("Add Experience", key="add_exp"):
        st.session_state.experience_entries.append({
            'org_name': '',
            'start_date': None,
            'end_date': None,
            'description': '',
            'skills_learned': ''
        })

    for idx, exp in enumerate(st.session_state.experience_entries):
        with st.container():
            st.write(f"Experience {idx + 1}")
            exp['org_name'] = st.text_input(f"Organization Name", value=exp.get('org_name', ''), key=f"exp_org_{idx}")
            exp['start_date'] = st.date_input(f"Start Date", value=exp.get('start_date', None), key=f"exp_start_{idx}")
            exp['end_date'] = st.date_input(f"End Date", value=exp.get('end_date', None), key=f"exp_end_{idx}")
            exp['description'] = st.text_area(f"Description", value=exp.get('description', ''), key=f"exp_desc_{idx}")
            exp['skills_learned'] = st.text_area(f"Skills Learned", value=exp.get('skills_learned', ''), key=f"exp_skills_{idx}")
            if st.button(f"Remove Experience {idx + 1}", key=f"remove_exp_{idx}"):
                st.session_state.experience_entries.pop(idx)
                st.rerun()

    # Education Section
    st.subheader("Education")
    if st.button("Add Education", key="add_edu"):
        st.session_state.education_entries.append({
            'school_name': '',
            'major': '',
            'start_date': None,
            'end_date': None,
            'skills_learned': '',
            'courses_taken': '',
            'thesis': ''
        })

    for idx, edu in enumerate(st.session_state.education_entries):
        with st.container():
            st.write(f"Education {idx + 1}")
            edu['school_name'] = st.text_input(f"School Name", value=edu.get('school_name', ''), key=f"edu_school_{idx}")
            edu['major'] = st.text_input(f"Major", value=edu.get('major', ''), key=f"edu_major_{idx}")
            edu['start_date'] = st.date_input(f"Start Date", value=edu.get('start_date', None), key=f"edu_start_{idx}")
            edu['end_date'] = st.date_input(f"End Date", value=edu.get('end_date', None), key=f"edu_end_{idx}")
            edu['skills_learned'] = st.text_area(f"Skills Learned", value=edu.get('skills_learned', ''), key=f"edu_skills_{idx}")
            edu['courses_taken'] = st.text_area(f"Courses Taken", value=edu.get('courses_taken', ''), key=f"edu_courses_{idx}")
            edu['thesis'] = st.text_area(f"Thesis (if applicable)", value=edu.get('thesis', ''), key=f"edu_thesis_{idx}")
            if st.button(f"Remove Education {idx + 1}", key=f"remove_edu_{idx}"):
                st.session_state.education_entries.pop(idx)
                st.rerun()

    # Technical Skills Section
    st.subheader("Technical Skills")
    if st.button("Add Technical Skill", key="add_tech"):
        st.session_state.technical_skills.append({
            'skill_name': '',
            'proficiency': 1
        })

    for idx, skill in enumerate(st.session_state.technical_skills):
        with st.container():
            skill['skill_name'] = st.text_input(f"Skill Name", value=skill.get('skill_name', ''), key=f"tech_name_{idx}")
            skill['proficiency'] = st.slider(f"Proficiency (1-5 Stars)", 1, 5, value=skill.get('proficiency', 1), key=f"tech_prof_{idx}")
            if st.button(f"Remove Technical Skill {idx + 1}", key=f"remove_tech_{idx}"):
                st.session_state.technical_skills.pop(idx)
                st.rerun()

    # Languages Section
    st.subheader("Languages")
    if st.button("Add Language", key="add_lang"):
        st.session_state.languages.append({
            'language_name': '',
            'proficiency_level': 1
        })

    for idx, lang in enumerate(st.session_state.languages):
        with st.container():
            lang['language_name'] = st.text_input(f"Language", value=lang.get('language_name', ''), key=f"lang_name_{idx}")
            lang['proficiency_level'] = st.slider(f"Proficiency (1-5 Stars)", 1, 5, value=lang.get('proficiency_level', 1), key=f"lang_prof_{idx}")
            if st.button(f"Remove Language {idx + 1}", key=f"remove_lang_{idx}"):
                st.session_state.languages.pop(idx)
                st.rerun()

    # Certifications Section
    st.subheader("Certifications")
    if st.button("Add Certification", key="add_cert"):
        st.session_state.certifications.append({
            'certification_name': '',
            'duration': ''
        })

    for idx, cert in enumerate(st.session_state.certifications):
        with st.container():
            cert['certification_name'] = st.text_input(f"Certification Name", value=cert.get('certification_name', ''), key=f"cert_name_{idx}")
            cert['duration'] = st.text_input(f"Duration", value=cert.get('duration', ''), key=f"cert_duration_{idx}")
            if st.button(f"Remove Certification {idx + 1}", key=f"remove_cert_{idx}"):
                st.session_state.certifications.pop(idx)
                st.rerun()

    # Hobbies and Interests
    hobbies_interests = st.text_area("Hobbies and Interests", key="hobbies")

    # Patents Section
    st.subheader("Patents")
    if st.button("Add Patent", key="add_patent"):
        st.session_state.patents.append({
            'patent_title': '',
            'patent_date': None
        })

    for idx, patent in enumerate(st.session_state.patents):
        with st.container():
            patent['patent_title'] = st.text_input(f"Patent Title", value=patent.get('patent_title', ''), key=f"patent_title_{idx}")
            patent['patent_date'] = st.date_input(f"Date/Expected Date", value=patent.get('patent_date', None), key=f"patent_date_{idx}")
            if st.button(f"Remove Patent {idx + 1}", key=f"remove_patent_{idx}"):
                st.session_state.patents.pop(idx)
                st.rerun()

    # Publications Section
    st.subheader("Publications")
    if st.button("Add Publication", key="add_pub"):
        st.session_state.publications.append({
            'publication_title': '',
            'publication_date': None
        })

    for idx, pub in enumerate(st.session_state.publications):
        with st.container():
            pub['publication_title'] = st.text_input(f"Publication Title", value=pub.get('publication_title', ''), key=f"pub_title_{idx}")
            pub['publication_date'] = st.date_input(f"Publication Date", value=pub.get('publication_date', None), key=f"pub_date_{idx}")
            if st.button(f"Remove Publication {idx + 1}", key=f"remove_pub_{idx}"):
                st.session_state.publications.pop(idx)
                st.rerun()

    # Download Information as DOCX
    if st.button("Download Information as DOCX", key="download_docx"):
        if not name or not contact or not email or not address:
            st.error("Please fill in all required fields (Name, Contact, Email, Address).")
        else:
            # Generate file name
            name_parts = name.split()
            first_name = name_parts[0] if len(name_parts) > 0 else "NoName"
            last_name = name_parts[1] if len(name_parts) > 1 else "NoLastName"
            current_date = datetime.now().strftime("%Y-%m-%d")
            file_name = f"{first_name.lower()}_{last_name.lower()}_{current_date}.docx"

            # Create and save document
            doc = Document()
            doc.add_heading('Resume Information', 0)

            # Add all sections to document
            # Personal Info
            doc.add_heading('Personal Information', level=1)
            doc.add_paragraph(f"Name: {name}")
            doc.add_paragraph(f"Contact: {contact}")
            doc.add_paragraph(f"Email: {email}")
            doc.add_paragraph(f"Address: {address}")
            doc.add_paragraph(f"LinkedIn: {linkedin}")
            doc.add_paragraph(f"GitHub: {github}")
            doc.add_paragraph(f"Other Links: {other_links}")

            if headline:
                doc.add_heading('Resume Headline', level=1)
                doc.add_paragraph(headline)

            if profile_summary:
                doc.add_heading('Profile Summary', level=1)
                doc.add_paragraph(profile_summary)

            # Experience
            if st.session_state.experience_entries:
                doc.add_heading('Experience', level=1)
                for exp in st.session_state.experience_entries:
                    doc.add_paragraph(f"Organization: {exp['org_name']}")
                    doc.add_paragraph(f"Start Date: {exp['start_date']}")
                    doc.add_paragraph(f"End Date: {exp['end_date']}")
                    doc.add_paragraph(f"Description: {exp['description']}")
                    doc.add_paragraph(f"Skills Learned: {exp['skills_learned']}")

            # Education
            if st.session_state.education_entries:
                doc.add_heading('Education', level=1)
                for edu in st.session_state.education_entries:
                    doc.add_paragraph(f"School: {edu['school_name']}")
                    doc.add_paragraph(f"Major: {edu['major']}")
                    doc.add_paragraph(f"Start Date: {edu['start_date']}")
                    doc.add_paragraph(f"End Date: {edu['end_date']}")
                    doc.add_paragraph(f"Skills Learned: {edu['skills_learned']}")
                    doc.add_paragraph(f"Courses Taken: {edu['courses_taken']}")
                    doc.add_paragraph(f"Thesis: {edu['thesis']}")

            # Technical Skills
            if st.session_state.technical_skills:
                doc.add_heading('Technical Skills', level=1)
                for skill in st.session_state.technical_skills:
                    doc.add_paragraph(f"Skill: {skill['skill_name']}")
                    doc.add_paragraph(f"Proficiency: {skill['proficiency']}")

            # Languages
            if st.session_state.languages:
                doc.add_heading('Languages', level=1)
                for lang in st.session_state.languages:
                    doc.add_paragraph(f"Language: {lang['language_name']}")
                    doc.add_paragraph(f"Proficiency: {lang['proficiency_level']}")

            # Certifications
            if st.session_state.certifications:
                doc.add_heading('Certifications', level=1)
                for cert in st.session_state.certifications:
                    doc.add_paragraph(f"Certification: {cert['certification_name']}")
                    doc.add_paragraph(f"Duration: {cert['duration']}")

            # Patents
            if st.session_state.patents:
                doc.add_heading('Patents', level=1)
                for patent in st.session_state.patents:
                    doc.add_paragraph(f"Patent: {patent['patent_title']}")
                    doc.add_paragraph(f"Patent Date: {patent['patent_date']}")

            # Publications
            if st.session_state.publications:
                doc.add_heading('Publications', level=1)
                for pub in st.session_state.publications:
                    doc.add_paragraph(f"Publication: {pub['publication_title']}")
                    doc.add_paragraph(f"Publication Date: {pub['publication_date']}")

            # Hobbies and Interests
            if hobbies_interests:
                doc.add_heading('Hobbies and Interests', level=1)
                doc.add_paragraph(hobbies_interests)

            # Save and download
            if not os.path.exists('downloads'):
                os.makedirs('downloads')
            
            file_path = os.path.join('downloads', file_name)
            doc.save(file_path)

            with open(file_path, 'rb') as file:
                st.download_button("Download DOCX", file, file_name, use_container_width=True)

# Upload Word document section
st.markdown("## Upload your information (Word document)")
uploaded_file = st.file_uploader("Upload your information (Word document)", type="docx")

# Job description section
st.markdown("## Paste the job description")
job_description = st.text_area("Paste the job description")

# LaTeX template section
st.markdown("## Paste the LaTeX template code")
template = st.text_area("Paste the LaTeX template code")

# Generate Resume and Cover Letter
if uploaded_file:
    candidate_info = extract_candidate_info(uploaded_file)
    
    if st.button("Generate Resume"):
        resume = generate_resume(job_description, candidate_info, template)
        st.text_area("Generated Resume (LaTeX)", value=resume, height=300)
    
    if st.button("Generate Cover Letter"):
        cover_letter = generate_cover_letter(job_description, candidate_info)
        st.text_area("Generated Cover Letter", value=cover_letter, height=300)
