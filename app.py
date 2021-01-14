from flask import Flask
from API import endpoints

app = Flask(__name__)
app.register_blueprint(endpoints.endpoints)


if __name__ == '__main__':
    app.run(host= '0.0.0.0')