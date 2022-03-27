from Landing.db import landingdb
class Message(landingdb.Model):
    id = landingdb.Column(landingdb.Integer, primary_key=True)
    nombre = landingdb.Column(landingdb.String(20), nullable=False)
    apellido = landingdb.Column(landingdb.String(20), nullable=False)
    correo = landingdb.Column(landingdb.String(20), nullable=False)
    mensaje = landingdb.Column(landingdb.String(300), nullable=False)

    def __init__(self, nombre, apellido, correo, mensaje) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.mensaje = mensaje
    def __repr__(self) -> str:
        return f"Message({self.id}, {self.nombre}, '{self.apellido}', '{self.correo}', '{self.mensaje}')"