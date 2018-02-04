import flask
import random
from flask_cors import CORS, cross_origin
app = flask.Flask(__name__)

CORS(app)

@app.route("/api/battles/public")
def hello():
    response = flask.jsonify(
		[{
		  "id": 1111,
		  "name": 'Startup NYC',
		  "sponsor": 'Alec Pesola',
		  "seedFund": '{}k'.format(random.uniform(100, 999))
		},
		{
		  "id": 1112,
		  "name": 'Startup Ontario',
		  "sponsor": 'Ryan Chenkie',
		  "seedFund": '{}k'.format(random.uniform(100, 999))
		},
		{
		  "id": 1113,
		  "name": 'Startup Uttah',
		  "sponsor": 'Diego Poza',
		  "seedFund": '{}k'.format(random.uniform(100, 999))
		}]
	)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(port=3333)
