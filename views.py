from flask import Flask, render_template
from models import Property

app = Flask(__name__)

@app.route('/')
def home():
    properties = Property.query.all()
    return render_template('index.html', properties=properties
