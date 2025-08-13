Employee Salary Prediction App

This project is a Flask-based web application that predicts an employee's salary using a K-Nearest Neighbors (KNN) regression model. The model is trained on employee data from Employe_Performance_dataset.csv.

Features

Salary Prediction: Predicts an employee's salary based on their ID, name, department, and performance score.

KNN Model: Uses a K-Nearest Neighbors Regressor for the prediction.

Data Preprocessing: Handles categorical data (name, department) using LabelEncoder and scales numerical features using StandardScaler.

Web Interface: A simple web form to input employee data and display the predicted salary.

Project Structure
app.py: The main Flask application file. It initializes the model and encoders, handles the web routes, and processes user input to provide a salary prediction.

knn_model.py: A utility script that contains the logic for training the KNN model and a function to make predictions.

Employe_Performance_dataset.csv: The dataset used to train the model, containing employee information like ID, name, department, performance score, and salary.

README.md: This file, providing an overview of the project.

templates/: (Implied) This directory would contain the HTML files for the web interface.

index.html: The main form for user input.

result.html: Displays the predicted salary

Technologies Used

Flask: Web framework.

Scikit-learn: Machine learning library for the KNN model and preprocessing.

Pandas: For data manipulation. 

<img width="737" height="449" alt="Screenshot (71)" src="https://github.com/user-attachments/assets/90efaf22-71f4-4273-84c6-6054a891b861" />
<img width="747" height="447" alt="Screenshot (72)" src="https://github.com/user-attachments/assets/27f0e4cf-d057-47e4-80f5-0594d3b5175f" />


