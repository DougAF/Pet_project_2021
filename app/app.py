from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_app():
	return  'Application is running, good work Doug!'


@app.route('/data')
def show_data():
	return "JSON"

if __name__ == '__main__':
	app.run(debug=True)
