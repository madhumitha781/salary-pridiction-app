import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import LabelEncoder, StandardScaler


def train_knn():
    df = pd.read_csv("Employe_Performance_dataset.csv")

    
    df = df[['ID', 'Name', 'Department', 'Performance Score', 'Salary']].dropna()

   
    name_encoder = LabelEncoder()
    dept_encoder = LabelEncoder()

    df['Name'] = name_encoder.fit_transform(df['Name'])
    df['Department'] = dept_encoder.fit_transform(df['Department'])


    X = df[['ID', 'Name', 'Department', 'Performance Score']]
    y = df['Salary']

  
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

   
    model = KNeighborsRegressor(n_neighbors=3)
    model.fit(X_scaled, y)

    return model, scaler, name_encoder, dept_encoder, df

def predict_salary(model, scaler, name_encoder, dept_encoder, input_data):
    input_data[1] = name_encoder.transform([input_data[1]])[0]  # Encode Name
    input_data[2] = dept_encoder.transform([input_data[2]])[0]  # Encode Dept
    scaled_input = scaler.transform([input_data])
    return model.predict(scaled_input)[0]
