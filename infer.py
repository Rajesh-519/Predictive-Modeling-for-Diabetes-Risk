import joblib
import pandas as pd

# Load model
model = joblib.load("saved_model/rf_model.joblib")

# Define feature names in correct order
feature_names = [
    "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
    "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
]

def predict_diabetes(data):
    # Convert input to DataFrame with feature names
    input_df = pd.DataFrame([data], columns=feature_names)
    prediction = model.predict(input_df)[0]
    return "Diabetic" if prediction == 1 else "Non-Diabetic"

# Example usage
if __name__ == "__main__":
    # Example: [Pregnancies, Glucose, BP, SkinThickness, Insulin, BMI, DPF, Age]
    sample = [2, 120, 70, 30, 0, 25.0, 0.5, 28]
    result = predict_diabetes(sample)
    print("Prediction:", result)
