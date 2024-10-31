from flask import Flask, render_template
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class FrontPage(Resource):
    def get(self):
        return render_template("index.html")

api.add_resource(FrontPage, "/index")

if __name__ == "__name__":
    app.run(debug=True)