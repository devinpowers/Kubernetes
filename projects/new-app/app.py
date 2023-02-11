from flask import Flask, render_template
app = Flask(__name__)


images = [
    "https://giphy.com/embed/QYgMSTflahPilFkmVf/video"
]


@app.route('/')
def index():
    return render_template('index.html', url=images)

@app.route('/error')
def error():
    return '', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
