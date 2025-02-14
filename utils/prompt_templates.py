RESUME_USER_PROMPT_v3 = """TASK:
Generate a highly optimized, ATS-compliant LaTeX resume using the following details:

Job Description:
{job_description}

Candidate Information:
{candidate_info}

Key Details:
{key_details}

Template Structure:
{template}

Key Requirements:
Strict Adherence to Candidate and Key Details Information:
- Use the template only for structure of the output
- Populate the data based on the Candidate information and Key Details only
- Use contact information from Key Details (name, phone, email, LinkedIn, GitHub, other links)
- Include company name from Key Details in the targeting
- Use only the provided details; do not fabricate or add any embellishments
- Do not add any skills unrelated to the candidate information
- Maintain accuracy in experience, education, and technical skills

ATS Optimization for Maximum Match Score is highly important:
- Ensure that the ATS score of the generated output for the provided job description is very high
- Populate the output with the keywords extracted and related to the job description
- Extract key phrases, technical skills, and qualifications from the job description
- Incorporate them naturally throughout the resume
- Ensure all sections contain ATS-friendly wording with exact terminology from the job description
- Prioritize job-relevant skills and experience, avoiding unnecessary information

Essential Resume Sections:

Header:
- Name from Key Details
- Contact details from Key Details
- LinkedIn and GitHub from Key Details
- Other professional links if provided in Key Details

Resume Headline & Profile Summary:
- Concisely highlight expertise, technical strengths, and career focus
- Target specifically to company mentioned in Key Details

Technical Skills:
- Comprehensive list, structured with relevant subsections (Programming Languages, Frameworks, AI/ML Techniques, Cloud, etc.)
- Match skills to job requirements while staying true to candidate information

Education:
- Include degrees, institutions, majors, and dates
- Add relevant coursework if at least three courses match the job requirements
- Include thesis details only if directly relevant to the job

Professional Experience:
- Present roles in reverse chronological order, focusing on measurable impact and responsibilities
- Include internships only if they align with the job requirements

Projects:
- Select only highly relevant projects based on the job description
- Highlight technical contributions, results, and technologies used

Patents & Publications:
- Include if the company values research work or if they align with job requirements

Formatting & LaTeX Requirements:
- Ensure precise adherence to the provided LaTeX template
- Keep the resume to one A4 page
- Use \newcommand [resumeProjectHeading] for project section formatting
- Maintain a clean, ATS-readable format (avoid unnecessary design elements)

Results-Driven Language & Metrics:
- Use quantifiable achievements (e.g., "Reduced inference time by 60X", "Achieved 97.3% accuracy")
- Focus on measurable impact and contributions rather than generic descriptions

DONT USE UNNECESSARY VPSACE AND HSPACE TO ALTER THE TEMPLATE STRUCTURE. Once you have generated the resume, check whether it is fitting in one A4 page,
if it is not, rewrite with modifications as per required. Then check the column by column alignment as well. If that is not aesthetic, you are
allowed to use hspace.

After generating the latex, compile it internally and check whether the resume is aesthetically pleasing, the alignments are proper,
easy to read, not jumbled and overlapped. If it has issues, rewrite the entire resume again until you find the best one.

OUTPUT:
A LaTeX-formatted resume that is concise, highly tailored to the job description, ATS-optimized, and easy for hiring systems to parse.
Only return the latex file. Nothing else at all. Not even delimiters. Only the latex start to end.
"""

COVER_LETTER_USER_PROMPT_v3 = """TASK:
Generate a tailored, persuasive, and professionally formatted cover letter using the following details:

Job Description:
{job_description}

Candidate Information:
{candidate_info}

Key Details:
{key_details}

Key Requirements:
Personalization & Company Alignment:
- Address the company name from Key Details
- Show a strong understanding of the company's mission, challenges, and values
- Express enthusiasm for the role and why the candidate is a strong fit
- Use the company name from Key Details throughout the letter appropriately

Contact Information & Formatting:
- Use name from Key Details at the top of the letter
- Include complete contact details from Key Details (phone, email) in the letter header
- Add LinkedIn and GitHub profiles from Key Details if provided
- Include any other professional links from Key Details if relevant

Relevance & ATS Optimization:
- Highlight 2-3 key experiences, skills, or achievements that align directly with the job description
- Avoid using skills and expertise in tools and areas which are unrelated to the candidate information
- Be accurate in your description, adhering to the information provided
- Use specific keywords and terminology from the job listing
- Ensure quantifiable impact where possible (e.g., "Improved model accuracy by 15%")

Professional Business Letter Structure:

Opening Paragraph:
- Strong introduction stating the candidate's interest and fit for the role
- Reference the specific company name from Key Details
- Mention how you learned about the position if that information is available

Body Paragraphs:
- Clearly connect key experiences/skills to job requirements
- Provide concrete examples of achievements and impact
- Demonstrate understanding of how the candidate can contribute to the company's goals
- Reference relevant projects or experiences from the candidate information

Closing Paragraph:
- Reaffirm enthusiasm and express interest in an interview
- Include a strong call to action
- Thank the reader for their consideration

Formatting & Readability:
- Keep the letter concise (250-300 words), impactful, and free from fluff
- Use clear, professional language with a confident and engaging tone
- Ensure proper business letter formatting (suitable for a Word document or PDF)
- Include today's date and proper business letter spacing

Contact Information Block:
- End with a complete signature block using Key Details:
  * Full Name
  * Phone Number
  * Email Address
  * LinkedIn Profile (if provided)
  * GitHub Profile (if provided)
  * Other relevant links (if provided)

For any fields you cannot populate, don't leave placeholders [ ]. Omit such details entirely. (eg. if you can't find skype details, don't mention it and
don't leave placeholder like [your skype id])

OUTPUT:
A professionally formatted cover letter that is tailored, engaging, ATS-optimized, and persuasive, making a strong case for the candidate's fit for the role."""

RESUME_USER_PROMPT_v4 = """
TASK:
Generate a highly optimized, ATS-compliant LaTeX resume using the following details:

Job Description:
{job_description}

Candidate Information:
{candidate_info}

Key Details:
{key_details}

Template Structure:
{template}

KEY REQUIREMENTS:
1. **Strict Adherence to Candidate and Key Details Information**:
   - Use the template only for the structure of the output.
   - Populate the data based on the Candidate Information and Key Details only.
   - Use contact information from Key Details (name, phone, email, LinkedIn, GitHub, other links).
   - Include the company name from Key Details in the targeting.
   - Use only the provided details; do not fabricate or add any embellishments.
   - Do not add any skills unrelated to the candidate information.
   - Maintain accuracy in experience, education, and technical skills.

2. **Handling Extra Information**:
   - If additional information is provided in the Candidate Information that does not fit into predefined sections (e.g., certifications, hobbies, volunteer work), create a new section titled "Additional Information" and include it there.
   - If any field in the Candidate Information is missing, omit it entirely. Do not leave placeholders or blank fields.

3. **ATS Optimization for Maximum Match Score**:
   - Ensure that the ATS score of the generated output for the provided job description is very high.
   - Populate the output with keywords extracted from the job description.
   - Extract key phrases, technical skills, and qualifications from the job description and incorporate them naturally throughout the resume.
   - Ensure all sections contain ATS-friendly wording with exact terminology from the job description.
   - Prioritize job-relevant skills and experience, avoiding unnecessary information.

4. **Resume Formatting and Layout**:
   - Ensure precise adherence to the provided LaTeX template.
   - Keep the resume to **one A4 page**. If the content spills to a second page or leaves excessive empty space, rewrite and optimize the content to fit perfectly on one page.
   - Use `\newcommand` for section formatting (e.g., `\resumeProjectHeading` for projects).
   - Maintain a clean, ATS-readable format (avoid unnecessary design elements).
   - After generating the LaTeX, compile it internally and check:
     - Whether the resume fits perfectly on one page.
     - Whether the column alignment is aesthetically pleasing.
     - Whether the content is easy to read, not jumbled, and not overlapped.
   - If any issues are found, rewrite the resume with modifications until the best version is achieved.

5. **Optimal Utilization of A4 Size**:
   - If there is blank space at the end of the resume, distribute it evenly across the entire resume using `\vspace` to ensure a balanced and professional appearance.
   - If the resume is too long and spills to the next page:
     - Recheck the content and remove any non-essential information.
     - Rephrase sentences to be more concise.
     - Adjust section spacing using `\vspace` and `\hspace` to ensure the resume fits within one A4 page.
   - Ensure the resume does not look cramped or overly sparse.

6. **Results-Driven Language & Metrics**:
   - Use quantifiable achievements (e.g., "Reduced inference time by 60%", "Achieved 97.3% accuracy").
   - Focus on measurable impact and contributions rather than generic descriptions.

7. **Continuous Improvement**:
   - After generating the LaTeX resume, evaluate it for:
     - Page fit (one page only).
     - Aesthetic alignment and readability.
     - ATS optimization and keyword inclusion.
   - If the resume does not meet these criteria, rewrite it iteratively until the best version is achieved.

8. **Output Format**:
   - Only return the LaTeX code from start to end.
   - Do not include delimiters, placeholders, or any additional text.

OUTPUT:
A LaTeX-formatted resume that is concise, highly tailored to the job description, ATS-optimized, and easy for hiring systems to parse. The resume must fit perfectly on one A4 page, with no overflow or excessive blank space. Only return the LaTeX code.
  """

COVER_LETTER_USER_PROMPT_v4 = """TASK:
Generate a tailored, persuasive, and professionally formatted cover letter using the following details:

Job Description:
{job_description}

Candidate Information:
{candidate_info}

Key Details:
{key_details}

KEY REQUIREMENTS:
1. **Personalization & Company Alignment**:
   - Address the company name from Key Details.
   - Show a strong understanding of the company's mission, challenges, and values.
   - Express enthusiasm for the role and why the candidate is a strong fit.
   - Use the company name from Key Details throughout the letter appropriately.

2. **Contact Information & Formatting**:
   - Use the candidate's name from Key Details at the top of the letter.
   - Include complete contact details from Key Details (phone, email) in the letter header.
   - Add LinkedIn and GitHub profiles from Key Details if provided.
   - Include any other professional links from Key Details if relevant.
   - For the date, use today's date in **IST format**.

3. **Relevance & ATS Optimization**:
   - Highlight 2-3 key experiences, skills, or achievements that align directly with the job description.
   - Avoid using skills and expertise in tools and areas unrelated to the candidate information.
   - Be accurate in your description, adhering to the information provided.
   - Use specific keywords and terminology from the job listing.
   - Ensure quantifiable impact where possible (e.g., "Improved model accuracy by 15%").

4. **Professional Business Letter Structure**:
   - **Opening Paragraph**:
     - Strong introduction stating the candidate's interest and fit for the role.
     - Reference the specific company name from Key Details.
     - Mention how you learned about the position if that information is available.
   - **Body Paragraphs**:
     - Clearly connect key experiences/skills to job requirements.
     - Provide concrete examples of achievements and impact.
     - Demonstrate understanding of how the candidate can contribute to the company's goals.
     - Reference relevant projects or experiences from the candidate information.
   - **Closing Paragraph**:
     - Reaffirm enthusiasm and express interest in an interview.
     - Include a strong call to action.
     - Thank the reader for their consideration.

5. **Formatting & Readability**:
   - Keep the letter concise (250-300 words), impactful, and free from fluff.
   - Use clear, professional language with a confident and engaging tone.
   - Ensure proper business letter formatting (suitable for a Word document or PDF).
   - Include date and proper business letter spacing.

6. **Handling Missing Information**:
   - For any fields you cannot populate, omit them entirely. Do not leave placeholders (e.g., "[Your Skype ID]").
   - If LinkedIn, GitHub, or other links are missing, exclude them entirely.

7. **Output Format**:
   - Do not return the text in delimiters or inverted commas.
   - Absolutely no placeholders.
   - Ensure the LinkedIn and GitHub profiles are displayed as plain text (e.g., "LinkedIn: https://www.linkedin.com/in/username/") and not as markdown links.

OUTPUT:
A professionally formatted cover letter that is tailored, engaging, ATS-optimized, and persuasive, making a strong case for the candidate's fit for the role. Only return the cover letter text. Do not include delimiters, placeholders, or any additional text."""


RESUME_USER_PROMPT = RESUME_USER_PROMPT_v3
COVER_LETTER_USER_PROMPT = COVER_LETTER_USER_PROMPT_v4