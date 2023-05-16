from flask import Flask, render_template, url_for, request
import pyttsx3

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/play", methods=['GET', 'POST'])
def play():
    text = request.form.get('text')
    converter = pyttsx3.init()
    converter.setProperty('rate', 150)
    converter.setProperty('volume', 1)
    converter.say(text)
    converter.runAndWait()
    return render_template("home.html")


if __name__ == '__main__':
    app.run()
