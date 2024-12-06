from flask import Flask, render_template,jsonify
#importing Flask Class from flask module

app = Flask(__name__)  #__name__ is a special variable in python that is automatically set to the name of the current module

JOBS = [
  {
    'id': 1,
    'Role': 'Data Scientist',
    'Location': 'Hyderabad',
    'Salary': 'Rs. 15,00,000'
  },
  {
    'id': 2,
    'Role': 'Data Analyst',
    'Location': 'Bengaluru',
    'Salary': 'Rs. 9,00,000'
  },
  {
    'id': 3,
    'Role': 'BackEnd Engineer',
    'Location': 'Pune',
    'Salary': 'Rs. 10,00,000'
  },
  {
    'id': 4,
    'Role': 'FrontEnd Engineer',
    'Location': 'New Delhi',
    'Salary': ' Rs. 9,50,000'
  },
  {
    'id': 5,
    'Role': 'Android Developer',
    'Location': 'Gurgaon'
  }
]

@app.route("/")  #decorator
def hello_world():
  return render_template('home.html',jobs = JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
