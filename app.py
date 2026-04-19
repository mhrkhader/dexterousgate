from flask import Flask, render_template

app = Flask(__name__)

# Home page
@app.route("/")
def index():
    return render_template("index.html")

# Excel page
@app.route("/excel")
def excel():
    return render_template("excel.html")


if __name__ == "__main__":
    app.run(debug=True)