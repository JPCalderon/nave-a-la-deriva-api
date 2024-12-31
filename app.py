from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# Sistema dañado seleccionado al azar
import random

systems = {
    "navigation": "NAV-01",
    "communications": "COM-02",
    "life_support": "LIFE-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05"
}
damaged_system = random.choice(list(systems.keys()))


# Primera llamada: GET /status
@app.route("/status", methods=["GET"])
def status():
    return jsonify({"damaged_system": damaged_system})


# Segunda llamada: GET /repair-bay
@app.route("/repair-bay", methods=["GET"])
def repair_bay():
    system_code = systems[damaged_system]
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Repair</title>
    </head>
    <body>
        <div class="anchor-point">{system_code}</div>
    </body>
    </html>
    """
    return render_template_string(html_content)


# Tercera llamada: POST /teapot
@app.route("/teapot", methods=["POST"])
def teapot():
    return "I'm a teapot", 418


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
