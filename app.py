from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        search_query = request.form.get('search', '')
        min_price = request.form.get('min_price', None)
        max_price = request.form.get('max_price', None)

        query = Property.query
        if search_query:
            query = query.filter(Property.title.like(f'%{search_query}%'))
        if min_price:
            query = query.filter(Property.price >= min_price)
        if max_price:
            query = query.filter(Property.price <= max_price)

        properties = query.all()
    else:
        properties = Property.query.all()
    return render_template('index.html', properties=properties)

if __name__ == '__main__':
    app.run(debug=True)
