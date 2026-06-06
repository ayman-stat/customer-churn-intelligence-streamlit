# Experiment Design: Retention Uplift

## Business Question

Which customers should receive a retention intervention, and does the model-driven targeting create measurable incremental uplift compared with business-as-usual targeting?

## Recommended Design

1. Score the eligible customer population.
2. Apply business rules such as contact policy, offer eligibility, and exclusion windows.
3. Select the targetable population based on risk, value, and intervention capacity.
4. Randomly split into target and control groups within comparable risk/value bands.
5. Activate retention actions only for the target group.
6. Measure retention, revenue, and engagement outcomes over a defined window.

## Targeting Logic

Prioritization should combine:

- Predicted churn probability
- Revenue exposure
- Tenure and engagement behavior
- Intervention cost
- Channel/contact eligibility
- Recent campaign exposure

## Success Metrics

- Incremental retained revenue
- Uplift versus control
- Retention rate improvement
- Cost per retained customer
- Net value after offer cost
- Contact fatigue and opt-out rate

## Why This Matters

A model can rank customers, but it cannot prove business impact alone. Senior data science work connects predictions to experiments, operating constraints, financial assumptions, and measurable outcomes.
