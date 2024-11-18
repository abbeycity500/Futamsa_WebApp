from app import db

class Gallery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    date_uploaded = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
