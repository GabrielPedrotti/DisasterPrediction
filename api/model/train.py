from pymongo import MongoClient
from bson import ObjectId
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import pandas as pd
import joblib

mongo_uri = "mongodb+srv://admin:ZWHQZ7ogjcocHwwt@data.szklj.mongodb.net/?retryWrites=true&w=majority&appName=data"
client = MongoClient(mongo_uri)
db = client["data"]

def get_all_disasters():
    disasters = db.disaster.find()
    return [disaster for disaster in disasters]

data = pd.DataFrame(get_all_disasters())
print(data.head())

print('COLUMNS ----------------->', data.columns)

print('isnull ------> ', data.isnull().sum())

X = data.drop(columns=['incidentType', '_id'])
y = data['incidentType']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

categorical_cols = ['state', 'declarationType', 'designatedArea']

enc = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
X_train_encoded = enc.fit_transform(X_train[categorical_cols])
X_test_encoded = enc.transform(X_test[categorical_cols])

numerical_cols = ['fipsStateCode', 'fipsCountyCode', 'combinedFIPS', 'year', 'Month',
                  'Precipitation', 'Cooling_Days', 'Heating_Days', 'AverageTemp',
                  'ihProgramDeclared', 'iaProgramDeclared', 'paProgramDeclared', 'hmProgramDeclared']
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train[numerical_cols])
X_test_scaled = scaler.transform(X_test[numerical_cols])


X_train_encoded = pd.DataFrame(X_train_encoded, index=X_train.index)
X_test_encoded = pd.DataFrame(X_test_encoded, index=X_test.index)
X_train_scaled = pd.DataFrame(X_train_scaled, index=X_train.index, columns=numerical_cols)
X_test_scaled = pd.DataFrame(X_test_scaled, index=X_test.index, columns=numerical_cols)

X_train_processed = pd.concat([X_train_encoded, X_train_scaled], axis=1)
X_test_processed = pd.concat([X_test_encoded, X_test_scaled], axis=1)

X_train_processed.columns = X_train_processed.columns.astype(str)
X_test_processed.columns = X_test_processed.columns.astype(str)

# comente caso queira usar o modelo salvo
model = RandomForestClassifier(random_state=42)
model.fit(X_train_processed, y_train)

# carrega o modelo treinado
# model = joblib.load('./model/model.pkl')

y_pred = model.predict(X_test_processed)

print(model.feature_importances_)
print(X_train_processed.columns)

comparison_df = pd.DataFrame({
    'Real': y_test,
    'Predicted': y_pred
})

print("Comparison of Real vs Predicted:")
print(comparison_df.head())

correct_predictions = (comparison_df['Real'] == comparison_df['Predicted']).sum()
total_predictions = len(comparison_df)
accuracy = correct_predictions / total_predictions
print(f"Manual accuracy: {accuracy:.2f}")

train_score = model.score(X_train_processed, y_train)
test_score = model.score(X_test_processed, y_test)

print(f"Train score: {train_score}")
print(f"Test score: {test_score}")

# salvar o modelo treinado
joblib.dump(model, './model/model.pkl')
joblib.dump(enc, './model/encoder.pkl')
joblib.dump(scaler, './model/scaler.pkl')
print('Model saved as model.pkl')
