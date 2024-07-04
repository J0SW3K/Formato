from app import db

class Ejemplo(db.Model):
    id_ejemplo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ejemplo = db.Column(db.String(50), nullable=False)