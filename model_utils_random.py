import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
import joblib


df = pd.read_csv('tumor_two_vars.csv')


X = df[['size', 'p53_concentration']]
y = df['is_cancerous']
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.3, random_state=42)
scaler = MinMaxScaler()
Xtrain_scaled = scaler.fit_transform(Xtrain)#on prend le min et max de train comme échelle et ça comme une règle
Xtest_scaled = scaler.transform(Xtest)#on a déjà le repère min et max pas besoin de re fit


model = RandomForestClassifier(random_state=42)
model.fit(Xtrain_scaled, ytrain)


joblib.dump(model, 'tumor_model.joblib')


def predict_cancer(tumor_features:dict)->str:
    input_data = scaler.transform([[tumor_features.size, tumor_features.p53_concentration]])
    prediction = model.predict(input_data)
    return "Cancéreux" if prediction[0] == 1 else "Non cancéreux"
