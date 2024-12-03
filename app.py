from flask import Flask, render_template, send_file

app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route("/skills", methods=['GET'])
def skills():
    return render_template("skills.html")

@app.route("/projects", methods=['GET'])
def projects():
    return render_template("projects.html")

@app.route("/download/cv", methods=['GET'])
def download_cv():
    return send_file("./files/romain_gendreau_cv.pdf", as_attachment=True)

@app.errorhandler(404) 
def not_found(e): 
  return render_template("404.html") 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"))