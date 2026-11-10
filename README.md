<div align="center">

# 📊 Autonomous AI Data Analyst

### Intelligent Data Analysis Powered by Agentic AI

**Transform raw datasets into actionable insights using Google Gemini, LangGraph, Pandas, and Streamlit.**

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/Google_Gemini-4285F4?style=for-the-badge&logo=googlegemini&logoColor=white)](https://ai.google.dev/)
[![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge)](https://www.langchain.com/langgraph)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)

![Deployment](https://img.shields.io/badge/Deployment-Streamlit_Cloud-success?style=flat-square)
![Status](https://img.shields.io/badge/Status-Functional_Prototype-blue?style=flat-square)
![Tests](https://img.shields.io/badge/Unit_Tests-3_Passed-brightgreen?style=flat-square)

### 🚀 Try the Application

**[🌐 Live Application](https://autonomous-ai-analyst-ashiwany25.streamlit.app/)** &nbsp; | &nbsp; **[💻 GitHub Repository](https://github.com/Ashiwany25/autonomous-ai-data-analyst)** &nbsp; | &nbsp; **[🐛 Report an Issue](https://github.com/Ashiwany25/autonomous-ai-data-analyst/issues)**

*Upload a CSV or Excel file, let the AI agent analyze it, and explore insights through natural-language questions.*

</div>

---

## 📌 Overview

**Autonomous AI Data Analyst** is an AI-powered data analysis application that combines **large language model reasoning with deterministic Python analytical tools**.

Traditional data analysis often requires writing code, selecting the right analytical methods, creating visualizations, and manually interpreting results.

This application simplifies that process by allowing users to upload a dataset and automatically generate analytical insights.

It provides two complementary workflows:

- **Autonomous Analysis:** The AI agent inspects a dataset, plans analytical tasks, executes supported operations, and generates a business intelligence report.
- **Ask Your Data:** Users ask questions in natural language, and the AI plans and executes relevant analytical operations to produce evidence-supported answers.

The application is built as a **single-agent analytical system**, using LangGraph to coordinate planning and execution.

---

## ✨ Key Features

### 🤖 Autonomous Data Analysis

- Automatic dataset profiling and column identification.
- Gemini-powered analytical planning.
- LangGraph-based agent workflow.
- Data quality assessment.
- Descriptive statistics and grouped analysis.
- Date-based trend analysis for suitable datasets.
- Interactive Plotly visualizations.
- AI-generated business intelligence reports.
- Downloadable analysis results.

### 💬 Ask Your Data

- Ask analytical questions in natural language.
- Break complex questions into multiple supported operations.
- Automatically select analytical tools.
- Perform calculations with Pandas.
- Explain results in understandable language.
- Support questions involving categories, numeric values, and time trends.

### 📂 Flexible Dataset Support

- Upload CSV and Excel files.
- Preview rows and columns.
- Inspect dataset structure.
- Identify numerical, categorical, and date-related columns.
- Explore datasets from different business and analytical domains.

---

## 🎯 Use Cases

| Domain | Example Analysis |
|---|---|
| 🛒 E-Commerce | Sales performance, revenue trends, category comparisons |
| 💰 Finance | Expense breakdowns, financial summaries, monthly trends |
| 🎓 Education | Student performance, subject averages, attendance analysis |
| 📊 Business Intelligence | KPI summaries, operational insights, grouped metrics |
| 📦 Inventory | Product quantities, category comparisons, stock summaries |
| 🧑‍💼 HR Analytics | Department-level statistics and workforce data summaries |

The application is designed for general-purpose tabular analysis, subject to the capabilities of its analytical tools.

---

## 🧠 System Architecture

```text
                 ┌───────────────────────┐
                 │         USER          │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │  Streamlit Interface  │
                 │    CSV / XLSX Input   │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │   Dataset Profiling   │
                 │  Schema & Data Types  │
                 └───────────┬───────────┘
                             │
                   ┌─────────┴─────────┐
                   │                   │
                   ▼                   ▼
        ┌──────────────────┐  ┌──────────────────┐
        │    Autonomous    │  │   Ask Your Data  │
        │     Analysis     │  │                  │
        └────────┬─────────┘  └────────┬─────────┘
                 │                     │
                 ▼                     ▼
        ┌──────────────────┐  ┌──────────────────┐
        │ Gemini Analytical│  │ Gemini Question  │
        │     Planning     │  │     Planning     │
        └────────┬─────────┘  └────────┬─────────┘
                 │                     │
                 ▼                     │
        ┌──────────────────┐           │
        │ LangGraph Agent  │           │
        │     Workflow     │           │
        └────────┬─────────┘           │
                 │                     │
                 └─────────┬───────────┘
                           │
                           ▼
                 ┌───────────────────────┐
                 │ Validated Pandas Tools│
                 │                       │
                 │ • Data Quality        │
                 │ • Summary Statistics  │
                 │ • Categorical Analysis│
                 │ • Grouped Analysis    │
                 │ • Time Series         │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │  Computed Evidence    │
                 │  & Analytical Results │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │ Gemini Interpretation │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │  Insights, Charts &   │
                 │        Reports        │
                 └───────────────────────┘
```

### Why This Architecture?

The system separates **AI reasoning** from **numerical execution**:

1. **Gemini** interprets the analytical objective and plans supported operations.
2. **LangGraph** coordinates the autonomous workflow.
3. **Pandas** performs the actual computations.
4. **Plotly** creates visualizations.
5. **Streamlit** provides the interactive user interface.

This design reduces dependence on unverified numerical calculations generated directly by a language model. However, AI explanations should still be reviewed for accuracy.

---

## 🛠️ Technology Stack

| Technology | Role |
|---|---|
| Python | Core application development |
| Google Gemini 3.1 Flash-Lite | Analytical planning and natural-language explanations |
| LangGraph | Agent orchestration and workflow management |
| Pandas | Data loading, manipulation, and analytical execution |
| NumPy | Numerical processing |
| Plotly | Interactive analytical visualizations |
| Streamlit | Web interface and interactive dashboard |
| Google Colab | Development and experimentation |
| Pytest | Automated analytical unit tests |
| Git & GitHub | Version control and source code management |
| Streamlit Community Cloud | Cloud application deployment |

---

## 🚀 Live Application

The project is deployed on **Streamlit Community Cloud** and can be accessed through a web browser.

### 🌐 [Open Autonomous AI Data Analyst](https://autonomous-ai-analyst-ashiwany25.streamlit.app/)

**Live URL:** https://autonomous-ai-analyst-ashiwany25.streamlit.app/

### How to Use

**Step 1 — Upload a Dataset**

Open the application and upload a supported CSV or Excel file.

**Step 2 — Explore the Dataset**

Review the preview, column details, and available analysis options.

**Step 3 — Choose an Analysis Mode**

Select either:

- **Autonomous Analysis** for AI-guided exploration and reporting.
- **Ask Your Data** for natural-language analytical questions.

**Step 4 — View Results**

Inspect analytical findings, charts, and explanations.

**Step 5 — Download Reports**

Download generated reports when available.

---

## 💬 Example Questions

After uploading a suitable dataset, try asking:

```text
Which category has the highest total sales?
```

```text
Which department has the highest average salary?
```

```text
How have monthly sales changed over time?
```

```text
Which product category has the highest sales
and which has the highest average profit?
```

The application uses supported analytical operations to compute results and then generates a natural-language explanation.

---

## 📁 Project Structure

```text
autonomous-ai-data-analyst/
│
├── app.py
│   └── Streamlit application interface
│
├── analyst_engine.py
│   └── Gemini planning, LangGraph workflow,
│       and analytical tool execution
│
├── requirements.txt
│   └── Python dependencies
│
├── README.md
│   └── Project documentation
│
├── .gitignore
├── .dockerignore
├── .env.example
│
├── Dockerfile
│   └── Container configuration
│
├── COLAB_SETUP_AND_BACKUP.ipynb
│   └── Colab setup and backup notebook
│
├── .streamlit/
│   └── config.toml
│
└── tests/
    └── test_tools.py
```

---

## ⚙️ Local Installation

### Prerequisites

- Python and pip
- Git
- A Google Gemini API key
- Internet access for Gemini API requests

### 1. Clone the Repository

```bash
git clone https://github.com/Ashiwany25/autonomous-ai-data-analyst.git
cd autonomous-ai-data-analyst
```

### 2. Create a Virtual Environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API

Get your API key from:

**[Google AI Studio — API Keys](https://aistudio.google.com/apikey)**

Create a file named:

```text
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

**Important:** Never commit `secrets.toml` or your real API key to GitHub.

### 5. Launch the Application

```bash
streamlit run app.py
```

The application should open locally at:

```text
http://localhost:8501
```

---

## 🧪 Testing & Verification

The application has been tested with sample tabular datasets.

### Functional Testing

| Component | Status |
|---|---|
| Streamlit application loading | ✅ Passed |
| CSV dataset upload | ✅ Passed |
| Dataset preview | ✅ Passed |
| Gemini API connectivity | ✅ Passed |
| Natural-language question answering | ✅ Passed |
| Multi-step analytical questions | ✅ Passed |
| Autonomous analytical workflow | ✅ Passed |
| Analytical evidence generation | ✅ Passed |
| Business intelligence reporting | ✅ Passed |
| Interactive visualizations | ✅ Passed |
| Report downloading | ✅ Passed |
| Basic analytical unit tests | ✅ 3 passed |

### Run Automated Tests

```bash
python -m pytest -v tests/test_tools.py
```

**Previously recorded result:** 3 tests passed.

These results demonstrate that the tested workflows function correctly on the evaluated sample data. They do not establish comprehensive production readiness or guarantee accurate results for every dataset.

---

## ☁️ Cloud Deployment

The application is hosted on **Streamlit Community Cloud**.

| Configuration | Value |
|---|---|
| Hosting Platform | Streamlit Community Cloud |
| GitHub Repository | [Ashiwany25/autonomous-ai-data-analyst](https://github.com/Ashiwany25/autonomous-ai-data-analyst) |
| Branch | `main` |
| Entry Point | `app.py` |
| Dependency File | `requirements.txt` |
| API Configuration | Streamlit Secrets |

### Deployment Steps

1. Fork or clone this repository into your GitHub account.
2. Visit [Streamlit Community Cloud](https://share.streamlit.io/).
3. Create a new application from your repository.
4. Select `main` and `app.py`.
5. Add `GEMINI_API_KEY` under **Advanced settings → Secrets**.
6. Deploy your application.

The actual Gemini API key should never appear in committed source files.

---

## 🔐 Security & Reliability

The project incorporates several precautions:

- **Secret management:** Gemini credentials are supplied through Streamlit Secrets or supported environment configuration.
- **Git exclusions:** `.gitignore` excludes common secret files, local datasets, and generated artifacts.
- **Controlled analytical execution:** The application uses predefined Pandas analytical tools instead of executing arbitrary AI-generated Python code.
- **Validated tool inputs:** Supported analytical requests are checked against available dataset columns and tool requirements.
- **Bounded workflows:** The autonomous agent limits analytical execution steps.
- **Session-based data handling:** Uploaded datasets are handled within the interactive application session.

### Responsible Usage

Avoid uploading confidential, regulated, or sensitive personal data unless you have the necessary permissions and have assessed the application's data-handling requirements.

**Note:** The application is a functionally tested prototype, not a security-audited production service.

---

## ⚠️ Current Limitations

- Designed primarily for general-purpose tabular datasets.
- Advanced domain-specific statistical methods may require additional tooling.
- Some analytical questions cannot be represented by the existing tools.
- Multi-step questions and autonomous workflows have execution limits.
- AI-generated explanations may occasionally contain inaccuracies.
- Gemini requests depend on API availability and quota.
- Application performance depends on dataset size and hosting resources.

---

## 🗺️ Development Roadmap

### ✅ Implemented

- ✅ CSV and Excel upload support
- ✅ Dataset profiling and structural inspection
- ✅ Gemini-powered analytical planning
- ✅ LangGraph-based autonomous workflow
- ✅ Predefined Pandas analytical tools
- ✅ Multi-step natural-language question answering
- ✅ Interactive Plotly visualizations
- ✅ Business intelligence report generation
- ✅ Downloadable analysis reports
- ✅ Streamlit Community Cloud deployment
- ✅ Initial functional and unit testing

### 🚧 Planned Improvements

- 🔲 Additional analytical tools and statistical methods
- 🔲 Stronger numerical result verification
- 🔲 Improved analytical error recovery
- 🔲 Enhanced chart selection and customization
- 🔲 PDF report generation
- 🔲 Performance optimization for larger datasets
- 🔲 Persistent analysis history
- 🔲 Expanded automated testing and edge-case coverage

---

## 🤝 Contributing

Contributions, bug reports, and enhancement suggestions are welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Add or update tests where appropriate.
5. Open a pull request describing the changes.

For bugs or feature ideas, use the [GitHub Issues page](https://github.com/Ashiwany25/autonomous-ai-data-analyst/issues).

---

## 👨‍💻 Developer

**Ashiwany**

*Aspiring Data Analyst | AI/ML Enthusiast | Software Developer*

Interested in building practical solutions using **Artificial Intelligence, Data Analytics, Machine Learning, and modern Python frameworks**.

**[GitHub Profile](https://github.com/Ashiwany25)** | **[LinkedIn](https://www.linkedin.com/in/ashiwany-kumar-b30b20325/)** | **[Live Project](https://autonomous-ai-analyst-ashiwany25.streamlit.app/)**

---

<div align="center">

### ⭐ If you find this project useful, consider giving it a star!

**Built with Python, Google Gemini, LangGraph, Pandas & Streamlit**

*Turning data into insights, one question at a time.*

**[🚀 Explore Live Application](https://autonomous-ai-analyst-ashiwany25.streamlit.app/)** | **[📂 View Source Code](https://github.com/Ashiwany25/autonomous-ai-data-analyst)**

</div>
