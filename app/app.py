from flask import Flask, render_template
from flask_restful import Api, Resource

app = Flask(__name__)
#api = Api(app)

@app.route("/")
def index():
    return render_template("index.html")
    #return "<p> Hello, world!</p>"

@app.route("/about")
def about_page():
    return "<p>About the app page</p>"

@app.route("/get_data", methods=["POST", "GET"])
def send_data():
    pass

if __name__ == "__name__":
    app.run(debug=True)