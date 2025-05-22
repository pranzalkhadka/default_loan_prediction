# Loan Default Predictor v1.0 Documentation

## Overview

The **Loan Default Predictor v1.0** automates home equity loan approvals by predicting loan defaults. The model prioritizes interpretability to ensure compliance with ECOA (Equal Credit Opportunity Act) and SR 11-7 supervisory guidance.

---

## Metadata

- **Name:** Loan Default Predictor v1.0  
- **ID:** LDP-2025-001  
- **Owner:** Data Science Team  
- **Purpose:** Minimize non-performing assets (NPAs) through accurate default prediction  
- **Business Unit:** Retail Banking  
- **Regulatory Framework:** SR 11-7, ECOA, Basel III  
- **Date:** May 2025  

---

## Methodology

### Model Type

- **Algorithm:** Tuned Decision Tree  
- **Parameters:**  
  - `max_depth=5`  
  - `criterion='gini'`  
  - `min_samples_leaf=5`  
  - `class_weight={0:0.2, 1:0.8}`  
- **Selection Criteria:** Prioritized recall (0.74) with interpretable decision rules  

### Data

- **Dataset:** HMDA (5,960 rows, 13 columns)  
- **Features:** See Data Dictionary  
- **Target Variable:** `BAD` (0 = non-default, 1 = default; approx. 20% default rate)  

### Preprocessing

See [Preprocessing Steps](#) for full details. Summary:  
- Missing values imputed (e.g., 21.3% missing in `DEBTINC`)  
- Outliers handled via IQR clipping  
- One-hot encoding for categorical features (`REASON`, `JOB`)  
- Numerical features scaled using StandardScaler  
- Class imbalance addressed via weighting  

### Training

- **Data Split:** 70% train (4,172 rows), 30% test (1,788 rows), stratified by target  
- **Tuning:** GridSearchCV over `max_depth` (2-6), `criterion` (gini/entropy), and `min_samples_leaf` (5-25)  
- **Evaluation Metrics:** Recall prioritized, alongside accuracy, precision, F1-score  

---

## Validation

See [Performance Report](#) for detailed metrics. Summary:

| Metric            | Training | Test  |
|-------------------|----------|-------|
| Accuracy          | 0.86     | 0.85  |
| Recall (Class 1)  | 0.80     | 0.74  |
| Precision (Class 1) | 0.62     | 0.61  |
| F1-Score (Class 1) | 0.70     | 0.67  |

---

## Interpretability

### Key Features (Importance)

| Feature                     | Importance |
|-----------------------------|------------|
| `DEBTINC_missing_values_flag`| 0.30       |
| `DEBTINC`                   | 0.25       |
| `CLAGE`                    | 0.20       |
| `DELINQ`                   | 0.15       |

### Decision Rules

- If `DEBTINC > 43.7` **and** `CLAGE < 285.5`: **High risk**  
- If `DEBTINC` is missing **and** `DELINQ > 0`: **High risk**  
- If `DEBTINC < 43.7` **and** `VALUE` present: **Low risk**

---

## Assumptions and Limitations

See [Assumptions and Limitations](#) for details.

### Risks

- **Data:** High missing data in `DEBTINC` (21.3%), imputed with median  
- **Methodology:** Recall of 0.74 means 26% of defaulters are missed  
- **Implementation:** API latency considerations (see Deployment Guide)  
- **Compliance:** ECOA fairness analysis pending  

---

## Recommendations

### Approval

- Scrutinize loans with `DEBTINC > 40` or missing values  
- Approve loans with predicted default probability < 0.3  

### Improvement

- Explore ensemble models to improve recall  
- Add additional features (e.g., credit trends)  

### Monitoring

- Monitor for data drift on `DEBTINC`, `CLAGE`  
- Perform quarterly model validation and recalibration  

---


*For questions or further details, please contact the Data Science Team.*