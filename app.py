from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here #https://machinelearningprojects.net/flight-price-prediction/
    return 'Hello World!' # https://github.com/sharmaji27/Flight-Price-Prediction/blob/master/flight%20price.ipynb


if __name__ == '__main__':
    app.run()
