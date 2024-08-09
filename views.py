from flask import Flask, render_template, request
from models import Property

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        search_query = request.form['search']
        properties = Property.query.filter(Property.title.like(f'%{search_query}%')).all()
    else:
        properties = Property.query.all()
    return render_template('index.html', properties=properties)
