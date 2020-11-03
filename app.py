from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "This API counts characters of various types in string. Available at address: /count/[textArgument]"


if __name__ == '__main__':
    app.run(debug=True)
