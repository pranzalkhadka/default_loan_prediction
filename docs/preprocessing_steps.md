# Preprocessing Steps

## Overview  
This document describes the preprocessing pipeline for the HMDA dataset, preparing it for loan default prediction.

---

## Steps

### 1. Load Data

- **Dataset:** HMDA (5,960 rows, 13 columns)  
- **Source:** `data/raw/hmda_data.csv`

---

### 2. Convert Types

- **Categorical:**  
  - `REASON`, `JOB`, `BAD` → converted to `category`
  
- **Numerical:**  
  - `LOAN`, `MORTDUE`, `VALUE`, `YOJ`, `DEROG`, `DELINQ`, `CLAGE`, `NINQ`, `CLNO`, `DEBTINC` → converted to `float`

---

### 3. Handle Outliers

- **Method:** IQR clipping  
- **Columns:** All numerical columns  
- **Example:**  
  - `DEBTINC` clipped at `Q1 - 1.5 * IQR` and `Q3 + 1.5 * IQR`

---

### 4. Handle Missing Values

- **Numerical:**
  - Imputed using median  
  - Example: `DEBTINC` has 21.3% missing values

- **Categorical:**
  - Imputed using mode  
  - Example: `REASON` has 4.2% missing values

- **Flags:**
  - Added `*_missing_values_flag` columns for each feature with missing values

---

### 5. Encode Categorical

- **Columns:** `REASON`, `JOB`  
- **Method:** One-hot encoding (`drop_first=True`)  
- **Output:**  
  - Dummy variables (e.g., `REASON_HomeImp`, `JOB_ProfExe`)

---

### 6. Scale Features

- **Method:** `StandardScaler`  
- **Columns:** All numerical features  
- **Output:** Standardized features with `mean=0` and `std=1`

---