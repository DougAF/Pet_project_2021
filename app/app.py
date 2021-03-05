from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_app():
	return  'Application is running, good work Doug!'
