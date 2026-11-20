
from flask import Flask, render_template, request

app = Flask(__name__)


# PAGINA PRINCIPAL
@app.route("/")
def inicio():
    return render_template("index.html")


# EJERCICIO 1: CALCULO DE NOTAS
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():

    promedio = None
    estado = None
    error = None

    if request.method == "POST":
        try:
            nota1 = float(request.form["nota1"])
            nota2 = float(request.form["nota2"])
            nota3 = float(request.form["nota3"])
            asistencia = float(request.form["asistencia"])

            if not all(10 <= nota <= 70 for nota in [nota1, nota2, nota3]):
                raise ValueError("Las notas deben estar entre 10 y 70.")

            if not 0 <= asistencia <= 100:
                raise ValueError("La asistencia debe estar entre 0 y 100.")

            promedio = (nota1 + nota2 + nota3) / 3

            if promedio >= 40 and asistencia >= 75:
                estado = "APROBADO"
            else:
                estado = "REPROBADO"

        except ValueError as e:
            error = str(e)

    return render_template(
        "ejercicio1.html",
        promedio=promedio,
        estado=estado,
        error=error
    )


# EJERCICIO 2: COMPARACION DE NOMBRES
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():

    nombre_mayor = None
    cantidad_caracteres = None
    error = None

    if request.method == "POST":
        nombre1 = request.form["nombre1"].strip()
        nombre2 = request.form["nombre2"].strip()
        nombre3 = request.form["nombre3"].strip()

        nombres = [nombre1, nombre2, nombre3]

        if not all(nombres):
            error = "Debes ingresar los tres nombres."

        elif len(set(nombre.lower() for nombre in nombres)) != 3:
            error = "Debes ingresar tres nombres diferentes."

        else:
            nombre_mayor = max(nombres, key=len)
            cantidad_caracteres = len(nombre_mayor)

    return render_template(
        "ejercicio2.html",
        nombre_mayor=nombre_mayor,
        cantidad_caracteres=cantidad_caracteres,
        error=error
    )


# INICIAR APLICACION
if __name__ == "__main__":
    app.run(debug=True)
