from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def index():
    return render_template('about.html')


    return render_template('')
if __name__ == "__main__":
   app.run(debug=True)