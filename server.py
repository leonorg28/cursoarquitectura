from flask import Flask, render_template, request
from database.db import *
app = Flask(__name__)

@app.route("/")
def home_func():
    ##return render_template("home.html")
    return "Test"
@app.route("/home",methods = ["get"])
def home_func_test():
    return "Test"

@app.route("/register_page")
def register_page_func():
    return render_template("register.html")

@app.route("/register_user",methods = ["post"])
def register_render_user():
    data = request.form
    id = data["id"]
    name = data["name"]
    lastname = data["lastname"]
    birthday = data["birthday"]
    add_user(id, name, lastname, birthday)
    return "the user was added"

@app.route("/registo_act", methods=["post"])
def register_render_act():
    data = request.form
    tipo_actividad = data["tipo_actividad"]
    descripcion_actividad = data["descripcion"]
    responsable_actividad = data["responsable"]
    tiempo_actividad = data["duracion"]
    fecha_asignacion = data["fecha"]
    estado_actividad = data["estado"]
    observaciones = data["observaciones"]
    add_actividad(tipo_actividad,descripcion_actividad,responsable_actividad,tiempo_actividad,fecha_asignacion,estado_actividad,observaciones)
    return "la actividad fue creada con exito"

@app.route("/consult_page")
def consult_page_func():
 return "la actividad fue creada con exito"
 
if __name__ == "__main__":
    host = "172.31.41.168"
    port = "80"
    app.run(host, port)
    # app.run()
