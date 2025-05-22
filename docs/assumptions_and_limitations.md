## Assumptions and Limitations

### Assumptions

- **Data Stability:**  
  Applicant credit behavior remains consistent with historical data.

- **Data Quality:**  
  The dataset is assumed to be representative of the broader loan applicant population.

- **Imputation Validity:**  
  Median/mode imputation for missing values (e.g., `DEBTINC`, with 21.3% missing) is considered appropriate.

- **Feature Relevance:**  
  The selected features (e.g., `DEBTINC`, `CLAGE`) are sufficient to capture meaningful default risk signals.

---

### Limitations

- **Recall Performance:**  
  Test recall = 0.74, meaning 26% of defaulters may go undetected—posing potential NPA (Non-Performing Asset) risks.

- **Missing Data:**  
  High missing value rates in key features (e.g., 21.3% in `DEBTINC`) may reduce the model's robustness.

- **Feature Set Constraints:**  
  The model uses only 13 features, which may oversimplify complex borrower behavior.

- **Fairness Concerns:**  
  No bias or fairness analysis has been conducted. This may risk non-compliance with ECOA (Equal Credit Opportunity Act).

- **Generalization:**  
  The model is trained on  historical loan default data and may not generalize well to data from other sources or regions.

---

### Mitigation Strategies

- **Monitor Model Performance:**  
  Continuously evaluate predictions in production to identify and address missed defaulters.

- **Validate Imputation:**  
  Test and refine imputation strategies with incoming real-world data.

- **Feature Expansion:**  
  Explore additional features (e.g., historical credit trends, repayment patterns) to improve accuracy and fairness.