import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/meetVi')
def meetVi():
    return render_template('meetVi.html', title="Vi Pham", url=os.getenv("URL"))

@app.route('/meetAshley')
def meetAshley():
    return render_template('meetAshley.html', title="Ashley Ye", url=os.getenv("URL"))

if __name__ ==  "__main__":
    app.run(debug=True)