from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', num_1=8, num_2=8 )

@app.route('/<int:num_1>')
def tablero(num_1):
    return render_template('index.html', num_1=num_1, num_2=8)

@app.route('/<int:num_1>/<int:num_2>')
def tablero_2(num_1, num_2):
    return render_template('index.html', num_1=num_1, num_2= num_2)

@app.route('/<int:num_1>/<int:num_2>/<string:color1>/<string:color2>')
def tablero_colores(num_1, num_2, color1, color2):
    return render_template('index.html', num_1=num_1, num_2= num_2, color1=color1, color2=color2)

if __name__ == '__main__':
    app.run(debug=True)