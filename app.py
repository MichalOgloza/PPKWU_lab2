from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "This API counts characters of various types in string. Available at address: /count/[textArgument]"


@app.route("/count/<text>")
def count(text):
    upper_count = sum(1 for c in text if c.isupper())
    return "upper_count: {}".format(upper_count)


if __name__ == '__main__':
    app.run(debug=True)
