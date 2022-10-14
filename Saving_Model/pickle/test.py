import pickle
#load the model

model = pickle.load(open('diabetes_80.pkl','rb'))

result = model.predict([[1,1,1,1,1,1,1,1]])

if result[0] == 1:
    print("The person is diabetic.")
else:
    print("The person is not diabetic.")