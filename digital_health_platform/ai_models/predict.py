import pickle

def load_model(model_path='ai_models/model.pkl'):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

def predict(input_data, model):
    # Assuming input_data is in the right format for your model
    prediction = model.predict(input_data)
    return prediction
