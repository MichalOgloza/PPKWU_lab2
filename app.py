from flask import Flask, jsonify

from StringInfo import StringInfo

app = Flask(__name__)


@app.route('/')
def home():
    return "This API counts characters of various types in string. Available at address: /count/[textArgument]"


@app.route("/count/<text>")
def count(text):
    upper_count = sum(1 for c in text if c.isupper())
    lower_count = sum(1 for c in text if c.islower())
    digit_count = sum(1 for c in text if c.isdigit())
    special_count = sum(1 for c in text if not (c.isalpha() or c.isdigit()))
    response = StringInfo(upper_count, lower_count, digit_count, special_count)
    return jsonify(response.__dict__)


if __name__ == '__main__':
    app.run(debug=True)
