from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "1132c42b947133a83aeb7b5c2d94c376"  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')  
    if city:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'icon': data['weather'][0]['icon']
            }
            return jsonify(weather_data)
        else:
            return jsonify({'error': 'City not found'}), 404
    return jsonify({'error': 'No city provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
