from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"))