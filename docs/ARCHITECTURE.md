# Architecture Brief

## Objective

Build a public, recruiter-friendly customer intelligence product that demonstrates how churn modeling can move from a notebook concept into a business-facing decision workflow.

## System Flow

```text
Synthetic Data Generator
        |
        v
Feature Engineering
        |
        v
Candidate Model Training
        |
        v
Model Selection + Feature Importance
        |
        v
Customer Risk Scoring
        |
        v
Executive Decision Layer
        |
        v
Retention Actions + Target/Control Design
```

## Technical Components

- **Streamlit:** interactive product interface and multi-page workflow.
- **pandas / numpy:** synthetic data generation, data manipulation, aggregation, and scoring tables.
- **scikit-learn:** preprocessing pipelines, candidate models, train/test split, evaluation metrics, and scoring.
- **Plotly:** executive charts and segment-level risk visualization.
- **pytest:** smoke tests for data generation and model training.
- **GitHub / Streamlit Cloud:** public repository and live deployment.

## Senior-Level Design Choices

- Separate `src/` modules for data, features, modeling, explainability, and utilities.
- Use synthetic data to protect confidentiality while still showing realistic business logic.
- Compare model candidates instead of hard-coding a single classifier.
- Show executive decision metrics, not just technical model metrics.
- Include model card, governance notes, deployment documentation, and experiment design.

## Production Extensions

For a real production rollout, the system would need:

- Source data contracts and data-quality checks.
- Batch or real-time scoring pipeline.
- Feature store or governed feature layer.
- Model registry and approval workflow.
- Scheduled monitoring for drift, performance, and campaign outcomes.
- Dashboard integration for stakeholders.
