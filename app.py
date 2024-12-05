from flask import Flask, render_template  #importing Flask Class from flask module

app = Flask(
    __name__
)  #__name__ is a special variable in python that is automatically set to the name of the current module


@app.route("/")  #decorator
def hello_world():
  return render_template('home.html')


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
