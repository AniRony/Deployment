import joblib
#load the model

model = joblib.load('diabetes_80.pkl')

result = model.predict([[1,1,1,1,1,1,1,1]])

if result[0] == 1:
    print("The person is diabetic.")
else:
    print("The person is not diabetic.")