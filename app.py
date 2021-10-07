from flask import Flask
from flask.helpers import url_for
from views import frontpage

app = Flask(__name__)
app.register_blueprint(frontpage, url_prefix="/frontpage")

if __name__ == '__main__':
    app.run(debug=True, port=5599)