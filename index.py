from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/upload", methods=['POST'])
def upload():
    return render_template('repues.html')


if __name__ == '__main__':
 # Iniciamos la aplicación
 app.run(debug=True)