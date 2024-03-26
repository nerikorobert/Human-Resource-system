from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://neriko:Jakaranda@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

# Assuming 'employees' is a list of dictionaries, each representing an employee
employees = [
    {'id': 1, 'name': 'Parwiz', 'email': 'par@gmail.com', 'phone': '0742024479'},
    {'id': 2, 'name': 'John Doe', 'email': 'john.doe@example.com', 'phone': '123456789'},
    {'id': 3, 'name': 'Jane Smith', 'email': 'jane.smith@example.com', 'phone': '987654321'},
    # Add more employees here...
]

@app.route('/')
def index():
    # Fetch all employees from the database
    employees = Data.query.all()
    return render_template('index.html', employees=employees)

# Inserting data
@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        my_data = Data(name, email, phone)
        db.session.add(my_data)
        db.session.commit()

        flash("Employee Inserted Successfully")

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
