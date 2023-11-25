from flask import Flask, render_template
import requests
from dotenv import load_dotenv, dotenv_values

config = dotenv_values('.env')

app=Flask(__name__)

def get_weather_data(city):
    API_KEY = config['API_KEY']
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&lang=es&units=metric&appid={API_KEY}'
    r = requests.get(url).json()
    print(r)
    return r 

@app.route('/prueba')
def prueba():
    clima=get_weather_data( 'Ambato')
    temperatura = str(clima['main']['temp'])
    descripcion = str(clima ['weather'][0]['description'])
    icono = str(clima['weather'][0]['icon'])

    r_json = {
    'ciudad':'Ambato',
    'temperatura': temperatura,
    'descripcion': descripcion,
    'icono':icono
    }
    return render_template('weather.html',clima= r_json)

@app.route('/about1')
def about1():
    return render_template('CVBAJANA.html')

@app.route('/about2')
def about2():
    return render_template('CVCAICE.html')

@app.route('/about3')
def about3():
    return render_template('CVCORONEL.html')

@app.route('/about4')
def about4():
    return render_template('CVFONG.html')

@app.route('/about5')
def about5():
    return render_template('CVGALLARDO.html')

@app.route('/about6')
def about6():
    return render_template('CVGUERRERO.html')

if __name__=='__main__':
    app.run(debug=True)
