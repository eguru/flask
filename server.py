import os
import sys
from flask import Flask
from flask import render_template

app_path = os.path.dirname(os.path.abspath(__file__))
if app_path not in sys.path:
    sys.path.append(app_path)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
