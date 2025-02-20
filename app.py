# save this as app.py
from flask import Flask


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Hello, World!"

if __name__ == '__main__':
    # Debug/Development
     app.run(debug=True, host="0.0.0.0", port="5000")
