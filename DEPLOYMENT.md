# Streamlit Community Cloud Deployment

Use these settings when deploying this app on Streamlit Community Cloud.

## Required Settings

- Repository: `ayman-stat/customer-churn-intelligence-streamlit`
- Branch: `main`
- Main file path: `app.py`
- Python version: `3.11.4`

## Why Python 3.11.4

The app uses the scientific Python stack: `numpy`, `pandas`, `scikit-learn`, and `plotly`.
Python 3.11.4 gives Streamlit Cloud a stable environment with widely available wheels, which keeps
deployment fast and avoids long source builds.

If Streamlit Cloud deploys with Python 3.14, dependency installation may be very slow and the app
can fail its startup health check.

## If The App Was Already Deployed With Python 3.14

Streamlit Cloud does not let you change the Python version in-place after deployment.

1. Open **Manage app**.
2. Go to **Settings**.
3. Delete the app.
4. Create/deploy the app again from the same GitHub repository.
5. Open **Advanced settings**.
6. Select **Python 3.11**. If a patch version is available, use **3.11.4**.
7. Deploy.

## Local Run

```powershell
.\scripts\setup.ps1
.\.venv\Scripts\Activate.ps1
streamlit run app.py
```
