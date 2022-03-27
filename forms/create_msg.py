from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length



class OrderCreateForm(FlaskForm):
    nombre = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=20),
        ],
        render_kw={"placeholder": "Nombre"},
    )

    apellido = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=20),
        ],
        render_kw={"placeholder": "Apellido"},
    )

    correo = StringField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "Correo"},
    )

    mensaje = StringField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "Escriba su mensaje aqui"},
    )

    submit = SubmitField("Enviar")