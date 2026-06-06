from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)

@app.route('/')
def index():
    with app.app_context():
        db.create_all()
        db.session.add(Visit())
        db.session.commit()
        count = Visit.query.count()
    return f'<h1>Брой посещения: {count}</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)