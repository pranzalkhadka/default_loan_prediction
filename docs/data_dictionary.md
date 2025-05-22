# Data Dictionary

| Feature   | Description                          | Type   | Range/Values                     |
|-----------|--------------------------------------|--------|----------------------------------|
| BAD       | Default status (0=non-default, 1=default) | Category | 0, 1                            |
| LOAN      | Loan amount                         | Float  | 0 - 89,300                      |
| MORTDUE   | Amount due on mortgage              | Float  | 0 - 399,307                     |
| VALUE     | Property value                      | Float  | 0 - 855,909                     |
| REASON    | Loan purpose                        | Category | DebtCon, HomeImp                |
| JOB       | Occupation                          | Category | Other, ProfExe, Office, Mgr, Self, Sales |
| YOJ       | Years at job                        | Float  | 0 - 41                          |
| DEROG     | Derogatory reports                  | Float  | 0 - 10                          |
| DELINQ    | Delinquent credit lines             | Float  | 0 - 15                          |
| CLAGE     | Age of oldest credit line (months)  | Float  | 0 - 1,168                       |
| NINQ      | Recent credit inquiries             | Float  | 0 - 17                          |
| CLNO      | Number of credit lines              | Float  | 0 - 71                          |
| DEBTINC   | Debt-to-income ratio                | Float  | 0 - 203.31                      |