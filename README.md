# 📊 Autonomous AI Data Analyst

### Transform Raw Data into Actionable Insights with Agentic AI

An intelligent, dataset-independent AI-powered analytics application built using **Google Gemini, LangGraph, Pandas, Plotly, and Streamlit**.

**Project Status:** Deployed and functionally tested prototype.

---

## 🌟 About the Project

**Autonomous AI Data Analyst** is an Agentic Generative AI application designed to automate exploratory data analysis, generate meaningful business insights, and answer natural-language questions about uploaded datasets.

The application combines Gemini-powered analytical planning with validated Python and Pandas tools, helping users explore their data without writing analytical code.

## 🚀 Key Features

### 🤖 1. Autonomous Data Analysis

- Automatic dataset profiling and column identification.
- AI-driven analytical planning using Google Gemini.
- LangGraph-based agent workflow orchestration.
- Data quality checks and statistical analysis.
- Interactive Plotly visualizations.
- AI-generated business intelligence reports.
- Downloadable analysis reports.

### 💬 2. Ask Your Data

- Natural-language question answering.
- Multi-step analytical planning.
- Automatic selection of appropriate analytical tools.
- Python-based calculations using Pandas.
- Evidence-based responses.

**Example Questions:**

- Which category has the highest total sales?
- Which department has the highest average salary?
- How have monthly sales changed over time?
- Which category has the highest sales and average profit?

### 📁 3. Dataset Support

- CSV and Excel uploads.
- Automatic identification of numeric, categorical, and date columns.
- Dataset preview and structural information.
- Support for different tabular-data domains.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Google Gemini | AI planning and explanations |
| LangGraph | Agent workflow orchestration |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Plotly | Interactive visualizations |
| Streamlit | Web application |
| Google Colab | Development and testing |
| GitHub | Version control |
| Streamlit Community Cloud | Application deployment |

---

## 🧠 System Architecture

```text
             USER
               |
               v
       Upload CSV / Excel
               |
               v
       Dataset Profiling
               |
               v
        Select AI Mode
               |
        +------+------+
        |             |
        v             v
   Autonomous      Ask Your
    Analysis         Data
        |             |
        v             v
   Gemini Agent    Question
    Planning       Planning
        |             |
        v             v
   LangGraph       Multi-Step
    Workflow       Tool Execution
        |             |
        +------+------+
               |
               v
      Pandas Analytical Tools
               |
               v
       Computed Results
               |
               v
       Gemini Explanation
               |
               v
       Insights & Reports
```

The application uses AI to plan analyses and Pandas to perform actual calculations. It does not execute arbitrary AI-generated Python code.

---

## 📁 Project Structure

```text
autonomous-ai-data-analyst/
├── app.py
├── analyst_engine.py
├── requirements.txt
├── README.md
├── .gitignore
├── .dockerignore
├── .env.example
├── Dockerfile
├── COLAB_SETUP_AND_BACKUP.ipynb
├── .streamlit/
│   └── config.toml
└── tests/
    └── test_tools.py
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Ashiwany25/autonomous-ai-data-analyst.git
cd autonomous-ai-data-analyst
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Gemini API

Obtain an API key from [Google AI Studio](https://aistudio.google.com/apikey).

Create a local `.streamlit/secrets.toml` file containing:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Never commit your actual API key to GitHub.

### 4. Run the Application

```bash
streamlit run app.py
```

---

## ☁️ Deployment

The application has been deployed using **Streamlit Community Cloud**.

**Deployment Configuration:**

- GitHub repository: `Ashiwany25/autonomous-ai-data-analyst`
- Branch: `main`
- Main application file: `app.py`
- API credentials: Streamlit Secrets

A live application URL can be added here once confirmed for the new deployment.

---

## 🧪 Testing & Verification

The application has undergone functional testing using sample datasets.

| Test | Result |
|---|---|
| Application loading | ✅ Passed |
| CSV dataset upload | ✅ Passed |
| Dataset preview | ✅ Passed |
| Gemini API connection | ✅ Passed |
| Multi-step question answering | ✅ Passed |
| Autonomous analysis workflow | ✅ Passed |
| Analytical evidence generation | ✅ Passed |
| Business intelligence reporting | ✅ Passed |
| Plotly visualization | ✅ Passed |
| Report download | ✅ Passed |
| Basic analytical unit tests | ✅ 3 passed |

These tests confirm functionality for the evaluated examples. They do not guarantee correctness across every dataset or question.

---

## 🔐 Security

- Gemini API keys are stored outside the GitHub repository.
- Streamlit Secrets is used for deployed API credentials.
- `.gitignore` excludes common secret files and local datasets.
- The application uses predefined analytical tools rather than arbitrary model-generated Python execution.

Users should avoid uploading confidential datasets without appropriate authorization.

---

## ⚠️ Current Limitations

- Supports general-purpose tabular datasets rather than every possible data format.
- Some advanced statistical and domain-specific questions may not be supported.
- Multi-step analytical questions have task limits.
- AI-generated explanations may contain inaccuracies.
- API availability depends on Gemini service limits and quotas.
- Hosting performance depends on Streamlit Community Cloud availability.

---

## 🔮 Future Enhancements

### ✅ Completed Features

- ✅ Universal dataset profiling
- ✅ Autonomous analytical planning
- ✅ LangGraph agent workflow
- ✅ Multi-step question answering
- ✅ Interactive Streamlit dashboard
- ✅ CSV and Excel support
- ✅ Cloud deployment
- ✅ Basic functional testing

### 🚀 Planned Improvements

- 🔲 Advanced visualization options
- 🔲 Automatic analytical error recovery
- 🔲 Stronger numerical verification
- 🔲 Automated PDF report generation
- 🔲 Improved large-dataset support
- 🔲 Persistent analysis history

---

## 🎯 Project Objective

To make data analysis more accessible by building an intelligent AI assistant capable of understanding datasets, planning analytical operations, executing computations, and communicating meaningful insights in natural language.

---

<div align="center">

### ⭐ Built with Python, Gemini, LangGraph & Streamlit

**Turning data into insights, one question at a time.**

</div>
