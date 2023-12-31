from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/complete')
def complete():
    return render_template("complete.html")


@app.route('/ministries')
def ministries():
    return render_template("ministries.html")

@app.route('/programs')
def programs():
    return render_template("programs.html")

@app.route('/mobil')
def mobil():
    return render_template("mobil.html")


app.run("0.0.0.0", port=27172, debug=True)