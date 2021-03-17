#!C:\\Users\\clara\\AppData\\Local\\Programs\\Python\\Python39\\python.exe
print("content-type: text/html;")
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/info')
def info():
    return render_template('info.html')

if __name__ == '__main__':
    
	app.run(port="5501", debug=True)