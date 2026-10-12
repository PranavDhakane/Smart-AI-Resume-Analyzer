# 🚀 Smart AI Resume Analyzer

<div align="center">

### Your Career. Your Skills. Your Next Opportunity.

**An AI/ML-focused resume analysis project by Pranav Dhakane**

[![GitHub](https://img.shields.io/badge/GitHub-PranavDhakane-181717?style=for-the-badge&logo=github)](https://github.com/PranavDhakane)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/pranav-dhakane-288634327/)

</div>

---

## 👨‍💻 About Me

Hi! I'm **Pranav Dhakane**, a final-year B.Tech student specializing in Computer Science and Engineering with Artificial Intelligence and Machine Learning (CSE AIML).

I'm passionate about programming, problem-solving, automation, and building practical applications using modern technologies.

This project is part of my journey toward becoming a skilled software engineer and developing useful AI-powered solutions.

- 🎓 **Education:** B.Tech — CSE AIML
- 💻 **Interests:** Artificial Intelligence, Machine Learning, Java, and Software Development
- 🚀 **Current Project:** Smart AI Resume Analyzer
- 🌱 **Currently Exploring:** Python, FastAPI, SQL, and AI/ML concepts
- 🎯 **Goal:** Build practical, reliable, and impactful technology

## 🎯 About the Project

Smart AI Resume Analyzer is a resume-processing application designed to extract information from PDF resumes and organize important details such as contact information, education, technical skills, projects, experience, and certifications.

The goal is to develop a useful foundation for resume analysis and eventually help students and job seekers understand and improve their resumes.

## ✨ Key Features

- 📄 **PDF Upload:** Upload a resume in PDF format.
- 📝 **Text Extraction:** Extract text from PDF documents.
- 🔍 **Resume Parsing:** Identify common resume details using rule-based parsing.
- 🛠️ **Skill Detection:** Recognize technical skills using a predefined skills dictionary.
- 🎓 **Education Extraction:** Identify education-related information.
- 💼 **Project and Experience Extraction:** Detect relevant sections of a resume.
- ⚡ **REST API:** Process resume uploads and analysis requests through FastAPI.
- 🧪 **Testing:** Verify parsing behavior and application functionality with automated tests.

*Note: Features such as AI-generated recommendations, ATS scoring, job-description matching, and advanced analytics should be marked as available only after they have been implemented and tested.*

## 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| FastAPI | Backend REST API |
| PyMuPDF | PDF text extraction |
| SQLAlchemy | Planned database integration |
| MySQL | Planned persistent storage |
| HTML | Frontend structure |
| CSS | Frontend styling |
| JavaScript | Frontend interactions |
| Pytest | Automated testing |
| Git & GitHub | Version control and collaboration |

## ⚙️ How It Works

1. **Upload:** The user submits a PDF resume.
2. **Validate:** The backend validates the file type and size.
3. **Extract:** Text is extracted from the PDF.
4. **Analyze:** The parser identifies available resume information.
5. **Return Results:** The API returns structured analysis data.

## 📁 Project Structure

```text
Smart-AI-Resume-Analyzer/
├── backend/
│   ├── app/
│   │   └── main.py
│   ├── services/
│   │   └── pdf_service.py
│   ├── tests/
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
├── README.md
└── .gitignore
```

*The structure above is illustrative. Update it to match the actual files and folders in your repository.*

## 💻 Getting Started

### Prerequisites

Install the following:

- Python 3.12 or a compatible version
- Git
- A code editor such as Visual Studio Code
- MySQL Server and MySQL Workbench when database integration is configured

### 1. Clone the repository

```bash
git clone https://github.com/PranavDhakane/Smart-AI-Resume-Analyzer.git
cd Smart-AI-Resume-Analyzer
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt instead:

```bat
venv\Scripts\activate.bat
```

### 3. Install dependencies

Navigate to the backend directory if the requirements file is located there:

```bash
cd backend
pip install -r requirements.txt
```

### 4. Start the backend

From the backend directory, run:

```bash
uvicorn app.main:app --reload
```

Open the following URLs:

- API base: http://127.0.0.1:8000
- API documentation: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/api/health

Keep the backend terminal running while testing the application.

### 5. Run the frontend

Open `frontend/index.html` in your browser, or use a local development server if your frontend setup requires one.

## 🧪 Testing

Run the project's automated tests from the appropriate backend directory:

```bash
pytest
```

Tests help verify that resume extraction and parsing work as expected.

## 🔐 Security and Privacy

Resumes may contain sensitive personal information. This project follows these development principles:

- Do not commit real resumes or confidential personal information to GitHub.
- Never upload API keys, passwords, or database credentials.
- Keep environment files such as `.env` out of version control.
- Use anonymized or sample resumes for testing.
- Validate uploaded files before processing them.
- Handle resume data responsibly.

## 🗺️ Future Improvements

The following are potential enhancements, not claims of completed functionality:

- 🤖 AI-powered resume feedback
- 📊 ATS-style resume analysis
- 🎯 Resume-to-job-description matching
- 🔑 Keyword gap analysis
- 📈 Skills analysis and recommendations
- 🗄️ Persistent resume records using MySQL
- 📄 Downloadable analysis reports
- 🌐 Deployment as a web application

## 🤝 Contributing

Suggestions, bug reports, and improvements are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make and test your changes.
4. Commit your changes with a descriptive message.
5. Push your branch.
6. Open a Pull Request.

## 📬 Connect With Me

<div align="center">

**Pranav Dhakane**

[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com/PranavDhakane)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/pranav-dhakane-288634327/)

</div>

---

<div align="center">

### ⭐ Learn. Build. Innovate.

Built with dedication by **Pranav Dhakane** as part of my software development and AI/ML learning journey.

</div>
