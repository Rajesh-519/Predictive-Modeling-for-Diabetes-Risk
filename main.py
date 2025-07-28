from infer import predict_diabetes

def get_user_input():
    features = []
    labels = [
        "Pregnancies", "Glucose", "Blood Pressure", "Skin Thickness", 
        "Insulin", "BMI", "Diabetes Pedigree Function", "Age"
    ]
    for label in labels:
        val = float(input(f"Enter {label}: "))
        features.append(val)
    return features

if __name__ == "__main__":
    print("---- Diabetes Risk Predictor ----")
    user_data = get_user_input()
    result = predict_diabetes(user_data)
    print("Result:", result)
