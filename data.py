from app import app
from models import db, Property

with app.app_context():
    db.create_all()

    property1 = Property(title="villa", description="center vile", price=1000000, location="casablanca")
    property2 = Property(title="chember", description="rue lmarif", price=2000000, location="casablanca")


    db.session.add_all([property1, property2])
    db.session.commit()