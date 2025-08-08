import tensorflow as tf 
import joblib
import numpy
heart_model=tf.keras.models.load_model("heart_model.h5")
scalar_model=joblib.load("heart_scalar.pkl")

def predict_heart_disease(features: list):
    data=np.array([features])
    data_scaled=scalar_model.transform(data)
    pred=heart_model.predict(data_scaled)
    return float(pred[0][0])
