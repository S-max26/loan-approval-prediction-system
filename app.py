from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained model and scaler
model = joblib.load('loan_model.pkl')
scaler = joblib.load('scaler.pkl')


@app.route('/')
def home():
    return render_template('index.html', prediction_text='')


@app.route('/predict', methods=['POST'])
def predict():

    # Convert categorical values into numbers
    gender = 1 if request.form['Gender'] == 'Male' else 0

    married = 1 if request.form['Married'] == 'Yes' else 0

    dependents = int(request.form['Dependents'])

    education = 1 if request.form['Education'] == 'Graduate' else 0

    self_employed = 1 if request.form['Self_Employed'] == 'Yes' else 0

    applicant_income = float(request.form['ApplicantIncome'])

    coapplicant_income = float(request.form['CoapplicantIncome'])

    loan_amount= float(request.form['LoanAmount'])

    loan_amount_term = float(request.form['Loan_Amount_Term'])

    credit_history = float(request.form['Credit_History'])

    property_area_map = {
        'Rural': 0,
        'Semiurban': 1,
        'Urban': 2
    }
   
    property_area = property_area_map[request.form['Property_Area']]

    # Create input data
    data = [[
        gender,
        married,
        dependents,
        education,
        self_employed,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_amount_term,
        credit_history,
        property_area
    ]]

    # Scale input data
    data_scaled = scaler.transform(data)

    # Predict loan status
    prediction = model.predict(data_scaled)

    # Predict probability
    probability = model.predict_proba(data_scaled)[0][1]

    # Final result
    bank_name = ""

    if prediction[0] == 1:
        result = "Loan Approved"

    # Bank suggestion logic
        if credit_history >= 5 and applicant_income > 5000:
            bank_name = "HDFC Bank"
        elif property_area == 2:   # Urban
            bank_name = "ICICI Bank"
        elif property_area == 1:   # Semiurban
            bank_name = "Axis Bank"
        else:
            bank_name = "State Bank of India"

    else:
        result = "Loan Rejected"
        bank_name = "No bank recommendation"
 
    return render_template(
        'result.html',
        prediction_text=result,
        probability=round(probability * 100, 2),
        bank_name=bank_name,
        user_data=request.form
    )


if __name__ == '__main__':
    app.run(debug=True)