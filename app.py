from flask import Flask, render_template, request
from knn_model import train_knn, predict_salary

app = Flask(__name__)


model, scaler, name_encoder, dept_encoder, df = train_knn()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        emp_id = int(request.form["id"])
        name = request.form["name"]
        department = request.form["department"]
        performance = float(request.form["performance"])

        
        input_data = [emp_id, name, department, performance]

        
        salary = predict_salary(model, scaler, name_encoder, dept_encoder, input_data)

        return render_template("result.html", salary=salary)

    
    names = sorted(df['Name'].unique())
    departments = sorted(df['Department'].unique())

    
    decoded_names = list(name_encoder.inverse_transform(names))
    decoded_departments = list(dept_encoder.inverse_transform(departments))

    return render_template("index.html", names=decoded_names, departments=decoded_departments)

if __name__ == "__main__":
    app.run(debug=True)
