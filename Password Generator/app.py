from flask import Flask, render_template, request, make_response, redirect, url_for
import password as pswd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=["POST", "GET"])
def checking():
    if request.method == "POST":
        lengthPassword = int(request.form['lengthPassword'])
        Symbols = request.form.get('Symbols')
        Characters = request.form.get('Characters')
        Numbers = request.form.get('Numbers')
        password = pswd.generate_random_password(length = lengthPassword, symbols = Symbols, characters = Characters, numbers = Numbers)
        return render_template('index.html',i = password)


app.run(debug=True)
