# Student Performance Prediction using Machine Learning

A Machine Learning project that predicts student grades using multiple classification algorithms. This project demonstrates the complete machine learning workflow, including data preprocessing, model training, evaluation, and prediction using Python and Scikit-learn.

---

## 📌 Project Overview

This project predicts a student's academic grade based on various academic performance indicators. It is designed to understand and compare different Machine Learning algorithms using the same dataset.

---

## 🎯 Objective

To build and compare Machine Learning models for predicting a student's final grade based on:

- Study Hours
- Attendance Percentage
- Class Participation
- Assignment Scores
- Test Scores
- Previous GPA

---

## 🛠 Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib

---

## 📂 Dataset

The dataset contains **1,500 student records** with the following features:

- Student ID
- Study Hours
- Attendance Percentage
- Class Participation
- Assignment Scores
- Test Scores
- Total Score
- Previous GPA
- Grade (Target Variable)

---

## 🤖 Machine Learning Algorithms

This project currently includes:

- Decision Tree Classifier
- K-Nearest Neighbors (KNN)

Both algorithms are trained and evaluated using the same dataset for performance comparison.

---

## 📊 Model Performance

| Algorithm | Accuracy |
|-----------|----------|
| Decision Tree | 94.33% |
| K-Nearest Neighbors (KNN) | 94.33% |

---

## 💻 Features

- Load dataset using Pandas
- Perform data preprocessing
- Check for missing values
- Display dataset statistics
- Train Machine Learning models
- Evaluate model accuracy
- Predict grades for new student data
- Compare multiple Machine Learning algorithms

---

## ▶ Example Prediction

**Input**

```
Study Hours: 20
Attendance Percentage: 95
Class Participation: 9
Assignment Score: 88
Test Score: 90
Previous GPA: 3.8
```

**Output**

```
Predicted Grade: A
```

---

## 📁 Project Structure

```
Student-Performance-Prediction/
│
├── data/
│   └── student_data.csv
│
├── src/
│   ├── student_prediction_decision_tree.py
│   └── student_prediction_knn.py
│
├── decision_tree.png
├── README.md
└── requirements.txt
```

---

## 🚀 Future Improvements

- Implement Logistic Regression
- Implement Random Forest Classifier
- Implement Naive Bayes Classifier
- Compare multiple Machine Learning models
- Evaluate Precision, Recall, and F1-Score
- Perform Hyperparameter Tuning

---

## 👩‍💻 Author

**Aamina Sadaf**

Bachelor of Science in Mathematics with Computer Applications

This project is part of my Machine Learning learning journey and GitHub portfolio, focusing on building practical skills in data analysis and predictive modeling.
