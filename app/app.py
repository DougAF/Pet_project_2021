from flask import Flask, url_for, render_template
import requests

app = Flask(__name__, template_folder= 'react-flask-app/public/')


@app.route("/")
def hello_app():
    return "Application is running, good work Doug!"


@app.route("/data")
def show_data():
    r = requests.get("http://google.com")
    return f"Status Code: {r.status_code}"


@app.route("/react_index")
def render_react_template():
    return render_template("index.html"
)


with app.test_request_context():
    print(f"Available Routes: ", url_for("show_data"), url_for("render_react_template"))

if __name__ == "__main__":
    app.run(debug=True)
