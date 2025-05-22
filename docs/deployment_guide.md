# Deployment Guide

## Overview

This guide details deploying the Loan Default Predictor v1.0 API for real-time predictions.

## Requirements

**Software:**

Python 3.8+
Libraries: Flask, pandas, scikit-learn (requirements.txt)


**Hardware:**

RAM: 8GB
CPU: 4 cores


**OS:**  

Linux (Ubuntu 20.04)

## Installation

**Clone repository:**
```bash
git clone <repository_url>
cd loan_default_project
```


## Install dependencies:

```bash
pip install -r requirements.txt
```


**Ensure files in models/:**

**1. tuned_decision_tree.pkl**

**2. scaler.pkl***



## Running the API

**1. Start server:**

```bash
python code/deploy.py
```

**2. Access at http://localhost:5000**

## Testing

```bash
Endpoint: /predict (POST)
Request:{
    "LOAN": 20000,
    "MORTDUE": 50000,
    "VALUE": 100000,
    "REASON": "DebtCon",
    "JOB": "Mgr",
    "YOJ": 5,
    "DEROG": 0,
    "DELINQ": 0,
    "CLAGE": 200,
    "NINQ": 1,
    "CLNO": 10,
    "DEBTINC": 35
}
```


**Command**
```bash
:curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"LOAN":20000,"MORTDUE":50000,"VALUE":100000,"REASON":"DebtCon","JOB":"Mgr","YOJ":5,"DEROG":0,"DELINQ":0,"CLAGE":200,"NINQ":1,"CLNO":10,"DEBTINC":35}'
```


**Response**:

```bash
{"default_probability": 0.15}
```


## Troubleshooting

**Contact: IT Team**S