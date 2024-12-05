from flask import Flask, request
from models.meals import Meals 

app = Flask(__name__)

Refeições = []

@app.route("/meals", methods=["POST"])
def register_meals():
    data = request.get_json()
    print(data)
    return 'Test'

@app.route('/')
def hello_word():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)