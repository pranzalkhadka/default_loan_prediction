from flask import Flask, request, jsonify
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('models/tuned_decision_tree.pkl', 'rb'))
scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    df = pd.get_dummies(df, columns=['REASON', 'JOB'], drop_first=True)
    for col in model.feature_names_in_:
        if col not in df.columns:
            df[col] = 0
    df = df[model.feature_names_in_]
    df_scaled = scaler.transform(df)
    prediction = model.predict_proba(df_scaled)[:, 1]
    return jsonify({'default_probability': float(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)