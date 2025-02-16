# Store templates in a dictionary for easier access
TEMPLATES = {
    "Research_Template_1": r'''
    \documentclass[letterpaper, 9pt]{article}

    \usepackage{latexsym}
    \usepackage[empty]{fullpage}
    \usepackage{titlesec}
    \usepackage{marvosym}
    \usepackage[usenames,dvipsnames]{color}
    \usepackage{verbatim}
    \usepackage{enumitem}
    \usepackage[hidelinks]{hyperref}
    \usepackage{fancyhdr}
    \usepackage[english]{babel}
    \usepackage{tabularx}
    \usepackage{fontawesome5}
    \usepackage{multicol}
    \setlength{\multicolsep}{-3.0pt}
    \setlength{\columnsep}{-1pt}

    % Adjust margins
    \addtolength{\oddsidemargin}{-0.6in}
    \addtolength{\evensidemargin}{-0.5in}
    \addtolength{\textwidth}{1.19in}
    \addtolength{\topmargin}{-.7in}
    \addtolength{\textheight}{1.4in}

    % Sections formatting
    \titleformat{\section}{
      \vspace{-4pt}\scshape\raggedright\large\bfseries
    }{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]

    % Custom commands for structured items
    \newcommand{\resumeSubheading}[2]{
      \vspace{-2pt}\item
        \begin{tabular*}{1.0\textwidth}[t]{l@{\extracolsep{\fill}}r}
          \textbf{#1} & \textbf{\small #2} \\
        \end{tabular*} 
    }

    \newcommand{\resumeItem}[1]{
      \item\small{
        {#1 \vspace{0pt}}
      }
    }

    \newcommand{\resumeItemListStart}{\begin{itemize}}
    \newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-0pt}}
    \newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.0in, label={}]}
    \newcommand{\resumeSubHeadingListEnd}{\end{itemize}}

    \begin{document}

    %----------HEADING----------

    \begin{center}
        {\Huge \scshape Your Name} \\ \vspace{8pt}
        \small \raisebox{-0.1\height}\faPhone\ Your Phone Number ~ 
        \href{mailto:your.email@example.com}{\raisebox{-0.2\height}\faEnvelope\ {your.email@example.com}} ~
        \href{https://www.linkedin.com/in/yourprofile}{\raisebox{-0.2\height}\faLinkedin\ {linkedin.com/in/yourprofile}}  ~ 
        \href{https://github.com/yourgithub}{\raisebox{-0.2\height}\faGithub\ {github.com/yourgithub}}
    \end{center}
    \vspace{-10pt}

    %-----------PROFILE SUMMARY-----------
    \section{Profile Summary}
    \resumeSubHeadingListStart
      \resumeItem{Your brief professional summary goes here.}
    \resumeSubHeadingListEnd

    %-----------WORK EXPERIENCE-----------
    \section{Work Experience}
    \resumeSubHeadingListStart
      \resumeSubheading{Job Title}{Company Name, Location | Start Date -- End Date}
      \resumeItemListStart
        \resumeItem{Your job responsibility or achievement.}
      \resumeItemListEnd
    \resumeSubHeadingListEnd

    %-----------TECHNICAL SKILLS-----------
    \section{Technical Skills}
    \resumeSubHeadingListStart
      \resumeItem{Skill Category: List of skills}
    \resumeSubHeadingListEnd

    %-----------RESEARCH & TECHNICAL PROJECTS-----------
    \section{Research and Technical Projects}
    \resumeSubHeadingListStart
      \resumeSubheading{Project Name}{Affiliation or Institution | Date}
      \resumeItemListStart
        \resumeItem{Brief description of the project.}
      \resumeItemListEnd
    \resumeSubHeadingListEnd

    %-----------EDUCATION-----------
    \section{Education}
    \resumeSubHeadingListStart
      \resumeSubheading{Degree}{University Name, Location | Start Date -- End Date}
      \resumeItemListStart
        \resumeItem{Relevant coursework or honors (optional).}
      \resumeItemListEnd
    \resumeSubHeadingListEnd

    %-----------CERTIFICATIONS-----------
    \section{Certifications}
    \resumeSubHeadingListStart
      \resumeItem{Certification Name - Issuing Organization | Date}
    \resumeSubHeadingListEnd

    \end{document}

    ''',
    # Add more templates here as needed
}

def get_all_templates():
    """Returns a dictionary of all available templates."""
    return TEMPLATES
