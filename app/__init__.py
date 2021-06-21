import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Vi Pham's Portfolio", url=os.getenv("URL"))


if __name__ ==  "__main__":
    app.run(debug=True)
