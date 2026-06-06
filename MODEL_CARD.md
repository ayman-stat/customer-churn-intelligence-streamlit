# Model Card: Customer Churn Intelligence Demo

## Purpose

This model card documents a public portfolio demo for churn prediction and retention prioritization.
The project is designed to show Senior Data Scientist / AI Lead thinking across business framing,
modeling, decision support, governance, and deployment readiness.

## Intended Use

- Identify synthetic customers with higher churn risk.
- Demonstrate how risk scores can support retention prioritization.
- Convert model output into executive metrics such as exposed revenue, target capacity, intervention cost, and estimated retained revenue.
- Show how a model would be governed before any real production rollout.

## Not Intended For

- Real customer decisioning without approved production data and retraining.
- Automated pricing, offer, credit, health, eligibility, or sensitive customer decisions.
- Claims of employer, client, or commercial performance.
- Use with confidential customer, member, patient, banking, or third-party data.

## Data

The app generates synthetic customer-level data inside the application. No employer, client, customer,
member, or third-party data is included in the repository or hosted demo.

Feature themes:

- Tenure
- Monthly revenue
- Recent visits
- Days since last visit
- Support tickets
- Discount usage
- Late payment count
- Segment and acquisition channel

## Modeling Approach

The model lab compares three candidate classifiers:

- Logistic Regression
- Random Forest
- Gradient Boosting

The app selects the highest-ranked model from the leaderboard and uses it to score synthetic customer profiles.

## Evaluation Metrics

Technical metrics:

- ROC AUC
- Average precision
- Recall at threshold
- Feature importance

Business metrics to add in a production rollout:

- Retained revenue
- Incremental uplift versus control
- Campaign conversion rate
- Cost per retained customer
- False-positive intervention cost
- Contact fatigue

## Governance Controls

Before production rollout, this model would need:

- Approved feature definitions and data lineage.
- Human review for high-value or sensitive actions.
- Target/control experiment design before claiming uplift.
- Threshold governance by intervention capacity and marginal business value.
- Drift monitoring across input features, scores, and campaign outcomes.
- Model card approval and retraining cadence.

## Limitations

- Synthetic data does not represent a validated production population.
- Model performance is illustrative and should not be compared with real-world benchmarks.
- The app demonstrates workflow, leadership thinking, and product framing rather than a production deployment.
