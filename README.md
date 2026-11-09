
# 📊 Autonomous AI Data Analyst

### Transform Raw Data into Actionable Insights with Agentic AI

An AI-powered data analytics application built using Google Gemini,
LangGraph, Pandas, Plotly, and Streamlit.

**Status:** Ready for deployment

---

## 🌟 About the Project

Autonomous AI Data Analyst is an Agentic AI project designed to
automate exploratory data analysis, generate meaningful insights,
and answer natural-language questions about datasets.

Users can upload CSV or Excel files and explore their data without
writing analytical code.

## 🚀 Key Features

- 🤖 Autonomous data analysis using Gemini and LangGraph
- 📊 Automatic dataset profiling and data quality checks
- 💬 Ask Your Data: natural-language question answering
- 🧠 Multi-step analytical planning and execution
- 📈 Interactive Plotly visualizations
- 📄 AI-generated business intelligence reports
- 📁 CSV and Excel file support

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Google Gemini | AI planning and explanations |
| LangGraph | Agent workflow orchestration |
| Pandas | Data processing and analysis |
| NumPy | Numerical computations |
| Plotly | Interactive visualizations |
| Streamlit | Web application |
| Google Colab | Development and testing |
| GitHub | Version control |

## 🧠 How It Works

1. Upload a CSV or Excel dataset.
2. The application analyzes the dataset structure.
3. Select Autonomous Analysis or Ask Your Data.
4. Gemini plans appropriate analytical operations.
5. Python and Pandas perform the calculations.
6. The application displays insights, charts, and reports.

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

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Ashiwany25/autonomous-ai-data-analyst.git
cd autonomous-ai-data-analyst
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a local `.streamlit/secrets.toml` file:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Run the application:

```bash
streamlit run app.py
```

## ☁️ Deployment

This project is prepared for deployment on Streamlit Community Cloud.

1. Connect your GitHub account to Streamlit.
2. Select `Ashiwany25/autonomous-ai-data-analyst`.
3. Choose the `main` branch.
4. Set the main file path to `app.py`.
5. Configure `GEMINI_API_KEY` in Streamlit Secrets.
6. Deploy the application.

**Live App:** Coming soon — deployment pending.

## 🔐 Security

- API keys are not stored in the repository.
- Credentials should be configured using Streamlit Secrets.
- Sensitive files are excluded using `.gitignore`.
- Never upload private datasets or authentication tokens.

## 🔮 Future Improvements

- Advanced data visualizations
- Improved analytical accuracy
- Automatic error recovery
- PDF report generation
- Additional statistical tools
- Better support for large datasets

## ⚠️ Limitations

This is a prototype intended for general-purpose tabular data
analysis. AI-generated reports may contain inaccuracies and should
be reviewed before important decisions.

---

### 🎯 Project Goal

To make data analysis easier and more accessible by combining
Generative AI, Agentic AI, and automated Python-based analytics.

**Built with Python, Gemini, LangGraph, and Streamlit.**
