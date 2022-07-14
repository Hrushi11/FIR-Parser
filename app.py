from parser_call import PdfParser
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
parser = PdfParser("FIR Sample update.pdf")

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/api")
def check():
    content = parser.get_content()
    return jsonify(content)

if __name__ == "__main__":
    app.run(debug=True)
