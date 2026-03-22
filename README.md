# 🏥 Insurance Charges Prediction App

A Machine Learning project that predicts medical insurance charges based on user inputs such as age, BMI, smoking status, and more.

---

## 🚀 Project Overview

This project focuses on building a regression model to estimate insurance costs using real-world data.
It includes data preprocessing, model training, evaluation, and deployment using a simple interactive web app.

The dataset contains features like:

* Age
* Sex
* BMI
* Number of children
* Smoking status
* Region

These factors are commonly used in insurance analysis to estimate costs ([Elisha Mlay][1]).

---

## 🧠 Machine Learning Workflow

### 1. Data Preprocessing

* Handling categorical variables باستخدام One-Hot Encoding
* Scaling numerical features (where needed)
* Building a preprocessing pipeline

---

### 2. Models Used

* K-Nearest Neighbors (KNN)
* Random Forest Regressor
* XGBoost Regressor 🔥

---

### 3. Model Evaluation

Models were evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

---

### 4. Hyperparameter Tuning

* GridSearchCV was used to find optimal parameters
* Improved model performance and generalization

---

## 🌐 Web App (Streamlit)

The project includes a simple web application where users can:

* Enter their data (age, BMI, etc.)
* Get predicted insurance charges instantly

---

## 🛠️ Tech Stack

* Python
* Pandas & NumPy
* Scikit-learn
* XGBoost
* Streamlit

---

## 📁 Project Structure

```bash
Insurance/
│
├── app/
│   └── app.py          # Streamlit app
│
├── model.pkl          # Trained model
├── notebook.ipynb     # EDA & training
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Mozoka995/Insurance.git
cd Insurance
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run the app

```bash
streamlit run app/app.py
```

---

## 📊 Key Insights

* Smoking status is the most influential factor affecting charges
* Age and BMI have moderate impact
* Other features have relatively lower influence

---

## 💡 Future Improvements

* Deploy the app online (Streamlit Cloud / Render)
* Add more advanced models
* Improve UI/UX
* Add model explainability (SHAP values)

---

## 👨‍💻 Author

**Mohamed Abd Elrazek**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!

[1]: https://elishamlay.github.io/Insurance_project.io/?utm_source=chatgpt.com "Insurance_project.io"
