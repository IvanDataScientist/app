
# Ejemplo sencillo en flask, cargamos un template home.html por defecto
# si navegamos hasta /info podemos ejecutar nuestra función la cual puede extraer la data
# y mostrar un dashboard por ejemplo: un analisis actual del covid-19
from flask import Flask, render_template

app = Flask(__name__) # archivo principal de arranque

#Usamos un decorador
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/info')
def info():
    return "Mas info"


if __name__ == '__main__':
    app.run()


# OUT: Obtenemos acceso a nuestra app mediante la dirección local y puerto que nos muestra.
# Si queremos ejecutar la app desde internet podemos usar un servicio gratuito como heroku
#E:\RepoPython\app_web_covid-19>python index.py
# * Serving Flask app "index" (lazy loading)
# * Environment: production
#   WARNING: This is a development server. Do not use it in a production deployment.
#   Use a production WSGI server instead.
# * Debug mode: off
# * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
#127.0.0.1 - - [07/Sep/2020 11:33:20] "GET / HTTP/1.1" 200 -