from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html") #if the file is in another file, specify the path

if __name__ == "__main__":
    app.run(debug=True)