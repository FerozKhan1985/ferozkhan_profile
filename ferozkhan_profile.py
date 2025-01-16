import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Feroz Khan, AI Engineer.
##### *Portfolio* 
''')

image = Image.open('dp.png')
st.image(image, width=150)

st.markdown('## Professional Summary', unsafe_allow_html=True)
st.info('''
- I am Feroz Khan, a dynamic professional with a Master of Business Administration (MBA) in Accounting & Finance and Management Information Systems honors, complemented by over 14 years of experience as an IT Assistant in the Government of Pakistan. My career journey reflects a seamless transition into the exciting field of Artificial Intelligence (AI), driven by a passion for innovation and technological advancement.
- With expertise in AI, Machine Learning (ML), and Deep Learning (DL), I develop intelligent solutions, including Chatbots and Retrieval-Augmented Generation (RAG) systems, leveraging Python as my core programming language. My skills extend to Exploratory Data Analysis (EDA), where I transform complex datasets into actionable insights, empowering data-driven decision-making and predictive modeling.
- My AI journey is marked by a commitment to creating impactful, real-world applications by integrating advanced machine learning algorithms and deep learning frameworks. I am eager to contribute to transformative projects, collaborate with forward-thinking teams, and shape the future of technology through innovation.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse justify-content-center" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Master of Business Administration (MBA)** (Finance & MIS), *Virtual University*, Government of Pakistan',
'2008-2010')
st.markdown('''
- GPA: `3.41`
- Graduated from Virtual University of Pakistan with a focus on financial analysis, strategic management, and IT systems integration.
- Developed an "Online Shopping Cart" website as a final-year project, utilizing ASP to create an interactive e-commerce platform, showcasing strong skills in web development and problem-solving.
''')

txt('**Legum Baccalaureus (LLB)** (Bachelor of Laws), *University of Peshawar*, Pakistan',
'2015-2017')
st.markdown('''
- GPA: `3.65`
- Graduated with First Class Honors.
''')

#####################
st.markdown('''
## Artificial Intelligence (AI)
''')

txt('**Computer Vision** (Introduction to Computer Vision & Image Processing), *IBM*, coursera.org',
'Dec 9th, 2024')
st.markdown('''
- Introduction to Computer Vision
- Image Processing with OpenCV & Pillow
- Machine Learning Image Classification
- Neural Networks & Deep Learning form Image Classification
- Object Detection
- Project Case: Not Quite a Self-Driving Car – Traffic Sign Classification.
 ''')

txt('**AI for Medicine** (Specialization), *Deeplearning.AI*, coursera.org',
'Nov 24th, 2024')
st.markdown('''
- AI for Medical Diagnosis
- AI for Medical Prognosis
- AI for Medical Treatment
''')

txt('**Deep Learning** (Specialization), *Deeplearning.AI*, coursera.org',
'Oct 31st, 2024')
st.markdown('''
- Neural Networks & Deep Learning
- Improving Deep Learning Networks: Hyper Parameter Tuning,  Regularization, and Optimization.
- Structuring Machine Learning Projects.
- Convolutional Neural Netwoks (CNN)
- Sequence Models
''')

txt('**Generative AI for everyone** (Specialization), *Deeplearning.AI*, coursera.org',
'Aug 10th, 2024')
st.markdown('''
- Introduction
- Generative AI Projects
- Generative AI in work and life
- AI and Society
''')

txt('**AI for everyone** (Specialization), *Deeplearning.AI*, coursera.org',
'Aug 7th, 2024')
st.markdown('''
- What is AI
- Building AI Projects
- AI in your Company
- AI and Society
''')

txt('**Machine Learning** (Specialization), *Stanford University*, deeplearning.ai | coursera.org',
'Jul 16th, 2024')
st.markdown('''
- Supervised Machine Learning: Regression & Classification
- Advanced Learning Algorithms 
- Un-Supervised Learning, Recommenders, Reinforcement Learning
''')

txt('**AI Python**| deeplearning.ai |',
'2024')
st.markdown('''
- Basics of AI Python Coding 
- Automating Tasks with Python
- Working with your own data and documents in Python
- Extending Python with packages and APIs
''')

txt('**LangChain chat with your data**,| deeplearning.ai |',
'2024')
st.markdown('''
- Document Loading, Splitting, Vector Stores, Embedding, Retrieval, Q&A, Chat
''')

txt('**LangChain for LLM Application Development**,| deeplearning.ai |',
'2024')
st.markdown('''
- Models, Prompts & parsers, Memory, Chains, Q&A, Evaluation, Agents
''')

##########END AI


st.markdown('''
## Work Experience
''')

txt('#### **Computer Assistant** | Government of Pakistan |',
'2010-Current')
st.markdown('''
- Responsible to Commissioner Malakand Division in discharging duties and functions. 
- Dealing with all types of Development-related correspondence. 
- Conducting and drafting different meetings and their minutes. 
- Preparation of presentation and brief for Commissioner. 
- Community-Driven Local Development (CDLD) activities. 
- Guide/support Junior/New Employee. ▪ Plan and arrange all work- related activities in an effective, timely, and efficient manner. 
- Maintenance of all records related to the work assigned. 
- Contributes to team effort by accomplishing related results as needed. 
- Compliance to all applicable policies, procedures and work instructions as per rules and regulations. 
- Timely reporting.
- Compliance with contractual agreements and cordial work relationships with colleagues. 
- Any other task assigned by the Commissioner from time to time.''')

txt('#### **Internee Officer** | Bank Alfalah (Pvt) Ltd |',
'Aug 2008-Sep 2008')
st.markdown('''
- Communicating with high-value customers regarding account management. 
- Performs tasks like a regular employee or assists in a supporting role.
- Assist employees in completing their day-to-day banking tasks to develop practical and interpersonal skills that are crucial for their specific job roles 
- Work under the department manager, who assigns their daily duties and tracks and monitors their progress. As part of their day-to-day training and duties, banking interns may assist in: 
    - Data collection 
    - Financial analysis 
    - Data modeling 
    - Industry research 
    - Documentation 
    - Solution development and delivery 
    - Financial evaluation
''')

txt('#### **Internee Officer** | Finance & Planning Department Govt: of Pakistan |',
'2008')
st.markdown('''
- In Finance wing, Responsible for district budgeting (Salary & Non-Salary) of the devolved departments and approval of the Annual Developmental Programme (ADP) from the Zilla Council. 
- Keeps record of the monthly expenditure of both (Salary & Non-Salary Budget 
- Monthly receipts of the departments reconciled by the District Accounts Officer. 
- Re-Appropriation of the Budget and Revised Budget for the district. 
- In Planning Wing, responsible for policy decision-making stakeholder in the field of development in the district. 
- Responsible for the implementation and monitoring of the overall development plans of the district.
''')

txt('#### **Internee Officer** | Invest Capital & Security (Pvt) Ltd |',
'Nov 2007-Dec 2007')
st.markdown('''
- Responsible for Managing the implemented InvestCap (Pvt) Ltd Standards and for delivering and maintaining a safe and secure working environment for all the staff. 
- Incident reporting and investigating all incidents including near misses and establish cause and corrective action to avoid further recurrence. 
- Carry out calibration, on a regular basis. 
- Preparation of SOPs and their implementation. 
- Conducting daily inspection along with Executive Chef
''')
############################

txt('**Master Classes and Activities**, Certificates and Participations',
'2024-Present')
st.markdown('''
- Certified **Adcance Excel for Business Analytics** `using` **Excel** (10th  December, 2024)
- Certified **Zomato Data Analysis** `using` **Python** (28th October, 2024)
- Certified **Excel Fndamentals for Data Analytics** `using` **Excel** (7th October, 2024)
- Certified **Data Analysis** `using` **PowerBI** (17th September, 2024)
- Certified **Python Fundamentals** `using` **Python** (22th August, 2024)
- Certified **Food Delivery Cost Analysis** `using` **Python** (28th July, 2024)
- Certified **Predictive Data Analytics** `using` **Machine Learning** (20th July, 2024)
- Certified **Data Visualisation** `using` **PowerBI** (13th July, 2024)
- Certified **Data Analytics** career with **`SQL`** (6th July) 
- Certified **Forcast ICC T20 World Cup Champions** `using` **Machine Learning** (28th June, 2024).
''')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `C++`')
txt3('Data processing/wrangling', '`Pandas`, `Numpy`,`MySQL`')
txt3('Data visualization', '`Matplotlib`, `Seaborn`, `Plotly`')
txt3('Machine Learning', '`Scikit-Learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Accounting', '`PeachTree`,`Tally`,`QuickBook`')
txt3('Model deployment', '`Streamlit`, `Gradio`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/feroz-khan85')
txt2('Face Book', 'https://www.facebook.com/ferozkhan1985/')
txt2('GitHub', 'https://github.com/FerozKhan1985/')
txt2('Kaggle', 'https://www.kaggle.com/ferozkhan85')
txt2('Email', 'ferozkhan85.ai@gmail.com')
txt2('WhatsApp', 'https://wa.me/923338059934')

######################

with open("feroz_khan_profile.pdf", "rb") as pdf_file:
       pdf_bytes = pdf_file.read()
st.write("###")

    # Download CV button
st.download_button(label="📄 Download my CV", data=pdf_bytes, file_name="Feroz_Khan_cv.pdf", mime="application/pdf",)
st.write("######")
st.write(f"""<div class="subtitle" style="text-align: center;">🌾🌻 Have A Wonderfull Day!!! 🌻🌾</div>""", unsafe_allow_html=True)


