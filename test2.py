#!C:\\Users\\clara\\AppData\\Local\\Programs\\Python\\Python39\\python.exe
print("content-type: text/html;")
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():

	return 'Hello world bitches! hello hi what'

	

# if __name__ == '__main__':

# 	app.run(port="5501", debug=True)