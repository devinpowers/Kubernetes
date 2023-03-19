from flask import Flask, render_template
import json, os, signal

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('new.html')


@app.route('/exit', methods=['GET'])
def stopServer():
    os.kill(os.getpid(), signal.SIGINT)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6000)

    