from pathlib import Path
import gspread
import re
import streamlit as st
from PIL import Image
from google.oauth2.service_account import Credentials
from datetime import datetime
from my_helper import ensure_headers


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Musa_Godwin_Resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Musa Godwin"
PAGE_ICON = ":material/work_history:"
NAME = "Musa Godwin"
DESCRIPTION = """
Data Scientist and App Developer with expertise in Python and AI-driven solutions.
Experienced in data analysis and customer-focused projects, blending technical skills with creative problem-solving.
"""
EMAIL = "musa.godwin8112@gmail.com"
SOCIAL_MEDIA = {
    "Medium": "https://medium.com/@musa.godwin8112",
    "LinkedIn": "https://www.linkedin.com/in/musa-godwin",
    "GitHub": "https://github.com/GeamXD",
    "Twitter": "https://twitter.com/musa__godwin",
}

# Set Page Config
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write("---")
    st.write(DESCRIPTION)
    st.download_button(
        label=" :material/download: Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write(":material/mail:", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader(":material/today: Experience")
st.write("---")
st.write(
    """
- ✔️ 2 year experience delivering data-driven insights in freelance data science.  
- ✔️ Skilled in Python, AI app development, and interactive tools.  
- ✔️ Proficient in multimodal AI systems and data analysis techniques.  
- ✔️ Strong initiative with a proven track record in solo and collaborative projects.  
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader(":material/construction: Skills")
st.write("---")
st.write(
    """
- 👩‍💻 **Programming**: Python (Scikit-learn, Pandas), SQL, AI app development.  
- 📊 **Data Visualization**: Power BI, MS Excel, Plotly.  
- 📚 **Modeling**: Logistic Regression, Linear Regression, Decision Trees.  
- 🗄️ **Databases**: PostgreSQL, MongoDB, MySQL, ChromaDB.  
- 🌐 **App Development**: Interactive tools and multimodal systems.
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader(":material/work: Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Remote Data Science Intern | Hamoye.org**")
st.write("Mar 2024 - Aug 2024")
st.write(
    """
- ► Focused on data visualization, machine learning, and deep learning projects.
- ► Developed and refined visualizations to present complex data in an accessible format, enabling informed decision-making by stakeholders.
- ► Contributed to the creation and optimization of machine learning and deep learning models, applying them to real-world datasets.
- ► Gained hands-on experience in key areas of data science and sharpened technical skills in these specialized domains.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Remote AI and Innovation Intern | Odingo**")
st.write("Feb 2024 - Mar 2024")
st.write(
    """
- ► Explored and implemented advanced AI technologies, including speech-to-text, text-to-speech, and speech-to-speech translation, to transform voice commands into actionable tasks and bridge language barriers.
- ► Utilized Large Language Models (LLMs) to automate workflows, significantly enhancing process speed and accuracy.
- ► Engaged in rapid prototyping and developing efficient automation solutions, while also venturing into new areas such as vision and video AI.
- ► Ensured the smooth operation of digital infrastructure, balancing AI innovation with effective system management.
"""
)

# # --- JOB 3
# st.write('\n')
# st.write("🚧", "**Data Analyst | Chegg**")
# st.write("04/2015 - 01/2018")
# st.write(
#     """
# - ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
# - ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
# - ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
# """
# )


# --- Projects & Accomplishments ---
PROJECTS = {
    "Dermatology Medical Case Search Using ChromaDB - search dermatology cases using text, image, or audio queries for research and clinical support": "https://huggingface.co/spaces/geamxd/Dermatology-Case",
    "DermaSeek - AI-powered dermatology case search engine that enables users to explore cases through text, image, and speech queries, enhancing medical education, research, and healthcare": "https://huggingface.co/spaces/geamxd/DermaSeek",
    # " Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    # "MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}
st.write('\n')
st.subheader(":material/build: Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f":material/trophy:[{project}]({link})")



# --- Feedback ---
# Define the scope and authorize the service account
SCOPES = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS = Credentials.from_service_account_info(st.secrets['gcp_service_account'], scopes=SCOPES)
gc = gspread.authorize(CREDS)


# Open the Google Sheet
SHEET_NAME = "Resume Feedback"

# Open spreadsheet
try:
    sheet = gc.open(SHEET_NAME).sheet1
except Exception as e:
    print(f'Error: {e}')

# Ensure the sheet has headers
headers = ["Timestamp", "Name", "Email", "Message"]
if not ensure_headers(sheet, headers):
    raise ValueError("Sheet headers don't match expected format")

st.write('\n')
st.subheader(":material/contact_page: Contact Me")
st.write('---')

# Form container with custom styling
with st.form("feedback_form", clear_on_submit=True):
    # Input fields with placeholders and validation hints
    name = st.text_input(
        "Name *",
        placeholder="Enter your full name",
        help="Please enter your full name (minimum 2 characters)"
    )
    
    email = st.text_input(
        "Email *",
        placeholder="your.email@example.com",
        help="Enter a valid email address"
    )
    
    message = st.text_area(
        "Message *",
        placeholder="Please share your thoughts...",
        help="Minimum 10 characters",
        height=150
    )
    
    # Submit button with custom styling
    submitted = st.form_submit_button(
        "Submit",
        use_container_width=True,
        type="primary"
    )

if submitted:
    # Input validation
    is_valid = True
    validation_errors = []
    
    # Name validation
    if not name or len(name.strip()) < 2:
        validation_errors.append("Please enter a valid name (minimum 2 characters)")
        is_valid = False
    
    # Email validation using regex
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not email or not re.match(email_pattern, email):
        validation_errors.append("Please enter a valid email address")
        is_valid = False
    
    # Message validation
    if not message or len(message.strip()) < 10:
        validation_errors.append("Please enter a message (minimum 10 characters)")
        is_valid = False

    if is_valid:
        try:
            with st.spinner("Submitting your message..."):
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                sheet.append_row([
                    timestamp,
                    name.strip(),
                    email.lower().strip(),
                    message.strip()
                ])
            
            st.success("✨ Thank you for reaching out! I will get back to you shortly.")
            st.balloons()
            
        except Exception as e:
            st.error("😟 We couldn't submit your message")
            st.error(f"Error details: {str(e)}")
            st.info("Please try again later later.")
    else:
        # Display all validation errors
        for error in validation_errors:
            st.warning(error)
