from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__, template_folder='template')
model = pickle.load(open('rfc.pkl', 'rb'))  # Ensure the correct model file name


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/bmi')
def bmi():
    return render_template('bmi.html')



@app.route('/predictAction', methods=['POST'])
def predictAction():
    if request.method == 'POST':
        # Extracting values from the form
        gender = request.form['gender']
        age = int(request.form['age'])
        hypertension = int(request.form['hypertension'])
        heart_disease = int(request.form['heart_disease'])
        ever_married = request.form['ever_married']
        avg_glucose_level = float(request.form['avg_glucose_level'])
        bmi = float(request.form['bmi'])
        work_type = request.form['work_type']
        residence_type = request.form['residence_type']
        smoking_status = request.form['smoking_status']

        # Encoding categorical variables
        gender_encoded = 1 if gender == 'Male' else 0
        ever_married_encoded = 1 if ever_married == 'Yes' else 0
        
        # One-hot encoding for categorical variables
        work_types = ['Private', 'Self-employed', 'Govt_job', 'children']
        residence_types = ['Urban', 'Rural']
        smoking_statuses = ['formerly smoked', 'never smoked', 'smokes', 'Unknown']
        
        work_type_encoded = [1 if work_type == wt else 0 for wt in work_types]
        residence_type_encoded = [1 if residence_type == rt else 0 for rt in residence_types]
        smoking_status_encoded = [1 if smoking_status == ss else 0 for ss in smoking_statuses]

        # Creating the feature array
        feature_values = np.array([[gender_encoded, age, hypertension, heart_disease, ever_married_encoded, avg_glucose_level, bmi] + work_type_encoded + residence_type_encoded + smoking_status_encoded])

        # Making prediction using the model
        prediction = model.predict(feature_values)

        # Rendering the result template with the prediction
        return render_template('result.html', prediction=prediction[0])
    
@app.route('/cta')
def cta():
    return render_template('cta.html')

@app.route('/counsel')
def counsel():
    return render_template('counsel.html') 
@app.route('/logi')
def logi():
    return render_template('logi.html') 

if __name__ == '__main__':
    app.run(debug=True)
