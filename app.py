from flask import Flask, render_template
from whitenoise import WhiteNoise

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/")

@app.route("/")
def login():
    return render_template("index.html")


if __name__=="__main__":
    app.run()


