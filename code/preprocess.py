import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

def treat_outliers(df, col):
    """Treat outliers in a numerical variable using IQR method."""
    Q1 = df[col].quantile(q=0.25)
    Q3 = df[col].quantile(q=0.75)
    IQR = Q3 - Q1
    Lower_Whisker = Q1 - 1.5 * IQR
    Upper_Whisker = Q3 + 1.5 * IQR
    df[col] = np.clip(df[col], Lower_Whisker, Upper_Whisker)
    return df

def treat_outliers_all(df, col_list):
    """Apply outlier treatment to all numerical columns."""
    for c in col_list:
        df = treat_outliers(df, c)
    return df

def add_binary_flag(df, col):
    """Add binary flag for missing values in a column."""
    new_col = f"{col}_missing_values_flag"
    df[new_col] = df[col].isna()
    return df

def preprocess_data(input_path, output_path):
    """Preprocess HMDA dataset for loan default prediction."""
    # Load data
    df = pd.read_csv(input_path)
    
    # Convert categorical columns to category type
    cat_cols = ['REASON', 'JOB', 'BAD']
    for col in cat_cols:
        df[col] = df[col].astype('category')
    
    # Treat outliers in numerical columns
    numerical_cols = ['LOAN', 'MORTDUE', 'VALUE', 'YOJ', 'DEROG', 'DELINQ', 
                     'CLAGE', 'NINQ', 'CLNO', 'DEBTINC']
    df = treat_outliers_all(df, numerical_cols)
    
    # Add binary flags for missing values
    missing_cols = [col for col in df.columns if df[col].isnull().any()]
    for col in missing_cols:
        df = add_binary_flag(df, col)
    
    # Impute missing values
    num_data = df.select_dtypes(include='number')
    for column in num_data.columns:
        median_val = df[column].median()
        df[column].fillna(median_val, inplace=True)
    
    cat_data = df.select_dtypes(include='category').columns.tolist()
    for column in cat_data:
        mode_val = df[column].mode()[0]
        df[column].fillna(mode_val, inplace=True)
    
    # Separate features and target
    Y = df['BAD']
    X = df.drop(columns=['BAD'])
    
    # Create dummy variables
    to_get_dummies_for = ['REASON', 'JOB']
    X = pd.get_dummies(data=X, columns=to_get_dummies_for, drop_first=True)
    
    # Drop boolean missing value flags
    bool_cols = X.select_dtypes(['bool']).columns.tolist()
    X = X.drop(columns=bool_cols)
    
    # Scale numerical features
    sc = StandardScaler()
    X_scaled = sc.fit_transform(X)
    X_scaled = pd.DataFrame(X_scaled, columns=X.columns)
    
    # Save preprocessed data
    X_scaled.to_csv(output_path, index=False)
    
    # Save scaler
    with open('models/scaler.pkl', 'wb') as f:
        pickle.dump(sc, f)
    
    return X_scaled, Y, sc

if __name__ == "__main__":
    input_path = "data/raw/hmda_data.csv"
    output_path = "data/preprocessed/hmda_preprocessed.csv"
    X_scaled, Y, scaler = preprocess_data(input_path, output_path)
    print(f"Preprocessed data saved to {output_path}")