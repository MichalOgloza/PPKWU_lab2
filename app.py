from flask import Flask

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
    return "upper_count: {0} <br/> lower_count: {1} <br/> digit_count: {2} <br/> special_count: {3}"\
        .format(upper_count, lower_count, digit_count, special_count)


if __name__ == '__main__':
    app.run(debug=True)
