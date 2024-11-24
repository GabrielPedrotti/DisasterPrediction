from flask import Blueprint, jsonify, request
from flask_cors import CORS
import joblib
import pandas as pd

model = Blueprint('model', 'model', url_prefix='/api/v1/model')
CORS(model)

trainedModel = joblib.load('./model/model.pkl')
encoder = joblib.load('./model/encoder.pkl')
scaler = joblib.load('./model/scaler.pkl')

'''
    ihProgramDeclared: assistência a afetados por desastres
    iaProgramDeclared: inclui o IHP e outros auxílios, como aconselhamento em crises, assistência ao desemprego
    paProgramDeclared: suporte financeiro a governos locais, tribos reconhecidas federalmente e algumas organizações sem fins lucrativos
    hmProgramDeclared: subsídios que ajuda comunidades a reduzir ou eliminar os riscos futuros causados por desastres
'''

@model.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print('Data received:', data)
        
        # preparar os dados recebidos para fazer a previsão
        X = pd.DataFrame([data])
        print('Input DataFrame:', X)
        
        categorical_cols = ['state', 'declarationType', 'designatedArea']
        numerical_cols = ['fipsStateCode', 'fipsCountyCode', 'combinedFIPS', 'year', 'Month',
                          'Precipitation', 'Cooling_Days', 'Heating_Days', 'AverageTemp',
                          'ihProgramDeclared', 'iaProgramDeclared', 'paProgramDeclared', 'hmProgramDeclared']
        
        X_encoded = encoder.transform(X[categorical_cols])
        X_encoded = pd.DataFrame(X_encoded, index=X.index)
        
        X_scaled = scaler.transform(X[numerical_cols])
        X_scaled = pd.DataFrame(X_scaled, index=X.index, columns=numerical_cols)
        
        X_processed = pd.concat([X_encoded, X_scaled], axis=1)
        X_processed.columns = X_processed.columns.astype(str)
        print('Processed DataFrame:', X_processed)
        
        prediction = trainedModel.predict(X_processed)
        print('Prediction:', prediction)
        
        return jsonify({'prediction': prediction[0]})
    
    except Exception as e:
        print('Error during prediction:', str(e))
        return jsonify({'error': str(e)}), 500
