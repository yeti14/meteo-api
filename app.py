#!flask/bin/python
from flask import Flask, jsonify
from datetime import datetime
import bmp180


app = Flask(__name__)

@app.route('/meteo-api',methods=['GET'])
def get_meteo():
	(temperature,pressure)=bmp180.readBmp180()
	meteo = {
		  'temperature': temperature,
		  'pressure': pressure,
		  'timestamp' : datetime.now()
		}
	return jsonify(meteo)

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)

