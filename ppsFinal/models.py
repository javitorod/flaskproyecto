from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from init__ import db

class Usuario (db.Model, UserMixin):
    __tablename__ = 'aplicacion_user'
    id = db.Column(db.Integer, primary_key=True)
    nombre_apellido = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    contraseña = db.Column(db.String(128), nullable=False)
    lider = db.Column(db.Boolean, default=False)
    puesto = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.email}>'
    def set_contraseña(self, password):
        self.contraseña = generate_password_hash(password)
    def check_password(self, contraseña):
        return check_password_hash(self.contraseña, contraseña)
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    @staticmethod
    def get_by_id(id):
        return Usuario.query.get(id)
    @staticmethod
    def get_by_email(email):
        return Usuario.query.filter_by(email=email).first()