# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def index():

    return render_template("index.html")

@app.route("/CoreListReports")
def CoreListReports():

    return render_template('corelistreports.html')

@app.route('/supportfilesecon')
def econsupportfiles():

    return render_template('supportfilesecon.html')


if __name__ == "__main__":
    app.run(debug=True)