from flask import Flask, render_template, url_for, request
import pyttsx3

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text')
        converter = pyttsx3.init()
        converter.setProperty('rate', 150)
        converter.setProperty('volume', 1)
        converter.say(text)
        converter.runAndWait()
    else:
        return render_template("home.html")
    return render_template("home.html")


if __name__ == '__main__':
    app.run()
