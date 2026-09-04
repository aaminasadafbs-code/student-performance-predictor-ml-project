# student-performance-predictor-ml-project
Machine Learning project to predict student grades using Decision Tree Classifier with Python, Pandas, and Sci-kit-learn. Future updates will include KNN and model comparison.
# Student Performance Prediction using Decision Tree

## 📌 Project Overview

This project predicts a student's academic grade using the Decision Tree Classification algorithm in Python. It is a simple Machine Learning project built to understand the complete ML workflow, from loading data to making predictions for a new student.

---

## 🎯 Objective

To predict a student's final grade based on academic performance indicators such as:

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

## 🤖 Machine Learning Algorithm

This project uses the **Decision Tree Classifier** from Scikit-learn.

The dataset is divided into:

- 80% Training Data
- 20% Testing Data

using the Hold-Out Method (`train_test_split`).

---

## 📊 Model Performance

**Accuracy:** **96.33%**

The trained model successfully predicts student grades based on the provided academic details.

---

## 🌳 Decision Tree Visualization

The project generates a graphical representation of the Decision Tree and saves it as:

```
decision_tree.png
```

---

## 💻 Features

- Loads CSV dataset using Pandas
- Performs basic data exploration
- Checks for missing values
- Displays statistical summary
- Trains a Decision Tree model
- Evaluates model accuracy
- Visualizes the Decision Tree
- Predicts the grade for a new student using user input

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
│   └── student_prediction_analysis.py
│
├── decision_tree.png
├── README.md
└── requirements.txt
```

---

## 🚀 Future Improvements

- Implement K-Nearest Neighbors (KNN)
- Compare multiple Machine Learning algorithms
- Evaluate Precision, Recall and F1-Score
- Improve model performance through feature engineering

---

## 👩‍💻 Author

**Aamina Sadaf**

Mathematics With Computer Applications Student

Project developed for learning Machine Learning fundamentals and building a practical GitHub portfolio project.
