# 📊 Autonomous AI Data Analyst — Portable Backup

A self-contained, secret-free, **reconstructed portable release** of the Autonomous AI Data Analyst project (Streamlit + LangGraph + Gemini + Pandas + Plotly).

> **Important:** This package was reconstructed from the application's architecture and features. It is **not an exact export of the current private GitHub repository or the original Colab development notebook**. Keep your original notebook/repository as the authoritative source. No credentials, personal datasets, or actual `.streamlit/secrets.toml` file are bundled.

## 📦 What's included

- `app.py` — Streamlit UI, CSV/XLSX uploads, Autonomous Analysis and Ask Your Data.
- `analyst_engine.py` — bounded LangGraph workflow, analytical tools, Gemini planning and explanations.
- `requirements.txt`, `.gitignore`, `.dockerignore`, `.env.example` — safe configuration and dependencies.
- `Dockerfile` — deployment option for Hugging Face Spaces (Docker) or similar hosts.
- `tests/` — simple tool checks.
- `COLAB_SETUP_AND_BACKUP.ipynb` — import the ZIP, run notebook analysis, back up to Drive, optionally push code to GitHub.

## 💻 Run locally

1. Unzip the archive.
2. `pip install -r requirements.txt`
3. Configure `GEMINI_API_KEY` in your environment or locally in **untracked** `.streamlit/secrets.toml`:

   ```toml
   GEMINI_API_KEY = "your_personal_api_key"
   ```

4. `streamlit run app.py`
5. Upload a CSV or XLSX file (up to 15 MB) and pick a mode.

## ☁️ Colab and Drive

1. Open `COLAB_SETUP_AND_BACKUP.ipynb` in Google Colab.
2. Run the first cell to upload **this ZIP** and extract it.
3. Run the dependency cell.
4. Use the notebook's Gemini test cell (enter your key in the hidden input; it stays in Colab's memory, not the repository).
5. Run the Drive backup cell and authorize the mount. It copies the ZIP into `MyDrive/AI_Data_Analyst_Backups`.
6. Optional: use the final **GitHub push** cell. It asks for a fine-grained GitHub token with **Contents: Read and write** access limited to the selected repo. It uses a temporary `GIT_ASKPASS` helper; the token is not written into Git history or included in the ZIP. **Revoke the token when you're finished**.

Colab is best for running notebook analysis, **not** for permanent public website hosting.

## 🚀 Deploy without Streamlit Community Cloud

### GitHub Pages cannot host this Python application

GitHub Pages only serves **static** HTML, CSS and JavaScript. This project needs a persistent Python server and an API secret. Do not put the Gemini key into JavaScript in a GitHub Pages site.

### Option A — Hugging Face Spaces (Docker)

1. Create a Space at https://huggingface.co/new-space and select **Docker** as SDK.
2. Add the package files, including `Dockerfile` and `requirements.txt`, to the Space's source repo.
3. Set a Space **Secret** named `GEMINI_API_KEY` (never a normal code file or public variable).
4. The Dockerfile starts Streamlit on port `7860`.
5. Verify whether the Space is public or private and check hosting quotas. Free hosting can still sleep or change availability.

**Warning:** Public Spaces expose their source repository. Your code is designed to be publishable, but double-check that no secret is included before uploading.

### Option B — Render Web Service

1. Connect the GitHub repository at https://dashboard.render.com/.
2. Choose a **Web Service** (not a static site).
3. Build command: `pip install -r requirements.txt`
4. Start command: `streamlit run app.py --server.address 0.0.0.0 --server.port $PORT --server.headless true`
5. Set environment variable `GEMINI_API_KEY` in Render's Secret/Environment settings.
6. Deploy. **Render's free web services sleep after ~15 minutes idle**, so opening them may still be slow.

**Speed note:** Switching from Streamlit Community Cloud to another free hosting service does not automatically eliminate startup delays. An always-on paid plan is usually needed for predictable cold-start performance.

## 🔒 Security checklist before publishing your GitHub repository

- [ ] No literal Gemini API keys, GitHub tokens, `.env` files or `.streamlit/secrets.toml` committed.
- [ ] Search **all Git commits** for old keys. `.gitignore` does not remove secrets already committed.
- [ ] If a secret was ever exposed, **revoke and replace it** before publishing.
- [ ] Verify `.ipynb` cells and outputs contain no secret values or personal data.
- [ ] Keep sensitive datasets off public repositories.
- [ ] Restrict GitHub token permissions to the one repository and revoke after pushing.
- [ ] Keep Gemini server-side. A public app can consume your free-tier API quota; consider access controls or rate limits.
- [ ] Decide whether hosted app traffic is permitted to send dataset metadata / analytical results to Gemini.

## ⚠️ Limitations

General-purpose tabular data only; tool plans may fail; result sets are limited; Gemini explanations are not independently audited. Not suitable for confidential data or high-stakes decisions without stronger privacy safeguards and numerical verification.

## Links

- Original private project: https://github.com/Ashiwany25/autonomous-ai-data-analyst
- Previously deployed app: https://autonomous-ai-data-analyst-kmbpc8frppj6wdhroqziof.streamlit.app/
