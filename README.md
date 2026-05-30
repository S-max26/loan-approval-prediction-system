# Loan Approval Prediction System

A Machine Learning-powered web application that predicts the likelihood of loan approval based on applicant details and provides bank recommendations for eligible applicants.

Built using **Python**, **Flask**, and **Scikit-Learn**, this project demonstrates the complete machine learning workflow from data preprocessing and model training to deployment through a web interface.

---

## Project Overview

Financial institutions often evaluate multiple factors before approving a loan application. This project uses a trained Machine Learning model to analyze applicant information and predict whether a loan is likely to be approved.

The system also provides a bank recommendation based on the applicant's profile, making the application more practical and user-oriented.

---

## Features

- Loan Approval Prediction
- Real-Time Prediction Results
- Approval Probability Score
- Bank Recommendation System
- User-Friendly Web Interface
- Machine Learning Model Integration
- Fast and Lightweight Flask Backend

---

## Technology Stack

### Backend
- Python
- Flask

### Machine Learning
- Scikit-Learn
- Joblib
- NumPy
- Pandas

### Frontend
- HTML5
- CSS3

---

## Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Feature Encoding
4. Feature Scaling
5. Model Training
6. Model Evaluation
7. Model Serialization using Joblib
8. Flask Deployment

---

## Input Parameters

The model predicts loan approval using:

| Parameter | Description |
|------------|------------|
| Gender | Male / Female |
| Married | Marital Status |
| Dependents | Number of Dependents |
| Education | Graduate / Not Graduate |
| Self Employed | Employment Status |
| Applicant Income | Monthly Income |
| Coapplicant Income | Co-applicant Income |
| Loan Amount | Requested Loan Amount |
| Loan Amount Term | Loan Repayment Period |
| Credit History | Credit Score History |
| Property Area | Urban / Rural / Semi-Urban |

---

## Project Structure

```text
loan-approval-prediction-system/
│
├── dataset/
│   └── Loan-Approval-Prediction.csv
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py
├── loan_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/loan-approval-prediction-system.git
```

### Navigate to Project Directory

```bash
cd loan-approval-prediction-system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

### Open in Browser

```text
http://127.0.0.1:5000
```

---

## Screenshots

### Home Page

<img width="445" height="790" alt="image" src="https://github.com/user-attachments/assets/326f9bc2-628a-48e8-a236-bc9a594bdeca" />


### Prediction Result

<img width="594" height="820" alt="image" src="https://github.com/user-attachments/assets/5c041913-15fa-47d5-bad7-bf69e14da3a3" />


---

## Sample Workflow

1. Enter applicant details.
2. Submit the form.
3. Machine Learning model processes the data.
4. Prediction result is generated.
5. Approval probability is displayed.
6. Recommended bank is shown (if applicable).

---

## Future Enhancements

- Multiple Bank Recommendations
- Explainable AI (XAI)
- Loan EMI Calculator
- User Authentication
- Database Integration
- Cloud Deployment (AWS/Render)
- Improved UI/UX Design
- Prediction History Dashboard

---

## Learning Outcomes

Through this project, I gained hands-on experience in:

- Machine Learning Model Development
- Data Preprocessing
- Feature Engineering
- Classification Algorithms
- Flask Web Development
- Model Deployment
- Full Project Lifecycle Management

---

## Author

**Sanjana Barui**

Connect with me on LinkedIn and feel free to share feedback or suggestions.

---

## License

This project is developed for educational, learning, and portfolio purposes.

© 2026 Sanjana Barui
