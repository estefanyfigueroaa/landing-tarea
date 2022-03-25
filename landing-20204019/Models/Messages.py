from Landing.db import db


class message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.Integer, nullable=False)
    apellido = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(15), nullable=False)

    def __init__(self, userId, description, status="new") -> None:
        self.userId = userId
        self.description = description
        self.status = status

    def __repr__(self) -> str:
        return f"Task({self.id}, {self.userId}, '{self.description}', '{self.status}')"