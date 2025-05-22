## Performance Report

### Overview

This report evaluates the Loan Default Predictor v1.0 (Tuned Decision Tree), compares it with alternative models, and highlights its interpretability.

---

### Performance Metrics

| Metric                  | Training | Test  |
|-------------------------|----------|-------|
| Accuracy                | 0.86     | 0.85  |
| Recall (Class 1)        | 0.80     | 0.74  |
| Precision (Class 1)     | 0.62     | 0.61  |
| F1-Score (Class 1)      | 0.70     | 0.67  |

---

### Model Comparison (Test Set)

| Model               | Accuracy | Recall (Class 1) | Precision (Class 1) |
|---------------------|----------|------------------|---------------------|
| Tuned Decision Tree | 0.85     | 0.74             | 0.61                |
| Random Forest       | 0.89     | 0.64             | 0.76                |
| Logistic Regression | 0.76     | 0.41             | 0.39                |

---

### Insights

- The **Tuned Decision Tree** excels in recall (0.74), which is crucial for identifying defaulters.
- **Random Forest** achieves higher precision (0.76) but is less interpretable.
- **Logistic Regression** underperforms with low recall (0.41).

---

### Interpretability

#### Key Feature Importances

| Feature                     | Importance |
|-----------------------------|------------|
| DEBTINC_missing_values_flag  | 0.30       |
| DEBTINC                     | 0.25       |
| CLAGE                       | 0.20       |
| DELINQ                      | 0.15       |

#### Decision Rules Extracted

- If `DEBTINC > 43.7` and `CLAGE < 285.5`: **High risk**
- If `DEBTINC` is missing and `DELINQ > 0`: **High risk**
- If `DEBTINC < 43.7` and `VALUE` present: **Low risk**

#### Insights

- High `DEBTINC` increases default odds by approximately 50%.
- Older `CLAGE` (credit age) indicates borrower stability.

---

### Visualizations

#### Confusion Matrix (Test Set)

|               | Predicted Negative | Predicted Positive |
|---------------|--------------------|--------------------|
| Actual Negative | 1259 (88% correct) | 172 (12% incorrect) |
| Actual Positive | 93 (26% missed)    | 264 (74% correct)  |

#### Feature Importance

- `DEBTINC` and `CLAGE` dominate feature importance, consistent with debt levels and credit history being key predictors.

---

### Recommendations

- Focus on monitoring `DEBTINC` and `DELINQ` during loan reviews.
- Approve loans with predicted default probability < 0.3.
- Implement ongoing monitoring to reduce the risk from 26% of missed defaulters.