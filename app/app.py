from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def hello_app():
    return "Application is running, good work Doug!"


@app.route("/data")
def show_data():
    r = requests.get("http://google.com")
    return f"Status Code: {r.status_code}"


if __name__ == "__main__":
    app.run(debug=True)
