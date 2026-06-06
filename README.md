# Customer Churn Intelligence Streamlit App

A portfolio-grade Streamlit machine learning product for churn prediction, retention analytics, customer scoring, and business decision support.

## Project Goal

Build an interactive application that demonstrates the full workflow expected from a Senior Data Scientist, ML Engineer, or Analytics Lead:

- Business framing for churn and retention
- Synthetic customer-level data generation for safe public demonstration
- Exploratory analytics and segment profiling
- Feature engineering
- Baseline and advanced ML model comparison
- Model evaluation with business-friendly metrics
- Explainability using feature importance and permutation importance
- Individual customer scoring
- Retention action recommendations
- Deployment-ready project structure

## Portfolio Value

This project is intentionally designed as a professional portfolio asset. It shows:

- Product thinking beyond notebook-only modeling
- Clear separation between app, data, features, modeling, and explainability
- Reproducible environment setup
- Streamlit UI suitable for recruiters, business stakeholders, and hiring managers
- A business theme aligned with customer intelligence use cases in fitness, telecom, banking, healthcare, and subscription businesses
- Production-minded habits such as modular code, testing, and configurable app structure

## Data Privacy Note

The dataset used in this repository is synthetic and generated inside the application. It does not contain confidential employer, client, customer, member, or third-party data.

## Project Structure

```text
customer-churn-intelligence-streamlit/
├── app.py
├── pages/
│   ├── 1_Data_Explorer.py
│   ├── 2_Model_Lab.py
│   └── 3_Customer_Scoring.py
├── .streamlit/
│   └── config.toml
├── src/
│   ├── config.py
│   ├── data.py
│   ├── features.py
│   ├── modeling.py
│   ├── explainability.py
│   └── utils.py
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── notebooks/
├── assets/
├── tests/
├── requirements.txt
├── .env.example
├── .gitignore
└── scripts/
    └── setup.ps1
```

## Quick Start

From this directory:

```powershell
.\scripts\setup.ps1
.\.venv\Scripts\Activate.ps1
streamlit run app.py
```

If the environment is already created:

```powershell
.\.venv\Scripts\Activate.ps1
streamlit run app.py
```

## Quality Check

Run the smoke tests:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

## Future Enhancements

- Upload custom CSV data and map target/features
- Add SHAP explanations
- Add MLflow experiment tracking
- Add drift monitoring dashboard
- Add model card page
- Add Docker deployment
- Add GitHub Actions quality checks

## Portfolio Positioning

Suggested website card title:

**Customer Churn Intelligence App**

Suggested description:

Interactive Streamlit ML product for churn prediction, retention analytics, customer scoring, model explainability, and business decision support.
