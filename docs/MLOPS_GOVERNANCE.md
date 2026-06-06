# MLOps & Governance Roadmap

## Current Portfolio Demo

The current app is intentionally lightweight and public:

- Synthetic data
- Modular Python source code
- Candidate model comparison
- Feature importance
- Interactive scoring
- Executive decision scenarios
- Smoke tests
- Streamlit Cloud deployment

## Production Roadmap

### Data Governance

- Data contracts for customer, transaction, interaction, and campaign tables.
- Feature definitions approved by data owners.
- Data-quality checks before training and scoring.
- Privacy and compliance review before activation.

### Model Lifecycle

- Experiment tracking with MLflow or an equivalent registry.
- Model versioning and approval workflow.
- Reproducible training configuration.
- Model card attached to each production version.
- Rollback plan for underperforming models.

### Monitoring

- Input feature drift.
- Score distribution drift.
- Segment-level performance stability.
- Campaign uplift versus control.
- Data freshness and scoring coverage.
- Business KPI movement after intervention.

### Responsible AI Controls

- Human review for sensitive or high-value interventions.
- Segment-level fairness checks.
- Contact policy and offer eligibility rules.
- Explainability review before stakeholder adoption.
- Clear distinction between decision support and automated decisioning.

## AI Lead Signals

This roadmap demonstrates ownership beyond model training:

- Translate business objectives into measurable AI use cases.
- Design operating controls around model output.
- Connect technical metrics to commercial outcomes.
- Plan deployment, monitoring, governance, and stakeholder adoption.
