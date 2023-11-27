from flask import Flask
app = Flask(__name__)
@app.route("/")
def first_to_flask():
    return "this is my first flask"
@app.route("/oba")
def second_flask():
    return "Hello my name is Oba Fadiora"
app.run(debug=True)