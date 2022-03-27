
from email import message
from Models.Messages import Message
from Landing.db import landingdb
from flask import Blueprint, render_template, redirect, url_for
from forms.create_msg import OrderCreateForm

msg = Blueprint("msg", __name__)


@msg.route("/", methods=["GET", "POST"])
def messages():
    form = OrderCreateForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        apellido = form.apellido.data
        correo = form.correo.data
        mensaje = form.mensaje.data
        newMessage = Message(nombre, apellido, correo, mensaje)
        landingdb.session.add(newMessage)
        landingdb.session.commit()
        return redirect(url_for("msg.messages"))
    return render_template("home.html", form=form)


@msg.route("/messagen")
def listmsg():
    currentmsglist = Message.querye.all()
    return render_template("todolist/tasklist.html", Messages=currentmsglist)

     




