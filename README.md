# Customer Churn Intelligence Streamlit App

A senior-level Streamlit machine learning product demo for churn prediction, retention prioritization, customer scoring, executive decision support, and production-minded model governance.

**Live demo:** https://ayman-stat-customer-churn-intelligence-streamlit-app-bnhaiu.streamlit.app/  
**Repository:** https://github.com/ayman-stat/customer-churn-intelligence-streamlit

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
- Executive decision layer for revenue exposure, targeting capacity, estimated save rate, and intervention cost
- Governance notes for target/control design, drift monitoring, privacy, and model cards
- Deployment-ready project structure

## Portfolio Value

This project is intentionally designed as a professional portfolio asset. It shows:

- Product thinking beyond notebook-only modeling
- Clear separation between app, data, features, modeling, and explainability
- Reproducible environment setup
- Streamlit UI suitable for recruiters, business stakeholders, and hiring managers
- A business theme aligned with customer intelligence use cases in fitness, telecom, banking, healthcare, and subscription businesses
- Production-minded habits such as modular code, testing, and configurable app structure

## Technology Stack

Core app and analytics:

- **Python:** application logic, data generation, modeling workflow, and reusable modules.
- **Streamlit:** interactive multi-page ML product interface.
- **pandas / numpy:** synthetic customer data, feature processing, scoring tables, and KPI aggregation.
- **scikit-learn:** preprocessing pipelines, classification models, model comparison, and evaluation metrics.
- **Plotly:** executive analytics visualizations and segment risk views.
- **pytest:** smoke tests for data generation and model training.

Senior DS / AI Lead practices demonstrated:

- Decision intelligence and executive KPI framing.
- Model governance through a model card and production controls.
- Target/control experiment design for retention uplift.
- MLOps readiness through deployment notes, modular code, testing, and monitoring roadmap.
- Privacy-safe public demonstration using synthetic data.

## Senior-Level Scope

This is not positioned as a beginner Streamlit tutorial. The app demonstrates how a data science leader would translate model output into operating decisions:

- **Executive KPI layer:** churn rate, high-risk share, exposed revenue, estimated retained revenue, and net value scenario.
- **Model strategy:** compare candidate models with ROC AUC, average precision, recall, and feature importance.
- **Activation logic:** prioritize high-risk customers while respecting intervention capacity and business value.
- **Experiment design:** recommend target/control measurement before claiming campaign uplift.
- **Governance:** call out data lineage, privacy, threshold review, model cards, drift monitoring, and human override paths.
- **Public safety:** use synthetic data only, with no employer, client, customer, member, or third-party data.

Documentation:

- [Architecture brief](docs/ARCHITECTURE.md)
- [Experiment design](docs/EXPERIMENT_DESIGN.md)
- [MLOps and governance roadmap](docs/MLOPS_GOVERNANCE.md)
- [Model card](MODEL_CARD.md)

## Product Architecture

```text
Synthetic Customer Data
        |
        v
Feature Engineering Layer
        |
        v
Candidate Model Training
        |
        v
Risk Scoring + Feature Importance
        |
        v
Executive Decision Layer
        |
        v
Retention Actions + Target/Control Governance
```

## Data Privacy Note

The dataset used in this repository is synthetic and generated inside the application. It does not contain confidential employer, client, customer, member, or third-party data.

## Project Structure

```text
customer-churn-intelligence-streamlit/
├── app.py
├── pages/
│   ├── 1_Data_Explorer.py
│   ├── 2_Model_Lab.py
│   ├── 3_Customer_Scoring.py
│   └── 4_AI_Leadership_Governance.py
├── docs/
│   ├── ARCHITECTURE.md
│   ├── EXPERIMENT_DESIGN.md
│   └── MLOPS_GOVERNANCE.md
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
├── MODEL_CARD.md
├── DEPLOYMENT.md
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

## Deployment

For Streamlit Community Cloud, deploy from `main` with entrypoint `app.py` and select **Python 3.11**
from Advanced settings. See [DEPLOYMENT.md](DEPLOYMENT.md) for the exact settings.

## Quality Check

Run the smoke tests:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest -q
```

## Future Enhancements

- Upload custom CSV data and map target/features
- Add SHAP explanations
- Add MLflow experiment tracking
- Add drift monitoring dashboard
- Add Docker deployment
- Add GitHub Actions quality checks

## Portfolio Positioning

Suggested website card title:

**Customer Churn Intelligence App**

Suggested description:

Interactive senior-level ML product demo for churn prediction, customer scoring, model comparison, retention prioritization, executive value scenarios, and model governance.
