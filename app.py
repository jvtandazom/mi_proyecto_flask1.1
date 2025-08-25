from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', 
                         title='Inicio',
                         welcome_message='Bienvenido a mi sitio Flask')

@app.route('/about')
def about():
    return render_template('about.html',
                         title='Acerca de',
                         description='Esta es la página acerca de nuestro proyecto')

if __name__ == '__main__':
    app.run(debug=True)