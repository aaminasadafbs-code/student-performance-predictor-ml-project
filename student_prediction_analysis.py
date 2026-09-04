import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
df = pd.read_csv("C:\\Users\\CIPL\\Documents\\Student-Performance-Prediction\\data\\student_data.csv")
print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.describe())
X = df[['study_hour',
        'attendance_percentage',
        'class_participation',
        'Assignment_Scores',
        'Test_Scores',
        'Previous_GPA']]

y = df['grade']
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
plt.figure(figsize=(18,10))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=model.classes_,
    filled=True,
    rounded=True,
    fontsize=8
)

plt.title("Student Performance Prediction using Decision Tree")
plt.savefig("decision_tree.png", dpi=300, bbox_inches="tight")
plt.show()
print("\nEnter New Student Details")

study_hour = float(input("Study Hours: "))
attendance = float(input("Attendance Percentage: "))
participation = float(input("Class Participation: "))
assignment = float(input("Assignment Score: "))
test = float(input("Test Score: "))
gpa = float(input("Previous GPA: "))

new_student = pd.DataFrame({
    "study_hour": [study_hour],
    "attendance_percentage": [attendance],
    "class_participation": [participation],
    "Assignment_Scores": [assignment],
    "Test_Scores": [test],
    "Previous_GPA": [gpa]
})

prediction = model.predict(new_student)

print("\nPredicted Grade:", prediction[0])