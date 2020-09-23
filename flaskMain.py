from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        size = request.form['size']
        repeat = request.form['repeat']
        data = request.form['data']
        return render_template('dataShow.html', size = size, repeat = repeat, data = data)
    return render_template('index.html')

@app.route("/back", methods = ["GET", "POST"])
def back():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug = True)