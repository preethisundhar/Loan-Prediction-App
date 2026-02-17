# 🏦 Loan Approval Prediction System (Machine Learning + Streamlit)

An end-to-end **Machine Learning–based financial application** that predicts whether a loan will be **Approved or Rejected** based on applicant financial, credit, and asset details.

The system is designed to assist banks and financial institutions in **automating loan decision-making** with speed, consistency, and data-driven insights.

---
## 🔗 Live Application
http://3.27.238.185:8501

---
## 🚀 Deployment
- Platform: AWS EC2
- Web Framework: Streamlit
- Model Serialization: Joblib
---

## 🚀 Project Overview

Loan approval is a critical process that depends on multiple factors such as income, credit score, employment status, and asset ownership. Manual evaluation is time-consuming and prone to bias.

This project builds, evaluates, and deploys a **Machine Learning classification model** that predicts loan approval outcomes and exposes the model through a **professional Streamlit web application**.

The trained model is **serialized using Joblib** and used for real-time predictions via the web interface.

---

## 🎯 Key Objectives

- Perform data preprocessing and feature handling
- Train multiple Machine Learning classification models
- Evaluate models using appropriate performance metrics
- Select the best-performing model
- Save the trained ML model using **Joblib**
- Deploy the model using **Streamlit** for real-time loan prediction

---

## 🧪 Models Trained

The following Machine Learning models were trained and evaluated:

- Logistic Regression
- KNeighbors Classifier
- Decision Tree Classifier   
- Support Vector Machine (SVM)  
- Gradient Boosting
- xgBoost Classifier
- **RandomForest Classifier (Selected Model)**

### 🔍 Model Selection Criteria

| Model          | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---------------|----------|-----------|--------|----------|---------|
| Random Forest | 0.9824   | 0.9850    | 0.9868 | 0.9859   | **0.9987** |


📌 Random Forest was selected as the final model due to its excellent performance across all metrics, particularly the highest ROC-AUC score.

---

## 🧠 Model Evaluation Strategy

The model evaluates loan approval likelihood based on applicant risk profile:

- Higher income and asset value increase approval probability
- Strong credit (CIBIL) score improves approval chances
- Loan amount and loan term are balanced against financial strength

The trained model generalizes well to unseen data and is suitable for deployment in a decision-support system.

---

## 🗂 Input Features

The application uses the following input features:

- Number of Dependents  
- Education  
- Self Employed Status  
- Annual Income  
- Loan Amount  
- Loan Term  
- CIBIL Score  
- Residential Assets Value  
- Commercial Assets Value  
- Luxury Assets Value  
- Bank Asset Value  

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Libraries & Frameworks:**
  - Pandas
  - NumPy
  - Scikit-learn
  - Joblib
  - Streamlit
  - Pillow

- **ML Techniques:**
  - Feature Encoding
  - Model Pipelines
  - Classification Algorithms
  - Model Serialization

---

## 🖥️ Web Application Features

- Clean and professional UI
- Main-page loan application form (no sidebar)
- Real-time loan approval prediction
- Visual feedback for Approved / Rejected outcomes
- Image-based UI elements
- Deployment-ready architecture

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/loan-approval-prediction.git
cd loan-approval-prediction

```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit App

```bash
streamlit run app.py
```

The application will open in your default browser.

---

## ⚠️ Disclaimer

This project is created for educational purposes only and should not be used as a substitute for professional financial or credit risk assessment systems.

---
## 🚀 Feature Enhancements

* **Probability-Based Loan Approval**

Show approval confidence scores for better risk evaluation.

* **Feature Importance Visualization**

Highlight key factors influencing loan approval decisions.

* **Explainable AI (SHAP)**

Provide transparent explanations for individual predictions.

* **Cloud Deployment**

Deploy the application on AWS for scalability and reliability.

---

## 👩‍💻 Author

Preethi
Machine Learning | Data Analytics | Financial ML

---

## ⭐ Acknowledgement

If you find this project useful, consider giving it a ⭐ on GitHub!
