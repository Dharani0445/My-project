import pickle
import numpy as np
from app.models import PatientData

model = pickle.load(open("ai_models/model.pkl", "rb"))

def predict_disease_risk(data: PatientData) -> float:
    features = np.array([[data.age, data.bmi, data.blood_pressure, data.cholesterol]])
    return float(model.predict_proba(features)[0][1])  # Return probability of disease
