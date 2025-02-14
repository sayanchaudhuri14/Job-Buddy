
RESUME_USER_PROMPT = """
Generate a LaTeX resume following these parameters:

- **Job Description:**  
  {job_description}  

- **Candidate Information:**  
  {candidate_info}  

- **Template Structure:**  
  {template}  

#### **Requirements:**  
1. Use **only** the information from the candidate’s details—no additional embellishments.  
2. Follow the **exact** structure of the provided LaTeX template without modifications.  
3. Ensure the resume is **precisely one A4 page** long.  
4. Integrate **high-value keywords** from the job description to enhance ATS optimization and **maximize ATS score**.  
5. Focus on **results-driven language**, incorporating measurable impact where possible.  
6. Include candidate's **contact details** (phone number, email, and location) **only from the provided candidate information**.  
"""

COVER_LETTER_USER_PROMPT = """
Write a professional cover letter based on the following details:

- **Job Description:**  
  {job_description}  

- **Candidate Information:**  
  {candidate_info}  

#### **Requirements:**  
1. **Clearly address** the key job requirements and explain how the candidate meets them.  
2. **Highlight 2-3 major achievements** that showcase the candidate’s value.  
3. Show **genuine understanding of the company’s mission and challenges**.  
4. Keep the letter **brief yet impactful** (250-300 words).  
5. Use **proper business letter formatting** with a strong opening and closing.  
6. Include candidate's **contact details** (phone number, email, and location) **only from the provided candidate information**.  
7. Maintain a **confident and formal** tone while ensuring clarity and persuasion.  
"""

RESUME_USER_PROMPT_v1="""
Create a highly optimised ATS-readable resume in LaTeX format using the following information:


- **Job Description:**  
  {job_description}  

- **Candidate Information:**  
  {candidate_info}  

- **Template Structure:**  
  {template}  

  
   - Adapt the resume to fit the company’s culture, values, key terminologies as per job requirements.

**Action Plan:**

1. **Incorporate following Details:**
- Must include sections: are Education, Technical Skills, Professional Experiences (include internship experience if any of technical requirements match from internship to job description)
- Include Section: Relevant Coursework only if it has more than 3 courses matching with Job requirements / technical requirements
- Include Sections: Patent and Publication company values research publication and patents or if publication and patent is strong match with  with Job requirements and technical requirements
- Include Section: Projects that matches directly or indirectly (choose particular projects which matches in technical skills sense)
- Must focus on Section Technical Skills, this should include all job description keywords, technical skills, domains, programming language and frameworks and other subsection.

2. **Optimise for Job Description:** (Extra attentions here)
   - Integrate exact phrases, keywords, and qualifications from the job description into the resume in all sections and keep concise.

3. **ATS-Friendly LaTeX Output:**
   - Make sure to add resumeProjectHeading
   - Ensure the resume is simple, clean, and compatible with ATS systems, avoiding any unnecessary complexity or design elements.


**make sure to add following block in resume - 
newcommand -- resumeProjectHeading from source latex**
   
Final result: A pure LaTeX highly matching resume optimised for ATS systems, easy to read by hiring software.
"""


COVER_LETTER_USER_PROMPT_v1 = """
You are a professional cover letter writer. Write a compelling cover letter for the following job description and candidate profile. The cover letter should emphasize the candidate's most relevant skills and experiences in relation to the job description.

Job Description: {job_description}

Candidate Information: {candidate_info}

The cover letter should:

Show enthusiasm for the role and the company.
Highlight 2-3 of the most relevant experiences/skills from the candidate's profile.
Demonstrate an understanding of the company's needs.
Include a strong call to action.
The cover letter should be in a structured, professional format, suitable for inclusion in a Word document. The content should be clearly written, well-organized, and formatted according to the template structure provided."""


RESUME_USER_PROMPT_v2 = """TASK:
Generate a highly optimized, ATS-compliant LaTeX resume using the following details:

Job Description:
{job_description}

Candidate Information:
{candidate_info}

Template Structure:
{template}

Key Requirements:
Strict Adherence to Candidate Information

Use only the provided details; do not fabricate or add any embellishments.
Maintain accuracy in experience, education, and technical skills.
Include candidate's contact details (phone, email, LinkedIn, GitHub, and location) exactly as provided.
ATS Optimization for Maximum Match Score

Extract key phrases, technical skills, and qualifications from the job description and incorporate them naturally throughout the resume.
Ensure all sections contain ATS-friendly wording with exact terminology from the job description.
Prioritize job-relevant skills and experience, avoiding unnecessary information.
Essential Resume Sections:

Header: Name, contact details, LinkedIn, GitHub (if provided).
Resume Headline & Profile Summary: Concisely highlight expertise, technical strengths, and career focus.
Technical Skills: Comprehensive list, structured with relevant subsections (Programming Languages, Frameworks, AI/ML Techniques, Cloud, etc.).
Education:
Include degrees, institutions, majors, and dates.
Add relevant coursework if at least three courses match the job requirements.
Include thesis details only if directly relevant to the job.
Professional Experience:
Present roles in reverse chronological order, focusing on measurable impact and responsibilities.
Include internships only if they align with the job requirements.
Projects:
Select only highly relevant projects based on the job description.
Highlight technical contributions, results, and technologies used.
Patents & Publications:
Include if the company values research work or if they align with job requirements.
Formatting & LaTeX Requirements:

Ensure precise adherence to the provided LaTeX template.
Keep the resume to one A4 page.
Use \newcommand(curly bracket open)resumeProjectHeading(curly bracket close) for project section formatting.
Maintain a clean, ATS-readable format (avoid unnecessary design elements).
Results-Driven Language & Metrics

Use quantifiable achievements (e.g., "Reduced inference time by 60X", "Achieved 97.3% accuracy").
Focus on measurable impact and contributions rather than generic descriptions.
OUTPUT:
A LaTeX-formatted resume that is concise, highly tailored to the job description, ATS-optimized, and easy for hiring systems to parse.

"""
COVER_LETTER_USER_PROMPT_v2 = """TASK:
Generate a tailored, persuasive, and professionally formatted cover letter using the following details:

Job Description:
{job_description}

Candidate Information:
{candidate_info}

Key Requirements:
Personalization & Company Alignment

Clearly address the company name and hiring manager (if available).
Show a strong understanding of the company’s mission, challenges, and values.
Express enthusiasm for the role and why the candidate is a strong fit.
Relevance & ATS Optimization

Highlight 2-3 key experiences, skills, or achievements that align directly with the job description.
Use specific keywords and terminology from the job listing.
Ensure quantifiable impact where possible (e.g., "Improved model accuracy by 15%").
Professional Business Letter Structure

Opening Paragraph: Strong introduction stating the candidate’s interest and fit for the role.
Body Paragraphs:
Clearly connect key experiences/skills to job requirements.
Provide concrete examples of achievements and impact.
Demonstrate understanding of how the candidate can contribute to the company’s goals.
Closing Paragraph:
Reaffirm enthusiasm and express interest in an interview.
Include a strong call to action.
Formatting & Readability

Keep the letter concise (250-300 words), impactful, and free from fluff.
Use clear, professional language with a confident and engaging tone.
Ensure proper business letter formatting (suitable for a Word document or PDF).
Incorporate Candidate Contact Information

Include phone number, email, and location exactly as provided.
Use a formal signature line with the candidate’s name.
OUTPUT:
A professionally formatted cover letter that is tailored, engaging, ATS-optimized, and persuasive, making a strong case for the candidate’s fit for the role."""



RESUME_USER_PROMPT_v3 = """TASK:
Generate a highly optimized, ATS-compliant LaTeX resume using the following details:

Job Description:
{job_description}

Candidate Information:
{candidate_info}

Template Structure:
{template}

Key Requirements:
Strict Adherence to Candidate Information. Use the template only for structure of the output. Populate the data based on the Candidate information only. 

Use only the provided details; do not fabricate or add any embellishments. Do not add any skills unrelated to the candidate information.
Maintain accuracy in experience, education, and technical skills.
Include candidate's contact details (phone, email, LinkedIn, GitHub, and location) exactly as provided. 
ATS Optimization for Maximum Match Score is highly important. Ensure that the ATS score of the generated output for the provided job description is very high.
Populate the output with the keywords extracted and related to the job description.

Extract key phrases, technical skills, and qualifications from the job description and incorporate them naturally throughout the resume.
Ensure all sections contain ATS-friendly wording with exact terminology from the job description.
Prioritize job-relevant skills and experience, avoiding unnecessary information.
Essential Resume Sections:

Header: Name, contact details, LinkedIn, GitHub (if provided).
Resume Headline & Profile Summary: Concisely highlight expertise, technical strengths, and career focus.
Technical Skills: Comprehensive list, structured with relevant subsections (Programming Languages, Frameworks, AI/ML Techniques, Cloud, etc.).
Education:
Include degrees, institutions, majors, and dates.
Add relevant coursework if at least three courses match the job requirements.
Include thesis details only if directly relevant to the job.
Professional Experience:
Present roles in reverse chronological order, focusing on measurable impact and responsibilities.
Include internships only if they align with the job requirements.
Projects:
Select only highly relevant projects based on the job description.
Highlight technical contributions, results, and technologies used.
Patents & Publications:
Include if the company values research work or if they align with job requirements.
Formatting & LaTeX Requirements:

Ensure precise adherence to the provided LaTeX template.
Keep the resume to one A4 page.
Use \newcommand(curly bracket open)resumeProjectHeading(curly bracket close) for project section formatting.
Maintain a clean, ATS-readable format (avoid unnecessary design elements).
Results-Driven Language & Metrics

Use quantifiable achievements (e.g., "Reduced inference time by 60X", "Achieved 97.3% accuracy").
Focus on measurable impact and contributions rather than generic descriptions.
DONT USE UNNECESSARY VPSACE AND HSPACE TO ALTER THE TEMPLATE STRUCTURE. once you have generated the resume, check whether it is fitting in one A4 page,
if it is not, rewrite with modifications as per required. then check the column by column alignment as well. if that is not aesthetic, you are
allowed to use hspace.

After generating the latex, compile it internally and check whether the resume is aesthetically pleasing, the alignments are proper,
easy to read, not jumbled and overlapped. if it has issues, rewrite the entire resume again until you find the best one.
OUTPUT:
A LaTeX-formatted resume that is concise, highly tailored to the job description, ATS-optimized, and easy for hiring systems to parse.
Only return the latex file. Nothing else at all. Not even delimiters. only the latex start to end. 

"""

COVER_LETTER_USER_PROMPT_v3 = """TASK:
Generate a tailored, persuasive, and professionally formatted cover letter using the following details:

Job Description:
{job_description}

Candidate Information:
{candidate_info}

Key Requirements:
Personalization & Company Alignment

Clearly address the company name and hiring manager (if available).
Show a strong understanding of the company’s mission, challenges, and values.
Express enthusiasm for the role and why the candidate is a strong fit.
Relevance & ATS Optimization
Include candidate's contact details (name,phone, email) exactly as provided at the bottom of the output.
Highlight 2-3 key experiences, skills, or achievements that align directly with the job description.
Avoid using skills and expertise in tools and area which are unrelated to the candidate information. Be accurate in your description,
adhering to the information provided.
Use specific keywords and terminology from the job listing.
Ensure quantifiable impact where possible (e.g., "Improved model accuracy by 15%").
Professional Business Letter Structure

Opening Paragraph: Strong introduction stating the candidate’s interest and fit for the role.
Body Paragraphs:
Clearly connect key experiences/skills to job requirements.
Provide concrete examples of achievements and impact.
Demonstrate understanding of how the candidate can contribute to the company’s goals.
Closing Paragraph:
Reaffirm enthusiasm and express interest in an interview.
Include a strong call to action.
Formatting & Readability

Keep the letter concise (250-300 words), impactful, and free from fluff.
Use clear, professional language with a confident and engaging tone.
Ensure proper business letter formatting (suitable for a Word document or PDF).

Incorporate Candidate Contact Information at the end exactly as provided in the candidate information
Include phone number, email, and location exactly as provided.
for field you cannot populate, dont leave placeholders [ ]. Omit such details entirely. (eg. if you cant find skype details, dont mention it and
dont leave placeholder like [your skype id])
OUTPUT:
A professionally formatted cover letter that is tailored, engaging, ATS-optimized, and persuasive, making a strong case for the candidate’s fit for the role."""




RESUME_USER_PROMPT = RESUME_USER_PROMPT_v3
COVER_LETTER_USER_PROMPT = COVER_LETTER_USER_PROMPT_v3