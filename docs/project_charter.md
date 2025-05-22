#  Loan Default Prediction Project Charter

## Context

A major proportion of retail bank profit comes from interests in the form of home loans. These loans are borrowed by regular income/high-earning customers. Banks are most fearful of defaulters, as bad loans (NPA) usually eat up a major chunk of their profits. Therefore, it is important for banks to be judicious while approving loans for their customer base.

The approval process for the loans is multifaceted. Through this process, the bank tries to check the creditworthiness of the applicant on the basis of a manual study of various aspects of the application. The entire process is not only effort-intensive but also prone to wrong judgment/approval owing to human error and biases.

There have been attempts by many banks to automate this process by using heuristics. But with the advent of data science and machine learning, the focus has shifted to building machines that can learn this approval process and make it free of biases and more efficient. At the same time, one important thing to keep in mind is to make sure that the machine does not learn the biases that previously crept in because of the human approval process.

## Problem Statement

A bank's consumer credit department aims to simplify the decision-making process for home equity lines of credit to be accepted. To do this, they will adopt the Equal Credit Opportunity Act's guidelines to establish an empirically derived and statistically sound model for credit scoring. The model will be based on the data obtained via the existing loan underwriting process from recent applicants who have been given credit. The model will be built from predictive modeling techniques, but the model created must be interpretable enough to provide a justification for any adverse behavior (rejections).

##  Objective

Develop an **interpretable machine learning model** to predict **home equity loan defaults** with the following goals:

- Target **<8% default rate**
- Ensure **>70% approval rate**
- Maintain **ECOA compliance** for fair and non-discriminatory lending

---

##  Scope

- **Model Type**: Binary classification (default vs. non-default)
- **Dataset**: HMDA (Home Mortgage Disclosure Act)
  - Rows: **5,960**
  - Columns: **13**
- **Primary Stakeholders**:
  - Retail Banking
  - Risk Management
  - Compliance
  - Loan Officers

---

##  Regulatory Requirements

| Regulation | Description |
|------------|-------------|
| **SR 11-7** | Enforce comprehensive documentation and model validation |
| **ECOA**    | Ensure fairness, avoid discriminatory practices |
| **Basel III** | Align predictions with capital risk standards |

---

##  Stakeholder Needs

| Stakeholder      | Requirement |
|------------------|-------------|
| **Loan Officers** | Clear, interpretable outputs (e.g., default probability < 0.3 = approve) |
| **Risk Managers** | High **recall** to identify as many defaulters as possible |
| **Compliance**    | Integrated **fairness metrics** to detect and avoid bias |

---

##  Timeline

| Phase             | Duration |
|-------------------|----------|
| **Data Preparation**     | 1 week   |
| **Model Development**    | 2 weeks  |
| **Documentation & Review** | 1 week   |

---

##  Notes

This project aligns business goals with regulatory compliance, leveraging interpretable models for both operational decision-making and audit readiness.